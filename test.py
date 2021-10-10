import time 
import RPi.GPIO as GPIO

# Seta o tipo de pinagem (BOARD OU BCM)
GPIO.setmode(GPIO.BCM) 

led = 4
 
GPIO.setup(led,GPIO.OUT)
x=0 

while x<=10:

	print("LED ligado")  
	GPIO.output(led,GPIO.HIGH)

	time.sleep(1)   

	print("LED Desligado")   
	GPIO.output(led,GPIO.LOW)

	time.sleep(1)
	x += 1
