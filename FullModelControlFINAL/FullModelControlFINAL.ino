#include <Adafruit_MotorShield.h>
#include <FastLED.h>

// How many leds in your strip?
#define NUM_LEDS 240

#define DATA_PIN 9
#define CLOCK_PIN 13

int delVal = 70;
int LEDstate = 0;

int numPos = 8;
int numPost []  = {0, 0, 0, 0, 0, 0, 0, 0};
int numIn[] = {0, 0, 0, 0, 0, 0, 0, 0};
//             stepper1, stepper2, reactivityLight, clutch1, clutch2, pump1, pump2, pumpLights
/*
    stepper1 should be the position in degrees - NOTE CURRENTLY IN STEPS
    stepper2 should be the position in degrees
    reactivityLight should be 0-255
    clutch1 should be 0 for off and 1 for on
    clutch2 should be 0 for off and 1 for on
    pump1 should be 0 for off and 1 for on
    pump2 should be 0 for off and 1 for on
    pumpLights should be 0 for off and 1 for on
*/

int animArray[] = {30, 20, 10, 5, 1, 0, 0}; //0,1,5,10,20,30,40

int temp = 0;
// Define the array of leds
CRGB leds[NUM_LEDS];

int counter = 0;
int steps1 = 0;
int steps2 = 0;

const int reactivityPin = 9;
const int clutchPin1 = 28;     //left motor
const int clutchPin2 = 29;     //right motor
const int pumpPin1 = 26;
const int pumpPin2 = 27;
const int pumpLightPin = 31;

bool startCycle = false;
bool endCycle = false;
bool cycleFailed = false;
char curChar = ' ';

Adafruit_MotorShield AFMS = Adafruit_MotorShield(); // Default address, no jumpers

// Connect two steppers with 200 steps per revolution (1.8 degree)
// to the top shield
Adafruit_StepperMotor *myStepper1 = AFMS.getStepper(200, 2); //left stepper (from back)
Adafruit_StepperMotor *myStepper2 = AFMS.getStepper(200, 1); //right stepper (from back)

void setup() {

  Serial.begin(115200);
  FastLED.addLeds<WS2812B, DATA_PIN, GRB>(leds, NUM_LEDS);  // GRB ordering is typical for WS2812B

  if (!AFMS.begin()) {         // create with the default frequency 1.6KHz
    Serial.println("Could not find Motor Shield. Check wiring.");
    while (1);
  }
  Serial.println("Motor Shield found.");

  pinMode(reactivityPin, OUTPUT);
  pinMode(clutchPin1, OUTPUT);
  pinMode(clutchPin2, OUTPUT);
  pinMode(pumpPin1, OUTPUT);
  pinMode(pumpPin2, OUTPUT);
  pinMode(pumpLightPin, OUTPUT);
  
  analogWrite(reactivityPin, 0);
  digitalWrite(clutchPin1, 0);
  digitalWrite(clutchPin2, 0);
  digitalWrite(pumpPin1, 0);
  digitalWrite(pumpPin2, 0);

  // From data sheet max torque is 1600 g/cm and rotor inertia is 35 g-cm^2
  // max acceleration without a load is 1600/35 = 45.7142857143 rads/s

  // Tune Values later

  myStepper1->setSpeed(1000);
  myStepper2->setSpeed(1000);


  for (int i = 0; i < NUM_LEDS; i++) {
    if (LEDstate >= 7) {
      LEDstate = 0;
    }
    if (i > 120)
      leds[i] = CRGB(0, 0, 0);
    else
      leds[i] = CRGB(0, 0, 0);
    LEDstate++;

  }

  temp = animArray[6];
  for (int i = 6; i > 0; i--) {
    animArray[i] = animArray[i - 1];
  }
  animArray[0] = temp;


  FastLED.show();

  // clear serial buffer of any mistakenly received characters
  while (Serial.available())
    Serial.read();

}

void loop() {

  curChar = Serial.peek();
  if (curChar == 'b') {
    counter = 0;
    curChar = ' ';
    Serial.read();
    endCycle = false;
    while (endCycle == false) {
      if (Serial.available()) {
        curChar = Serial.peek();
      }
      if (curChar == 'e') {
        Serial.read();
        Serial.println("Cycle Succeeded");
        for (int i = 0; i < numPos; i++)
          numPost[i] = numIn[i];
        Serial.println(String(numPost[0]) + " " + String(numPost[1]) + " " + String(numPost[2]) + " " + String(numPost[3]) + " " + String(numPost[4]) + " " + String(numPost[5]) + " " + String(numPost[6]) + " " + String(numPost[7]));
        endCycle = true;
      }
      else if (curChar == 'b') {
        Serial.read();
        Serial.println("Cycle Failed");
        endCycle = true;
      }
      else if (curChar == ',') {
        Serial.read();
      }
      else if (isDigit(curChar) || (curChar == '-')) {
        numIn[counter] = Serial.parseInt();
        counter++;
      }
      curChar = ' ';

    }
  }


  if (steps1 < numPost[0]) {
    myStepper1->step(1, FORWARD, SINGLE);
    steps1++;
  }
  else if (steps1 > numPost[0]) {
    myStepper1->step(1, BACKWARD, SINGLE);
    steps1--;
  }

  if (steps2 > numPost[1]) {                 // change < to > to change direction
    myStepper2->step(1, FORWARD, SINGLE);
    steps2--;                                // change ++ to --
  }
  else if (steps2 < numPost[1]) {            // change > to < to change direction
    myStepper2->step(1, BACKWARD, SINGLE);
    steps2++;                                // change -- to ++
  }

  analogWrite(reactivityPin, numPost[2]);

  if (numPost[3] == 1)
    digitalWrite(clutchPin1, 1);
  else
    digitalWrite(clutchPin1, 0);

  if (numPost[4] == 1)
    digitalWrite(clutchPin2, 1);
  else
    digitalWrite(clutchPin2, 0);

  if (numPost[5] == 1)
    digitalWrite(pumpPin1, 1);
  else
    digitalWrite(pumpPin1, 0);

  if (numPost[6] == 1)
    digitalWrite(pumpPin2, 1);
  else
    digitalWrite(pumpPin2, 0);
  if (numPost[7] == 1)
    digitalWrite(pumpLightPin, 1);
  else
    digitalWrite(pumpLightPin, 0);


}
