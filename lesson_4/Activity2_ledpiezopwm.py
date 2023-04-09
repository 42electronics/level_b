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

import time, RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

pwm_26 = GPIO.PWM(26, 50)   #assigns PWM signal to pin 26 at 20Hz
pwm_26.start(10)             #starts PWM on pin 26 at 10% duty cycle
time.sleep(2)               #program sleeps for 2 seconds
pwm_26.stop()               #stops PWM output on pin 26

pwm_19 = GPIO.PWM(19, 300)  #assigns PWM signal to pin 19 at 300Hz
pwm_19.start(50)            #starts pin 19 at 50% duty cycle
time.sleep(0.5)             #program sleeps for 0.5 seconds
pwm_19.stop()               #stops PWM output on pin 19

GPIO.cleanup()