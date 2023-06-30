#include <Arduino.h>

void setup() {
  pinMode(LED_BUILTIN,OUTPUT);    // set digital pin connected to LED as output
}

void loop() {
  digitalWrite(LED_BUILTIN,HIGH); // turn LED ON
  delay(1000);                    //wait for 500 milliseconds
  digitalWrite(LED_BUILTIN,LOW);  // turn OFF the LED
  delay(1000);                    //wait for 500 milliseconds

}