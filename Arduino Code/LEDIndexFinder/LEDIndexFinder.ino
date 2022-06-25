#include <FastLED.h>

// NOTABLE INDICIES 
/*
 *  Hot leg of secondary  START: 33  END 65
 *  Cold leg of primary   START: 74  END 140
 *  Hot leg of primary    START: 153 END 182
 *  Cold log of secondary START: 192 END 215
 */

// How many leds in your strip?
#define NUM_LEDS 240

#define DATA_PIN 10    // pin to LEDS
#define CLOCK_PIN 13

// Define the array of leds
CRGB leds[NUM_LEDS];

int curInd = 0;
int prevInd = 0;
int delVal = 10;

void setup() {
  Serial.begin(115200);
  FastLED.addLeds<WS2812B, DATA_PIN, GRB>(leds, NUM_LEDS);  // GRB ordering is typical for WS2812B

}

void loop() {

  prevInd = curInd - 1;
  if (prevInd == -1) {
    prevInd = NUM_LEDS - 1;
  }


  leds[curInd] = CRGB(0, 0, 100);
  leds[prevInd] = CRGB(0, 0, 0);


  if (Serial.available()) {
    Serial.read();
    curInd++;
    if (curInd >= NUM_LEDS) {
      curInd = 0;
    }
  }
  else{
    Serial.println(curInd);
  }

  FastLED.show();
  delay(delVal);
}
