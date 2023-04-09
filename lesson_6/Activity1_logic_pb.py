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

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.OUT)

led = False
old_switch = False

try:
    while True:
        new_switch = GPIO.input(13)
        if new_switch == False and old_switch == False:
            led = not led
            time.sleep(0.2)
            GPIO.output(26, led)
        old_switch = new_switch
        time.sleep(0.05)

except KeyboardInterrupt:
    GPIO.cleanup()