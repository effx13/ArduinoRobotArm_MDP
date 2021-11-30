package com.example.arduinorobotarmcontrol;

import android.util.Log;
import android.widget.SeekBar;
import android.widget.TextView;

import java.text.CollationElementIterator;

public class SeekbarChanged implements SeekBar.OnSeekBarChangeListener {
    TextView value;

    public SeekbarChanged(TextView value) {
        this.value = value;
    }

    @Override
    public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {
        // onProgressChange - Seekbar 값 변경될때마다 호출
        Log.d("X", String.format("onProgressChanged 값 변경 중 : progress [%d] fromUser [%b]", progress, fromUser));
        value.setText(String.valueOf(seekBar.getProgress()));
    }

    @Override
    public void onStartTrackingTouch(SeekBar seekBar) {
        // onStartTeackingTouch - SeekBar 값 변경위해 첫 눌림에 호출
        Log.d("X", String.format("onStartTrackingTouch 값 변경 시작 : progress [%d]", seekBar.getProgress()));
    }

    @Override
    public void onStopTrackingTouch(SeekBar seekBar) {
        // onStopTrackingTouch - SeekBar 값 변경 끝나고 드래그 떼면 호출
        Log.d("X", String.format("onStopTrackingTouch 값 변경 종료: progress [%d]", seekBar.getProgress()));
    }
}
