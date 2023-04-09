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

#!/usr/bin/python3

import RPi.GPIO as GPIO
import SimpleMFRC522
import time
import csv

reader = SimpleMFRC522.SimpleMFRC522()

with open('access_list.txt', 'r') as data:
    values = list(csv.reader(data))

try:
    while True:
        id, text = reader.read()
        text = text.strip()
        for search in values:
            if text in search:
                user = search[1]
                status = search[2]
                break
            else:
                user = 'Unknown'
                status = 'deny'
        if status == 'allow':
            print('ACCESS GRANTED')
        if status == 'deny':
            print('ACCESS DENIED')
        time.sleep(.3)

except KeyboardInterrupt:
    GPIO.cleanup()