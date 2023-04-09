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

import bme280
import RPi.GPIO as GPIO
import time

red = 13
green = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

try:
	while True:
		temperature,pressure,humidity = bme280.readBME280All()
		temperature = (temperature * 9/5) + 32
		print('Temp= %.2f' %temperature)

		if temperature >= 80:
			GPIO.output(green, GPIO.LOW)
			GPIO.output(red, GPIO.HIGH)
		else:
			GPIO.output(green, GPIO.HIGH)
			GPIO.output(red, GPIO.LOW)
		time.sleep(.3)

except KeyboardInterrupt:
	GPIO.cleanup()
	SystemExit()