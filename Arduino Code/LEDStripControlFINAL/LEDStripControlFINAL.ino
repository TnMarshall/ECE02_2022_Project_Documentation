#include <FastLED.h>

// How many leds in your strip?
#define NUM_LEDS 240

// For led chips like WS2812, which have a data line, ground, and power, you just
// need to define DATA_PIN.  For led chipsets that are SPI based (four wires - data, clock,
// ground, and power), like the LPD8806 define both DATA_PIN and CLOCK_PIN
// Clock pin only needed for SPI based chipsets when not using hardware SPI
#define DATA_PIN 10    // pin to LEDS
#define CLOCK_PIN 13

#define CONTROL_PIN 9  // pin to pther Arduino

int delVal = 70;
int LEDstatePri = 0;
int LEDstateSec = 0;
int pinState = 0;

int animArray[] = {30, 20, 10, 5, 1, 0, 0}; //0,1,5,10,20,30,40

int temp = 0;
// Define the array of leds
CRGB leds[NUM_LEDS];


// NOTABLE INDICIES
/*
    Hot leg of secondary  START: 33  END 65
    Cold leg of primary   START: 74  END 140
    Hot leg of primary    START: 153 END 182
    Cold log of secondary START: 191 END 217
*/

#define coldSecStart 191
#define coldSecEnd   217
#define hotSecStart  33
#define hotSecEnd    65

#define coldPriStart 74
#define coldPriEnd   140
#define hotPriStart  153
#define hotPriEnd    182


void setup() {
  pinMode(CONTROL_PIN, INPUT);
  FastLED.addLeds<WS2812B, DATA_PIN, GRB>(leds, NUM_LEDS);  // GRB ordering is typical for WS2812B
}

void loop() {
  pinState = digitalRead(CONTROL_PIN);
  if (pinState) {
    for (int i = 0; i < NUM_LEDS; i++) {
      //      for (int i = NUM_LEDS-1; i >= 0; i--) {
      if (LEDstateSec >= 7) {
        LEDstateSec = 0;
      }
      if ((i >= coldSecStart) && (i <= coldSecEnd))
        leds[i] = CRGB(0, 0, animArray[LEDstateSec]);
      else if ((i >= hotSecStart) && (i <= hotSecEnd))
        leds[i] = CRGB(animArray[LEDstateSec], 0, 0);
      LEDstateSec++;

    }

    //    for (int i = 0; i < NUM_LEDS; i++) {
    for (int i = NUM_LEDS - 1; i >= 0; i--) {
      if (LEDstatePri >= 7) {
        LEDstatePri = 0;
      }
      if ((i >= coldPriStart) && (i <= coldPriEnd))
        leds[i] = CRGB(0, 0, animArray[LEDstatePri]);
      else if ((i >= hotPriStart) && (i <= hotPriEnd))
        leds[i] = CRGB(animArray[LEDstatePri], 0, 0);
      LEDstatePri++;

    }

    temp = animArray[6];
    for (int i = 6; i > 0; i--) {
      animArray[i] = animArray[i - 1];
    }
    animArray[0] = temp;

    for (int i = 0; i < NUM_LEDS; i++) {
      if (!((i >= coldSecStart) && (i <= coldSecEnd)) && !((i >= hotSecStart) && (i <= hotSecEnd)) && !((i >= coldPriStart) && (i <= coldPriEnd)) && !((i >= hotPriStart) && (i <= hotPriEnd)))
        leds[i] = CRGB(0, 0, 0);
    }

    FastLED.show();
    delay(delVal);
  }
  else {
    FastLED.show();
  }
}
