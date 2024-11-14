import time
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C

sw0 = Pin(9, Pin.IN, Pin.PULL_UP)
sw2 = Pin(7, Pin.IN, Pin.PULL_UP)
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

oled.fill(0)
#oled.text('<=>', 0, 50, 1)
#oled.show()

char_width = 8
char_height = 8
ufo = '<=>'
size_ufo = len(ufo)*char_width

x_axis = 50

oled.text(ufo, x_axis, 50, 1)
oled.show()

while True:
    oled.fill(0)
    oled.text(ufo, x_axis, 50, 1)
    oled.show()
    if sw0() == 0:
        x_axis = x_axis - size_ufo
        if x_axis <= 0:
            x_axis = 0
        #print('vasemmalle')
    if sw2() == 0:
        x_axis = x_axis + 3
        if x_axis >= 100:
            x_axis = 100
        #print('oikeelle')
    oled.text(ufo, x_axis, 50, 1)
    oled.show()