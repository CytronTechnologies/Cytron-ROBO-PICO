/*
DESCRIPTION:
This example code will uses: Robo Pico and Raspberry Pi Pico / Pico W
to read analog value on the Maker Line.
This code applicable to other analog sensor.

CONNECTION:
Robo Pico : Maker Line
GROVE 6   - Maker Line Grove
GP27      - OUT

AUTHOR  : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io
*/

int sensorPin = 27;    // select the input pin for the potentiometer
int raw_value = 0; 
float voltage_value = 0; 

void setup() {
  // declare the ledPin as an OUTPUT:
  pinMode(sensorPin, INPUT);
  Serial.begin(9600);
  // enable adc resolution to 12-bit (default 10-bit)
  analogReadResolution(12);
}

void loop() {
  // read the value from the sensor:
  raw_value = analogRead(sensorPin);
  voltage_value = (raw_value * 3.3) / 4095;
  Serial.print("Raw Value : ");
  Serial.println(raw_value);
  Serial.print("Voltage Value : ");
  Serial.println(voltage_value);
  Serial.println("---------------------------");
  
  delay(1000);
}
