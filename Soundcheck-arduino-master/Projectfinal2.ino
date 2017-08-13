#include <SoftwareSerial.h>

#include <TinyGPS.h>

#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

TinyGPS gps;
SoftwareSerial ss(9, 8111);

static void smartdelay(unsigned long ms);
static void print_float(float val, float invalid, int len, int prec);
const float pi = 3.1415926;
const int ledPin =  13;      // the number of the LED pin
const int potPin = A0;
const int buzzerPin = 7;

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status

void setup()
{
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT);
  pinMode(potPin,INPUT);
  pinMode(buzzerPin,7);
  ss.begin(9600);
}

void loop()
{
  float flat, flon;
  lcd.setCursor(0, 1);
  gps.f_get_position(&flat, &flon);
  print_float(flat, TinyGPS::GPS_INVALID_F_ANGLE, 0, 6);
  print_float(flon, TinyGPS::GPS_INVALID_F_ANGLE, 1, 6);
  Serial.println();
  print_distance(flat, flon);


  Serial.println();
  
  smartdelay(1000);
}

static void smartdelay(unsigned long ms)
{
  unsigned long start = millis();
  do 
  {
    while (ss.available())
      gps.encode(ss.read());
  } while (millis() - start < ms);
}

static void print_float(float val, float invalid, int len, int prec)
{
  if (val == invalid)
  {
    while (len-- > 1)
      Serial.print('*');
    Serial.print(' ');
  }
  else
  {
    Serial.print(val, prec);
    int vi = abs((int)val);
    int flen = prec + (val < 0.0 ? 2 : 1); // . and -
    flen += vi >= 1000 ? 4 : vi >= 100 ? 3 : vi >= 10 ? 2 : 1;
    for (int i=flen; i<len; ++i)
      Serial.print(' ');
  }
  smartdelay(0);
}

void print_distance(float lati, float longi)
{
  float lat[]={ 28.363416, 28.365193,28.360683, 28.360154};
  float lon[]={75.587095, 75.590233, 75.585714, 75.589506};
  
  int mindist=2 * 6400000 *sinh(sqrt(sin((lati - lat[0]) / 2) * sin((lati - lat[0]) / 2) + cos(lati) * cos(lat[0]) * sin((longi - lon[0]) / 2) * sin((longi - lon[0]) / 2)))*pi/180; 
  for(int i=0; i<4; i++)
  {
    int dist = 2 * 6400000 * sinh(sqrt(sin((lati - lat[i]) / 2) * sin((lati - lat[i]) / 2) + cos(lati) * cos(lat[i]) * sin((longi - lon[i]) / 2) * sin((longi - lon[i]) / 2)))*pi/180;
    switch(i)
    {
      case 0:
      Serial.print("Distance from rotunda="); break;
      case 1:
      Serial.print("Distance from LTC="); break;
      case 2:
      Serial.print("Distance from SAC="); break;
      case 3:
      Serial.print("Distance from ANC="); break;
    
    }
    Serial.println(dist);
    if(dist<mindist)
    mindist=dist;
    
  }
  Serial.print("Minimun distance is = ");
  Serial.println(mindist);
  lcd.setCursor(0,0);
  lcd.print("MIN D");
  lcd.setCursor(5,0);
  lcd.print("ISTANCE-");
  lcd.setCursor(0,1);
  lcd.print((int)mindist);
  lcd.setCursor(2,1);
  lcd.print("   Metres ");
  Serial.println("---------------------------------------");

  int potValue = analogRead(potPin);
  int pressureValue = map(potValue,0,1023,0,255);
  Serial.println(potValue);
  Serial.print("Pressure Applied - ");
  Serial.println(pressureValue);

if(mindist > 250)
  {
  digitalWrite(ledPin,LOW);
  
  digitalWrite(buzzerPin,HIGH);
  
  }
  
else 
  {
    
    // turn LED off:
    digitalWrite(ledPin, HIGH);
    if (pressureValue>150)
  digitalWrite(buzzerPin,HIGH);
  if (pressureValue<150)
  digitalWrite(buzzerPin,LOW);
  }

}
  


