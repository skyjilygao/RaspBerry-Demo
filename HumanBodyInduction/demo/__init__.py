import RPi.GPIO as GPIO
import time


def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.IN)
    GPIO.setup(11, GPIO.OUT)
    pass


def beep():
    while GPIO.input(12):
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "some body here!") 
        GPIO.output(11,True)
        time.sleep(0.5)
        GPIO.output(11,False)
        time.sleep(0.5)


def detct():
 #   beep()
 
   print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "  Hello sky!")
   while True:
    #for i in range(1, 1000):
        if GPIO.input(12) == True:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "  Someone is closing!")
            beep()
        else:
            GPIO.output(11,False)
            print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+" Not anybody!")
        time.sleep(2)



time.sleep(2)
init()
detct()
GPIO.cleanup()
