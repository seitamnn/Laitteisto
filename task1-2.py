import time
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C

button = Pin(9, Pin.IN, Pin.PULL_UP)
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

y_axis = 0

while True:
    user_input = input('Write: ')
    oled.text(user_input, 0, y_axis, 1)
    oled.show()
    y_axis = y_axis + 8
