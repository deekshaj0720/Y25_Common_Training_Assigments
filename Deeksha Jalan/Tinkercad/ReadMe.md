## Logic 

First, we assign variables to the LDR,Temperature Sensor and both the LEDs. Then, we decalre the LEDs as output so that they can glow as required. 

- LED 1 - Light LED glows when the surroundings are dark as read by LDR. 
- LED 2 - Fan LED glows when the temperature is high(above 30C). So, we read the temperature using TMP sensor and convert the voltage given by it to temperature. As the sensor gives a value from 0 to 1023, we first convert it such that voltage lies between 0-5V. And accordingly, calculate the temperature.

Lastly, a delay of 200 is given in the loop so that the system is not overloaded and a delay of 0.2s is present to ensure smooth function.



## CODE
```cpp

// C++ code

int LDR = A0;
int tempSensor = A1;

int lightLED = 8;
int fanLED = 9;

void setup() {

  pinMode(lightLED, OUTPUT);
  pinMode(fanLED, OUTPUT);

  Serial.begin(9600);
}

void loop() {

  // -------- LDR --------
  int ldrValue = analogRead(LDR);

  Serial.print("LDR Value: ");
  Serial.println(ldrValue);

  // Dark condition
  if (ldrValue < 500) {
    digitalWrite(lightLED, HIGH);
  }
  else {
    digitalWrite(lightLED, LOW);
  }

  // -------- Temperature --------
  int tempValue = analogRead(tempSensor);

  float voltage = tempValue * (5.0 / 1023.0);

  float temperature = (voltage - 0.5) * 100;

  Serial.print("Temperature: ");
  Serial.println(temperature);

  // High temperature condition
  if (temperature > 30) {
    digitalWrite(fanLED, HIGH);
  }
  else {
    digitalWrite(fanLED, LOW);
  }

  delay(200);
}

```