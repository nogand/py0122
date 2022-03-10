# CircuitPlaygroundExpress_NeoPixel

import board
from digitalio import DigitalInOut, Direction
from adafruit_circuitplayground.express import cpx
import time

RED = (255, 0, 0)
YELLOW = (200, 150, 25)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
BLACK = (0, 0, 0)

TREN = 3
TIEMPO_ON = 0.1
TIEMPO_OFF = 0.001
COLOR = GREEN
HUMM = False

pixels = cpx.pixels
pixels.brightness=0.2

i = 0

while True:
    if i+TREN > 10 :
        pixels[i:] = [ COLOR ] * (10 - i)
        pixels[:TREN-(10 - i)] = [ COLOR ] * (TREN - (10 - i))
    else :
        pixels[i:i+TREN] = [ COLOR ] * TREN
    pixels.show()
    time.sleep(TIEMPO_ON)
    pixels[0:10] = [ BLACK ] * 10
    time.sleep(TIEMPO_OFF)
    i+=1
    if i == 10 :
        i = 0
    if cpx.touch_A1 or cpx.touch_A2 or cpx.touch_A3 or cpx.touch_A4 or cpx.touch_A5 or cpx.touch_A6 or cpx.touch_A7:
        COLOR = RED
        cpx.start_tone(540)
    else :
        COLOR = GREEN
        cpx.stop_tone()