from machine import Pin, I2C
from fifo import Fifo
import time
from filefifo import Filefifo
from ssd1306 import SSD1306_I2C

# data from the file
file = Filefifo(10, name = 'capture_250Hz_03.txt')
data = []
for i in range(1000):
    data.append(file.get())
#print(data)
minvalue = min(data)
maxvalue = max(data)
#print(minvalue)
#print(maxvalue)    

# oled screen
screen_width = 128
screen_height = 64
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
screen = SSD1306_I2C(screen_width, screen_height, i2c)
    
#print(minvalue)
#print(maxvalue)
#print(data)
    
class Encoder:
    def __init__(self, rot_a, rot_b):
        self.a = Pin(rot_a, mode = Pin.IN, pull = Pin.PULL_UP)
        self.b = Pin(rot_b, mode = Pin.IN, pull = Pin.PULL_UP)
        self.fifo = Fifo(30, typecode = 'i')
        self.a.irq(handler = self.handler, trigger = Pin.IRQ_RISING, hard = True)
        
    def handler(self, pin):
        if self.b():
            self.fifo.put(-2)
        else:
            self.fifo.put(2)
            
            
rot = Encoder(10, 11)
            
class Screencontroller:
    def __init__(self):
        self.x = 0
        self.lines = []
        
        self.convert_lines(data)
        
    def convert_lines(self, array):
        for item in array:
            self.lines.append(int((item - minvalue) / (maxvalue - minvalue) * 64)) #screen height 64
            
    def draw_screen(self):
        screen.fill(0)
        for i in range(0, 127):
            screen.pixel(i, self.lines[i + self.x], 1)
        
    def update_screen(self):
        self.draw_screen()
        screen.show()
        
    def scroll_screen(self, amount):
        # set previous and current X cordinates
        prev = self.x
        self.x -= amount
        if self.x < 0: 
            self.x = 0
            return # ends scrolling at the edge of screen
        elif self.x >= len(self.lines) - 127:
            self.x = len(self.lines) - 128
  
line = Screencontroller()
line.draw_screen()

while True:
    line.update_screen()
    while rot.fifo.has_data():
        line.scroll_screen(-rot.fifo.get())