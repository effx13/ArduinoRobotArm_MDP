package com.example.arduinorobotarmcontrol;

import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothSocket;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;
import android.widget.SeekBar;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Set;

public class MainActivity extends AppCompatActivity {

    Set<BluetoothDevice> pairedDevices;
    ArrayAdapter<String> btArrayAdapter;
    ArrayList<String> deviceAddressArray;
    BluetoothAdapter btAdapter;
    TextView textStatus;

    ListView listView;
    private final static int REQUEST_ENABLE_BT = 1;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        listView = (ListView) findViewById(R.id.listview);
        SeekBar seekBarX = findViewById(R.id.seekBar_X);
        SeekBar seekBarY = findViewById(R.id.seekBar_Y);
        SeekBar seekBarZ = findViewById(R.id.seekBar_Z);
        TextView X_Value = findViewById(R.id.XValue);
        TextView Y_Value = findViewById(R.id.YValue);
        TextView Z_Value = findViewById(R.id.ZValue);
        Button btnPaired = findViewById(R.id.btn_paired);
        Button submit_button = findViewById(R.id.change_button);

        btAdapter = BluetoothAdapter.getDefaultAdapter();

        seekBarX.setOnSeekBarChangeListener(new SeekbarChanged(X_Value));
        seekBarY.setOnSeekBarChangeListener(new SeekbarChanged(Y_Value));
        seekBarZ.setOnSeekBarChangeListener(new SeekbarChanged(Z_Value));

        btnPaired.setOnClickListener(this::onClickButtonPaired);
        listView.setOnItemClickListener(new myOnItemClickListener());

        btArrayAdapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1);
        deviceAddressArray = new ArrayList<>();
        listView.setAdapter(btArrayAdapter);
        submit_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast t = Toast.makeText(getApplicationContext(), "X: " + seekBarX.getProgress() + " Y: " + seekBarY.getProgress() + " Z: " + seekBarZ.getProgress(), Toast.LENGTH_LONG);
                t.show();

            }
        });


    }
    public void onClickButtonPaired(View view){
        btArrayAdapter.clear();
        if(deviceAddressArray!=null && !deviceAddressArray.isEmpty()){ deviceAddressArray.clear(); }
        pairedDevices = btAdapter.getBondedDevices();
        if (pairedDevices.size() > 0) {
            // There are paired devices. Get the name and address of each paired device.
            for (BluetoothDevice device : pairedDevices) {
                String deviceName = device.getName();
                String deviceHardwareAddress = device.getAddress(); // MAC address
                btArrayAdapter.add(deviceName);
                deviceAddressArray.add(deviceHardwareAddress);
            }
        }
    }
    public class myOnItemClickListener implements AdapterView.OnItemClickListener {

        @Override
        public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
            Toast.makeText(getApplicationContext(), btArrayAdapter.getItem(position), Toast.LENGTH_SHORT).show();

            textStatus.setText("try...");

            final String name = btArrayAdapter.getItem(position); // get name
            final String address = deviceAddressArray.get(position); // get address
            boolean flag = true;

            BluetoothDevice device = btAdapter.getRemoteDevice(address);

            // create & connect socket
            try {
                btSocket = createBluetoothSocket(device);
                btSocket.connect();
            } catch (IOException e) {
                flag = false;
                textStatus.setText("connection failed!");
                e.printStackTrace();
            }

            if(flag){
                textStatus.setText("connected to "+name);
                connectedThread = new ConnectedThread(btSocket);
                connectedThread.start();
            }

        }

    }
}




