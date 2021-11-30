package com.example.arduinorobotarmcontrol;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.SeekBar;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        BluetoothModule bluetoothModule = new BluetoothModule(this);

        SeekBar seekBarX = findViewById(R.id.seekBar_X);
        SeekBar seekBarY = findViewById(R.id.seekBar_Y);
        SeekBar seekBarZ = findViewById(R.id.seekBar_Z);
        TextView X_Value = findViewById(R.id.XValue);
        TextView Y_Value = findViewById(R.id.YValue);
        TextView Z_Value = findViewById(R.id.ZValue);
        Button submit_button = findViewById(R.id.change_button);

        seekBarX.setOnSeekBarChangeListener(new SeekbarChanged(X_Value));
        seekBarY.setOnSeekBarChangeListener(new SeekbarChanged(Y_Value));
        seekBarZ.setOnSeekBarChangeListener(new SeekbarChanged(Z_Value));
        submit_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast t = Toast.makeText(getApplicationContext(), "X: " + seekBarX.getProgress() + " Y: " + seekBarY.getProgress() + " Z: " + seekBarZ.getProgress(), Toast.LENGTH_LONG);
                t.show();
            }
        });
    }
}



