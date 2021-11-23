#include <Servo.h>

int servoPins[4] = {8, 9, 10, 11};
Servo servo[4];
int angle[4] = {
    0,
};

String Split(String data, char separator, int index)
{
  int found = 0;
  int strIndex[] = {0, -1};
  int maxIndex = data.length() - 1;

  for (int i = 0; i <= maxIndex && found <= index; i++)
  {
    if (data.charAt(i) == separator || i == maxIndex)
    {
      found++;
      strIndex[0] = strIndex[1] + 1;
      strIndex[1] = (i == maxIndex) ? i + 1 : i;
    }
  }

  return found > index ? data.substring(strIndex[0], strIndex[1]) : "";
}

void sendSerial(String str)
{
  Serial.println("Send: " + str);
}

void setup()
{
  Serial.begin(9600);
  Serial.setTimeout(20); 
  for (int i = 0; i < 3; i++)
  {
    servo[i].attach(servoPins[i]);
    servo[i].write(0);
  }
}

void loop()
{
  if (Serial.available())
  {
    String str = Serial.readString();
    String first = Split(str, ',', 0);
    String second = Split(str, ',', 1);

    sendSerial(first + " " + second);

    for (int i = 0; i < 3; i++)
    {
      angle[first.toInt()] = second.toInt();
    }
  }

  for (int i = 0; i < 3; i++)
  {
    servo[i].write(angle[i]);
  }
}
