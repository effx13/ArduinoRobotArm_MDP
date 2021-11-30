package com.example.arduinorobotarmcontrol;

import android.Manifest;
import android.app.Activity;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.content.Intent;

import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;

import androidx.core.app.ActivityCompat;

import java.util.*;

public class BluetoothModule {
    Activity activity;
    public BluetoothModule(Activity activity) {
        this.activity = activity;
    }

    BluetoothAdapter mBluetoothAdapter;
    Set<BluetoothDevice> mPairedDevices;
    List<String> mListPairedDevices;
    Set<BluetoothDevice> pairedDevices;
    ArrayAdapter<String> btArrayAdapter;
    ArrayList<String> deviceAddressArray;



    final static int BT_REQUEST_ENABLE = 1;
    final static int BT_MESSAGE_READ = 2;
    final static int BT_CONNECTING_STATUS = 3;
    final static UUID BT_UUID = UUID.fromString("00001101-0000-1000-8000-00805F9B34FB");
    public BluetoothModule() {
        String[] permission_list = {
                Manifest.permission.ACCESS_FINE_LOCATION,
                Manifest.permission.ACCESS_COARSE_LOCATION
        };

        ActivityCompat.requestPermissions(activity, permission_list,  1);
        BluetoothAdapter btAdapter;
        final int REQUEST_ENABLE_BT = 1;

        protected void onCreate(Bundle savedInstanceState) {
            ListView listView = (ListView) findViewById(R.id.listview);
            Button btnParied = (Button) findViewById(R.id.btn_paired);

            // Enable bluetooth
            btAdapter = BluetoothAdapter.getDefaultAdapter();
            if (!btAdapter.isEnabled()) {
                Intent enableBtIntent = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
                startActivityForResult(enableBtIntent, REQUEST_ENABLE_BT);
            }
            btArrayAdapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1);
            deviceAddressArray = new ArrayList<>();
            listView.setAdapter(btArrayAdapter);
        }
        public void onClickButtonPaired(View view{
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



    }

    private void startActivityForResult(Intent enableBtIntent, int request_enable_bt) {
    }
}
