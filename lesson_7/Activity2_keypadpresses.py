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

inputs = [12,25,24,23]
outputs = [16,20,21]

GPIO.setup(inputs,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(outputs,GPIO.OUT)

r1 = ['1', '2', '3']
r2 = ['4', '5', '6']
r3 = ['7', '8', '9']
r4 = ['*', '0', '#']

def check():
    row = 0
    if GPIO.input(12) == True:
        row = r1
    elif GPIO.input(25) == True:
        row = r2
    elif GPIO.input(24) == True:
        row = r3
    elif GPIO.input(23) == True:
        row = r4
    if row != 0:
        selection = row[col]
        print('The key pressed was ' + selection)
        time.sleep(0.3)

while True:
    GPIO.output(21,GPIO.HIGH)
    col = 0
    check()
    GPIO.output(21,GPIO.LOW)
    GPIO.output(20,GPIO.HIGH)
    col = 1
    check()
    GPIO.output(20,GPIO.LOW)
    GPIO.output(16,GPIO.HIGH)
    col = 2
    check()
    GPIO.output(16,GPIO.LOW)