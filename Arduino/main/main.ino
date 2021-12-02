#include <ArduinoJson.h>
#include <Servo.h>

const int capacity = JSON_OBJECT_SIZE(3);

char servoPins[3] = {8, 9, 10};
Servo servo[3];
int angle[3] = { // 기본 초기 각도 설정
    150, 160, 170
};

void sendStatus() // 현재 각도 시리얼로 전송
{
  StaticJsonDocument<24> doc;

  doc["0"] = angle[0];
  doc["1"] = angle[1];
  doc["2"] = angle[2];
  String output;
  serializeJson(doc, output); // 데이터 JSON으로 변환
  Serial.println(output);
}

void setup()
{
  Serial.begin(115200);
  Serial.setTimeout(200);

  for (char i = 0; i < 3; i++) // 서보 모터 초기화
  {
    servo[i].attach(servoPins[i]);
    servo[i].write(angle[i]);
  }
}

void loop()
{
  if (Serial.available())
  {
    for (char i = 0; i < 3; i++)
    {
      angle[i] = Serial.parseInt(); // 데이터 받아서 각도 지정
    }

    sendStatus();
  }

  for (char i = 0; i < 3; i++)
  {
    servo[i].write(angle[i]); // 계속해서 각도 설정
  }
}
