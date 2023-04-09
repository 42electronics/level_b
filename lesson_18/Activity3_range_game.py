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

import time, RPi.GPIO as GPIO, random, ultrasonic, Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont

slide = 16
rgb = [13,19,26]
red = 13
green = 19
blue = 26
cap = [22,27,17,4]
cap1 = 22
cap2 = 27
cap3 = 17
cap4 = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(slide, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(rgb, GPIO.OUT)
GPIO.setup(cap, GPIO.IN)

disp = Adafruit_SSD1306.SSD1306_128_64(rst=None)
disp.begin()
width = disp.width
height = disp.height
image = Image.new('1', (width, height)) # '1' converts image to 1-bit color
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf',18)

def update_display():
	disp.image(image)
	disp.display()

try:
	while True:
		for skill_selection in range(0,20):
			if GPIO.input(slide) == False:
				draw.rectangle((0,0,width,height), outline=0, fill = 0)
				draw.text((0, 0), "Difficulty?", font=font, fill=255)
				draw.text((0, 22), "Easy", font=font, fill=255)
				update_display()
				skill = 2
			else:
				draw.rectangle((0,0,width,height), outline=0, fill = 0)
				draw.text((0, 0), "Difficulty?", font=font, fill=255)
				draw.text((0, 22), "Hard", font=font, fill=255)
				update_display()
				skill = 1
			time.sleep(.1)

		target = random.randint(20,100)

		draw.rectangle((0,0,width,height), outline=0, fill=0)
		draw.text((0, 0), "Target = %s" %target, font=font, fill=255)
		draw.text((0, 22), "Press pad", font=font, fill=255)
		draw.text((0, 44), "to start", font=font, fill=255)
		update_display()


		while GPIO.input(cap1)==GPIO.input(cap2)==GPIO.input(cap3)==GPIO.input(cap4)==False:
			time.sleep(.05)

		if GPIO.input(cap1) == True:
			delay = 1
		if GPIO.input(cap2) == True:
			delay = 2
		if GPIO.input(cap3) == True:
			delay = 3
		if GPIO.input(cap4) == True:
			delay = 4

		draw.rectangle((0,0,width,height), outline=0, fill=0)
		draw.text((0, 0), "Target = %s" %target, font=font, fill=255)
		draw.text((0, 22), "Capturing range", font=font, fill=255)
		if delay == 1:
			draw.text((0, 44), "in %i second" %delay, font=font, fill=255)
		else:
			draw.text((0, 44), "in %i seconds" %delay, font=font, fill=255)
		update_display()
		time.sleep(delay)

		distance = ultrasonic.average()
		diff = abs(target-distance)
		window = 10 * skill

		if diff <= window:
			GPIO.output(green, GPIO.HIGH)
		else:
			GPIO.output(red, GPIO.HIGH)

		draw.rectangle((0,0,width,height), outline=0, fill=0)
		draw.text((0, 0), "Target = %s" %target, font=font, fill=255)
		draw.text((0, 22), "Player = %.0f" %distance, font=font, fill=255)
		draw.text((0,44), "Diff = %.0f" %diff, font=font, fill=255)
		update_display()
		time.sleep(5)
		GPIO.output(rgb, GPIO.LOW)

except KeyboardInterrupt:
	disp.clear()
	disp.display()
	GPIO.cleanup()