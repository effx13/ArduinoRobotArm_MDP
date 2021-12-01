package com.example.arduinorobotarmcontrol;

import android.bluetooth.BluetoothSocket;
import android.os.SystemClock;
import android.widget.Toast;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

class ConnectedBluetoothThread extends Thread {
    private final MainActivity mainActivity;
    private final BluetoothSocket mmSocket;
    private final InputStream mmInStream;
    private final OutputStream mmOutStream;

    public ConnectedBluetoothThread(MainActivity mainActivity, BluetoothSocket socket) {
        this.mainActivity = mainActivity;
        mmSocket = socket;
        InputStream tmpIn = null;
        OutputStream tmpOut = null;

        try {
            tmpIn = socket.getInputStream();
            tmpOut = socket.getOutputStream();
        } catch (IOException e) {
            Toast.makeText(mainActivity.getApplicationContext(), "소켓 연결 중 오류가 발생했습니다.", Toast.LENGTH_LONG).show();
        }

        mmInStream = tmpIn;
        mmOutStream = tmpOut;
    }

    public void run() {
        byte[] buffer = new byte[1024];
        int bytes;

        while (true) {
            try {
                bytes = mmInStream.available();
                if (bytes != 0) {
                    SystemClock.sleep(100);
                    bytes = mmInStream.available();
                    bytes = mmInStream.read(buffer, 0, bytes);
                    mainActivity.mBluetoothHandler.obtainMessage(MainActivity.BT_MESSAGE_READ, bytes, -1, buffer).sendToTarget();
                }
            } catch (IOException e) {
                break;
            }
        }
    }

    public void write(String str) {
        byte[] bytes = str.getBytes();
        try {
            mmOutStream.write(bytes);
        } catch (IOException e) {
            Toast.makeText(mainActivity.getApplicationContext(), "데이터 전송 중 오류가 발생했습니다.", Toast.LENGTH_LONG).show();
        }
    }

    public void cancel() {
        try {
            mmSocket.close();
        } catch (IOException e) {
            Toast.makeText(mainActivity.getApplicationContext(), "소켓 해제 중 오류가 발생했습니다.", Toast.LENGTH_LONG).show();
        }
    }
}
