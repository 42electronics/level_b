#Copyright (c) 2023 42 Development dba 42 Electronics
#Author: Eric Feickert
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of
#this software and associated documentation files (the "Software"), to deal in the
#Software without restriction, including without limitation the rights to use,
#copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the
#Software, and to permit persons to whom the Software is furnished to do so,
#subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
#INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
#PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
#OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import RPi.GPIO as GPIO
import time

rgb = [13,19,26]
red = 13
green = 19
blue = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(rgb, GPIO.OUT)
GPIO.setup(21, GPIO.IN)

try:
    while True:
        if GPIO.input(21) == False:
            GPIO.output(green, GPIO.LOW)
            GPIO.output(red, GPIO.HIGH)
        else:
            GPIO.output(red, GPIO.LOW)
            GPIO.output(green, GPIO.HIGH)
        time.sleep(.1)
        
except KeyboardInterrupt:
    GPIO.cleanup()