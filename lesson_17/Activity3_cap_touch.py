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

import RPi.GPIO as GPIO, time

pads = [22,27,17]
rgb = [13,19,26]
GPIO.setmode(GPIO.BCM)
GPIO.setup(pads, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(rgb, GPIO.OUT)

try:
    while True:
        while GPIO.input(22) == True:
            GPIO.output(13, GPIO.HIGH)
        while GPIO.input(27) == True:
            GPIO.output(19, GPIO.HIGH)
        while GPIO.input(17) == True:
            GPIO.output(26, GPIO.HIGH)
        GPIO.output(rgb, GPIO.LOW)
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()