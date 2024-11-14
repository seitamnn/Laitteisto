from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C

sw0 = Pin(9, Pin.IN, Pin.PULL_UP)
sw1 = Pin(8, Pin.IN, Pin.PULL_UP)
sw2 = Pin(7, Pin.IN, Pin.PULL_UP)
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

y_axis = 30
x_axis = 0

oled.fill(0)

while True:
    oled.pixel(x_axis, y_axis, 1)
    x_axis = x_axis + 1
    print(y_axis)
    oled.show()
    
    #alotetaan alusta ku päästään oikeesee reunaan
    if x_axis >= 128:
        x_axis = 0
        
    # nappuloita painellaan jeejee    
    if sw0() == 0:
        if y_axis > 0:
            y_axis = y_axis -1
    elif sw2() == 0:
        if y_axis  < 63:
            y_axis = y_axis +1
    elif sw1() == 0:
        oled.fill(0)
        x_axis = 0
        y_axis = 30