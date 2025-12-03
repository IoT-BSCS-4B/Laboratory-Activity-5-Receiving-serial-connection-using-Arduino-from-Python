#include "led_functions.h"

void setup() {
  Serial.begin(9600); // Initialize serial communication
  setupLEDPins();     // Call function from header file
}

void loop() {
  if (Serial.available() > 0) {
    char input = Serial.read();

    // Logic based on input
    switch (input) {
      // Toggle Red
      case 'R':
      case 'r':
        toggleLED(RED_PIN);
        Serial.println("Red Toggled");
        break;

      // Toggle Green
      case 'G':
      case 'g':
        toggleLED(GREEN_PIN);
        Serial.println("Green Toggled");
        break;

      // Toggle Blue
      case 'B':
      case 'b':
        toggleLED(BLUE_PIN);
        Serial.println("Blue Toggled");
        break;

      // All ON
      case 'A':
      case 'a':
        turnAllOn();
        Serial.println("All ON");
        break;

      // All OFF
      case 'O':
      case 'o':
        turnAllOff();
        Serial.println("All OFF");
        break;
      
      // Handle newline characters (ignore them)
      case '\n':
      case '\r':
        break;

      // Error handling
      default:
        Serial.println("Error: Invalid Input");
        break;
    }
  }
}