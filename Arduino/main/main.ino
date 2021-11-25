#include <ArduinoJson.h>
#include <Servo.h>

const int capacity = JSON_OBJECT_SIZE(3);

char servoPins[3] = {8, 9, 10};
Servo servo[3];
int angle[3] = {
    90, 20, 100
};

void sendSerial(String str)
{
  Serial.println("Send: " + str);
}

void sendStatus()
{
  StaticJsonDocument<24> doc;

  doc["0"] = angle[0];
  doc["1"] = angle[1];
  doc["2"] = angle[2];
  String output;
  serializeJson(doc, output);
  Serial.println(output);
}

void setup()
{
  Serial.begin(115200);
  Serial.setTimeout(200);

  for (char i = 0; i < 3; i++)
  {
    servo[i].attach(servoPins[i]);
    servo[i].write(0);
  }
}

void loop()
{
  if (Serial.available())
  {
    //sendSerial(first + " " + second);
    for (char i = 0; i < 3; i++)
    {
      angle[i] = Serial.parseInt();
    }

    sendStatus();
  }

  for (char i = 0; i < 3; i++)
  {
    servo[i].write(angle[i]);
  }
}
