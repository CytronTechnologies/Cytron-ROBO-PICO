/*
DESCRIPTION:
This example code will uses: Robo Pico and Raspberry Pi Pico / Pico W
to display text on the OLED Display SSD1315 using Arduino.

CONNECTION:
Robo Pico : OLED Display
Grove 1   - Oled Grove
GP0       - SDA
GP1       - SCL

AUTHOR  : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

REFERENCE:
Code adapted from:
https://wiki.seeedstudio.com/Grove-OLED-Display-0.96-SSD1315/
*/
#include <Arduino.h>
#include <U8g2lib.h>

#ifdef U8X8_HAVE_HW_SPI
#include <SPI.h>
#endif
#ifdef U8X8_HAVE_HW_I2C
#include <Wire.h>
#endif

U8G2_SSD1306_128X64_NONAME_F_SW_I2C u8g2(U8G2_R0, /* clock=*/ 1, /* data=*/ 0, /* reset=*/ U8X8_PIN_NONE);    //Low speed I2C

void setup(void) {
  u8g2.begin();
}

void loop(void) {
  u8g2.clearBuffer();                   // clear the internal memory
  u8g2.setFont(u8g2_font_ncenB08_tr);   // choose a suitable font
  u8g2.drawStr(0,10,"Hello World!");    // write something to the internal memory
  u8g2.drawStr(0,25,"Yeah!");
  u8g2.sendBuffer();                    // transfer internal memory to the display
  delay(1000);  
}