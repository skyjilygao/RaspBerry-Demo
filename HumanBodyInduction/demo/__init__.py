pi@raspberrypi:~ $ cat 66.py 
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
pi@raspberrypi:~ $ sudo python3
Python 3.7.3 (default, Jul 25 2020, 13:03:44) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import time
>>> print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "  Hello sky!")
2021-02-05 14:20:58  Hello sky!
>>> print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "  Someone is closing!")
2021-02-05 14:21:10  Someone is closing!
>>> print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+" Not anybody!")
2021-02-05 14:21:16 Not anybody!
>>> exit()
pi@raspberrypi:~ $ sudo python3 66.py 
  File "66.py", line 32
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+" Not anybody!")
                                                                                        ^
IndentationError: unindent does not match any outer indentation level
pi@raspberrypi:~ $ vi 66.py 
pi@raspberrypi:~ $ sudo python3 66.py 
2021-02-05 14:21:47  Hello sky!
2021-02-05 14:21:47  Someone is closing!
^[2021-02-05 14:23:08 Not anybody!
2021-02-05 14:23:10  Someone is closing!
2021-02-05 14:25:10 Not anybody!
2021-02-05 14:25:12 Not anybody!
2021-02-05 14:25:14 Not anybody!
2021-02-05 14:25:16 Not anybody!
2021-02-05 14:25:18 Not anybody!
2021-02-05 14:25:20 Not anybody!
2021-02-05 14:25:22 Not anybody!
2021-02-05 14:25:24 Not anybody!
2021-02-05 14:25:26 Not anybody!
2021-02-05 14:25:28 Not anybody!
2021-02-05 14:25:30 Not anybody!
2021-02-05 14:25:32 Not anybody!
2021-02-05 14:25:34 Not anybody!
2021-02-05 14:25:36 Not anybody!
2021-02-05 14:25:38 Not anybody!
2021-02-05 14:25:40 Not anybody!
2021-02-05 14:25:42 Not anybody!
2021-02-05 14:25:44 Not anybody!
2021-02-05 14:25:46 Not anybody!
2021-02-05 14:25:48 Not anybody!
2021-02-05 14:25:50 Not anybody!
2021-02-05 14:25:52  Someone is closing!
Traceback (most recent call last):
  File "66.py", line 39, in <module>
    detct()
  File "66.py", line 29, in detct
    beep()
  File "66.py", line 16, in beep
    time.sleep(0.5)
KeyboardInterrupt
^Cpi@raspberrypi:~ $ vi 66.py 
pi@raspberrypi:~ $ sudo python3 66.py 
2021-02-05 14:28:39  Hello sky!
2021-02-05 14:28:39  Someone is closing!
2021-02-05 14:28:39some body here!
2021-02-05 14:28:40some body here!
2021-02-05 14:28:41some body here!
2021-02-05 14:28:42some body here!
2021-02-05 14:28:43some body here!
2021-02-05 14:28:44some body here!
2021-02-05 14:28:45some body here!
2021-02-05 14:28:46some body here!
2021-02-05 14:28:47some body here!
2021-02-05 14:28:48some body here!
2021-02-05 14:28:49some body here!
2021-02-05 14:28:50some body here!
2021-02-05 14:28:51some body here!
2021-02-05 14:28:52some body here!
2021-02-05 14:28:53some body here!
2021-02-05 14:28:54some body here!
2021-02-05 14:28:55some body here!
2021-02-05 14:28:56some body here!
2021-02-05 14:28:57some body here!
2021-02-05 14:28:58some body here!
2021-02-05 14:28:59some body here!
2021-02-05 14:29:00some body here!
2021-02-05 14:29:01some body here!
2021-02-05 14:29:02some body here!
2021-02-05 14:29:03some body here!
2021-02-05 14:29:04some body here!
2021-02-05 14:29:05some body here!
2021-02-05 14:29:06some body here!
2021-02-05 14:29:07some body here!
2021-02-05 14:29:08some body here!
2021-02-05 14:29:09some body here!
2021-02-05 14:29:10some body here!
2021-02-05 14:29:11some body here!
2021-02-05 14:29:12some body here!
2021-02-05 14:29:13some body here!
2021-02-05 14:29:14some body here!
2021-02-05 14:29:15some body here!
2021-02-05 14:29:16some body here!
2021-02-05 14:29:17some body here!
2021-02-05 14:29:18some body here!
2021-02-05 14:29:19some body here!
2021-02-05 14:29:20some body here!
2021-02-05 14:29:21some body here!
2021-02-05 14:29:22some body here!
2021-02-05 14:29:23some body here!
2021-02-05 14:29:24some body here!
2021-02-05 14:29:25some body here!
2021-02-05 14:29:26some body here!
2021-02-05 14:29:27some body here!
2021-02-05 14:29:28some body here!
2021-02-05 14:29:29some body here!
2021-02-05 14:29:30some body here!
2021-02-05 14:29:31some body here!
2021-02-05 14:29:32some body here!
2021-02-05 14:29:33some body here!
2021-02-05 14:29:34some body here!
2021-02-05 14:29:35some body here!
2021-02-05 14:29:36some body here!
2021-02-05 14:29:37some body here!
2021-02-05 14:29:38some body here!
2021-02-05 14:29:39some body here!
2021-02-05 14:29:40some body here!
2021-02-05 14:29:41some body here!
2021-02-05 14:29:42some body here!
2021-02-05 14:29:43some body here!
2021-02-05 14:29:44some body here!
2021-02-05 14:29:45some body here!
2021-02-05 14:29:46some body here!
2021-02-05 14:29:47some body here!
2021-02-05 14:29:48some body here!
2021-02-05 14:29:49some body here!
2021-02-05 14:29:50some body here!
2021-02-05 14:29:51some body here!
2021-02-05 14:29:52some body here!
2021-02-05 14:29:55 Not anybody!
2021-02-05 14:29:57 Not anybody!
2021-02-05 14:29:59 Not anybody!
2021-02-05 14:30:01  Someone is closing!
2021-02-05 14:30:01some body here!
2021-02-05 14:30:02some body here!
2021-02-05 14:30:03some body here!
2021-02-05 14:30:04some body here!
2021-02-05 14:30:05some body here!
2021-02-05 14:30:06some body here!
2021-02-05 14:30:07some body here!
2021-02-05 14:30:08some body here!
2021-02-05 14:30:09some body here!
2021-02-05 14:30:10some body here!
2021-02-05 14:30:11some body here!
2021-02-05 14:30:12some body here!
2021-02-05 14:30:13some body here!
2021-02-05 14:30:14some body here!
2021-02-05 14:30:15some body here!
2021-02-05 14:30:16some body here!
2021-02-05 14:30:17some body here!
2021-02-05 14:30:18some body here!
2021-02-05 14:30:19some body here!
2021-02-05 14:30:20some body here!
2021-02-05 14:30:21some body here!
2021-02-05 14:30:23some body here!
2021-02-05 14:30:24some body here!
2021-02-05 14:30:25some body here!
2021-02-05 14:30:26some body here!
2021-02-05 14:30:27some body here!
2021-02-05 14:30:28some body here!
2021-02-05 14:30:29some body here!
2021-02-05 14:30:30some body here!
2021-02-05 14:30:31some body here!
2021-02-05 14:30:32some body here!
2021-02-05 14:30:33some body here!
2021-02-05 14:30:34some body here!
2021-02-05 14:30:35some body here!
2021-02-05 14:30:36some body here!
2021-02-05 14:30:37some body here!
2021-02-05 14:30:38some body here!
2021-02-05 14:30:39some body here!
2021-02-05 14:30:40some body here!
2021-02-05 14:30:41some body here!
2021-02-05 14:30:42some body here!
2021-02-05 14:30:43some body here!
2021-02-05 14:30:44some body here!
2021-02-05 14:30:45some body here!
2021-02-05 14:30:46some body here!
2021-02-05 14:30:47some body here!
2021-02-05 14:30:48some body here!
2021-02-05 14:30:49some body here!
2021-02-05 14:30:50some body here!
2021-02-05 14:30:51some body here!
2021-02-05 14:30:52some body here!
2021-02-05 14:30:53some body here!
2021-02-05 14:30:54some body here!
2021-02-05 14:30:55some body here!
2021-02-05 14:30:56some body here!
2021-02-05 14:30:57some body here!
2021-02-05 14:30:58some body here!
2021-02-05 14:30:59some body here!
2021-02-05 14:31:00some body here!
2021-02-05 14:31:01some body here!
2021-02-05 14:31:02some body here!
2021-02-05 14:31:03some body here!
2021-02-05 14:31:04some body here!
2021-02-05 14:31:05some body here!
2021-02-05 14:31:06some body here!
2021-02-05 14:31:07some body here!
2021-02-05 14:31:08some body here!
2021-02-05 14:31:09some body here!
2021-02-05 14:31:10some body here!
2021-02-05 14:31:11some body here!
2021-02-05 14:31:12some body here!
2021-02-05 14:31:13some body here!
2021-02-05 14:31:14some body here!
2021-02-05 14:31:15some body here!
2021-02-05 14:31:16some body here!
2021-02-05 14:31:17some body here!
2021-02-05 14:31:18some body here!
2021-02-05 14:31:19some body here!
2021-02-05 14:31:20some body here!
2021-02-05 14:31:21some body here!
2021-02-05 14:31:22some body here!
2021-02-05 14:31:23some body here!
2021-02-05 14:31:24some body here!
2021-02-05 14:31:25some body here!
2021-02-05 14:31:26some body here!
2021-02-05 14:31:27some body here!
2021-02-05 14:31:28some body here!
2021-02-05 14:31:29some body here!
2021-02-05 14:31:30some body here!
2021-02-05 14:31:31some body here!
2021-02-05 14:31:32some body here!
2021-02-05 14:31:33some body here!
2021-02-05 14:31:34some body here!
2021-02-05 14:31:35some body here!
2021-02-05 14:31:36some body here!
2021-02-05 14:31:37some body here!
2021-02-05 14:31:38some body here!
2021-02-05 14:31:39some body here!
2021-02-05 14:31:40some body here!
2021-02-05 14:31:41some body here!
2021-02-05 14:31:42some body here!
2021-02-05 14:31:43some body here!
2021-02-05 14:31:44some body here!
2021-02-05 14:31:45some body here!
2021-02-05 14:31:46some body here!
2021-02-05 14:31:47some body here!
2021-02-05 14:31:48some body here!
2021-02-05 14:31:49some body here!
2021-02-05 14:31:50some body here!
2021-02-05 14:31:51some body here!
2021-02-05 14:31:52some body here!
2021-02-05 14:31:53some body here!
2021-02-05 14:31:54some body here!
2021-02-05 14:31:55some body here!
2021-02-05 14:31:56some body here!
2021-02-05 14:31:57some body here!
2021-02-05 14:31:58some body here!
2021-02-05 14:31:59some body here!
2021-02-05 14:32:02 Not anybody!
2021-02-05 14:32:04 Not anybody!
2021-02-05 14:32:06 Not anybody!
2021-02-05 14:32:08 Not anybody!
2021-02-05 14:32:10 Not anybody!
2021-02-05 14:32:12 Not anybody!
2021-02-05 14:32:14 Not anybody!
2021-02-05 14:32:16 Not anybody!
2021-02-05 14:32:18 Not anybody!
2021-02-05 14:32:20 Not anybody!
2021-02-05 14:32:22 Not anybody!
2021-02-05 14:32:24 Not anybody!
2021-02-05 14:32:26 Not anybody!
2021-02-05 14:32:28 Not anybody!
2021-02-05 14:32:30 Not anybody!
2021-02-05 14:32:32 Not anybody!
2021-02-05 14:32:34 Not anybody!
2021-02-05 14:32:36 Not anybody!
2021-02-05 14:32:38 Not anybody!
2021-02-05 14:32:40 Not anybody!
2021-02-05 14:32:42 Not anybody!
2021-02-05 14:32:44 Not anybody!
2021-02-05 14:32:46 Not anybody!
2021-02-05 14:32:48 Not anybody!
2021-02-05 14:32:50 Not anybody!
2021-02-05 14:32:52 Not anybody!
2021-02-05 14:32:54 Not anybody!
2021-02-05 14:32:56 Not anybody!
2021-02-05 14:32:58 Not anybody!
2021-02-05 14:33:00 Not anybody!
2021-02-05 14:33:02 Not anybody!
2021-02-05 14:33:04 Not anybody!
2021-02-05 14:33:06 Not anybody!
2021-02-05 14:33:08 Not anybody!
2021-02-05 14:33:10 Not anybody!
2021-02-05 14:33:12 Not anybody!
2021-02-05 14:33:14 Not anybody!
2021-02-05 14:33:16 Not anybody!
2021-02-05 14:33:18 Not anybody!
2021-02-05 14:33:20 Not anybody!
2021-02-05 14:33:22 Not anybody!
2021-02-05 14:33:24 Not anybody!
2021-02-05 14:33:26 Not anybody!
2021-02-05 14:33:28 Not anybody!
2021-02-05 14:33:30 Not anybody!
2021-02-05 14:33:32 Not anybody!
2021-02-05 14:33:34 Not anybody!
2021-02-05 14:33:36 Not anybody!
2021-02-05 14:33:38 Not anybody!
2021-02-05 14:33:40 Not anybody!
2021-02-05 14:33:42 Not anybody!
2021-02-05 14:33:44 Not anybody!
2021-02-05 14:33:46 Not anybody!
2021-02-05 14:33:48 Not anybody!
2021-02-05 14:33:50 Not anybody!
2021-02-05 14:33:52 Not anybody!
2021-02-05 14:33:54 Not anybody!
2021-02-05 14:33:56 Not anybody!
2021-02-05 14:33:58 Not anybody!
2021-02-05 14:34:00 Not anybody!
2021-02-05 14:34:02 Not anybody!
2021-02-05 14:34:04 Not anybody!
2021-02-05 14:34:06 Not anybody!
2021-02-05 14:34:08 Not anybody!
2021-02-05 14:34:10 Not anybody!
2021-02-05 14:34:12 Not anybody!
2021-02-05 14:34:14 Not anybody!
2021-02-05 14:34:16 Not anybody!
2021-02-05 14:34:18 Not anybody!
2021-02-05 14:34:20 Not anybody!
2021-02-05 14:34:22 Not anybody!
2021-02-05 14:34:24 Not anybody!
2021-02-05 14:34:26 Not anybody!
2021-02-05 14:34:28 Not anybody!
2021-02-05 14:34:30 Not anybody!
2021-02-05 14:34:32 Not anybody!
2021-02-05 14:34:34 Not anybody!
2021-02-05 14:34:36 Not anybody!
2021-02-05 14:34:38 Not anybody!
2021-02-05 14:34:40 Not anybody!
2021-02-05 14:34:42 Not anybody!
2021-02-05 14:34:44 Not anybody!
2021-02-05 14:34:46 Not anybody!
2021-02-05 14:34:48 Not anybody!
2021-02-05 14:34:50 Not anybody!
2021-02-05 14:34:52 Not anybody!
2021-02-05 14:34:54 Not anybody!
2021-02-05 14:34:56 Not anybody!
2021-02-05 14:34:58 Not anybody!
2021-02-05 14:35:00 Not anybody!
2021-02-05 14:35:02 Not anybody!
2021-02-05 14:35:04 Not anybody!
2021-02-05 14:35:06 Not anybody!
2021-02-05 14:35:08 Not anybody!
2021-02-05 14:35:10 Not anybody!
2021-02-05 14:35:12 Not anybody!
2021-02-05 14:35:14 Not anybody!
2021-02-05 14:35:16 Not anybody!
2021-02-05 14:35:18 Not anybody!
2021-02-05 14:35:20 Not anybody!
2021-02-05 14:35:22 Not anybody!
2021-02-05 14:35:24 Not anybody!
2021-02-05 14:35:26 Not anybody!
2021-02-05 14:35:28 Not anybody!
2021-02-05 14:35:30 Not anybody!
2021-02-05 14:35:32 Not anybody!
2021-02-05 14:35:34 Not anybody!
2021-02-05 14:35:36 Not anybody!
2021-02-05 14:35:38 Not anybody!
2021-02-05 14:35:40 Not anybody!
2021-02-05 14:35:42 Not anybody!
2021-02-05 14:35:44 Not anybody!
2021-02-05 14:35:46 Not anybody!
2021-02-05 14:35:48 Not anybody!
2021-02-05 14:35:50 Not anybody!
2021-02-05 14:35:52 Not anybody!
2021-02-05 14:35:54 Not anybody!
2021-02-05 14:35:56 Not anybody!
2021-02-05 14:35:58 Not anybody!
2021-02-05 14:36:00 Not anybody!
2021-02-05 14:36:02 Not anybody!
2021-02-05 14:36:04 Not anybody!
2021-02-05 14:36:06 Not anybody!
2021-02-05 14:36:08 Not anybody!
2021-02-05 14:36:10 Not anybody!
2021-02-05 14:36:12 Not anybody!
2021-02-05 14:36:14 Not anybody!
2021-02-05 14:36:16 Not anybody!
2021-02-05 14:36:18 Not anybody!
2021-02-05 14:36:20 Not anybody!
2021-02-05 14:36:22 Not anybody!
2021-02-05 14:36:24 Not anybody!
2021-02-05 14:36:26 Not anybody!
2021-02-05 14:36:28 Not anybody!
2021-02-05 14:36:30 Not anybody!
2021-02-05 14:36:32 Not anybody!
2021-02-05 14:36:34 Not anybody!
2021-02-05 14:36:36 Not anybody!
2021-02-05 14:36:38 Not anybody!
2021-02-05 14:36:40 Not anybody!
2021-02-05 14:36:42 Not anybody!
2021-02-05 14:36:44 Not anybody!
2021-02-05 14:36:46 Not anybody!
2021-02-05 14:36:48 Not anybody!
2021-02-05 14:36:50 Not anybody!
2021-02-05 14:36:52 Not anybody!
2021-02-05 14:36:54 Not anybody!
2021-02-05 14:36:56 Not anybody!
2021-02-05 14:36:58 Not anybody!
2021-02-05 14:37:00 Not anybody!
2021-02-05 14:37:02 Not anybody!
2021-02-05 14:37:04 Not anybody!
2021-02-05 14:37:06 Not anybody!
2021-02-05 14:37:08 Not anybody!
2021-02-05 14:37:10 Not anybody!
2021-02-05 14:37:12 Not anybody!
2021-02-05 14:37:14 Not anybody!
2021-02-05 14:37:16 Not anybody!
2021-02-05 14:37:18 Not anybody!
2021-02-05 14:37:20 Not anybody!
2021-02-05 14:37:22 Not anybody!
2021-02-05 14:37:24 Not anybody!
2021-02-05 14:37:26 Not anybody!
2021-02-05 14:37:28 Not anybody!
2021-02-05 14:37:30 Not anybody!
2021-02-05 14:37:32 Not anybody!
2021-02-05 14:37:34 Not anybody!
2021-02-05 14:37:36 Not anybody!
2021-02-05 14:37:38 Not anybody!
2021-02-05 14:37:40 Not anybody!
2021-02-05 14:37:42 Not anybody!
2021-02-05 14:37:44 Not anybody!
2021-02-05 14:37:46 Not anybody!
2021-02-05 14:37:48 Not anybody!
2021-02-05 14:37:50 Not anybody!
2021-02-05 14:37:52 Not anybody!
2021-02-05 14:37:54 Not anybody!
2021-02-05 14:37:56 Not anybody!
2021-02-05 14:37:58 Not anybody!
2021-02-05 14:38:00 Not anybody!
2021-02-05 14:38:02 Not anybody!
2021-02-05 14:38:04 Not anybody!
2021-02-05 14:38:06 Not anybody!
2021-02-05 14:38:08 Not anybody!
2021-02-05 14:38:10 Not anybody!
2021-02-05 14:38:12 Not anybody!
2021-02-05 14:38:14 Not anybody!
2021-02-05 14:38:16 Not anybody!
2021-02-05 14:38:18 Not anybody!
2021-02-05 14:38:20 Not anybody!
2021-02-05 14:38:22 Not anybody!
2021-02-05 14:38:24 Not anybody!
2021-02-05 14:38:26 Not anybody!
2021-02-05 14:38:28 Not anybody!
2021-02-05 14:38:30 Not anybody!
2021-02-05 14:38:32 Not anybody!
2021-02-05 14:38:34 Not anybody!
2021-02-05 14:38:36 Not anybody!
2021-02-05 14:38:38 Not anybody!
2021-02-05 14:38:40 Not anybody!
2021-02-05 14:38:42 Not anybody!
2021-02-05 14:38:44 Not anybody!
2021-02-05 14:38:46 Not anybody!
2021-02-05 14:38:48 Not anybody!
2021-02-05 14:38:50 Not anybody!
2021-02-05 14:38:52 Not anybody!
2021-02-05 14:38:54 Not anybody!
2021-02-05 14:38:56 Not anybody!
2021-02-05 14:38:58 Not anybody!
2021-02-05 14:39:00 Not anybody!
2021-02-05 14:39:02 Not anybody!
2021-02-05 14:39:04 Not anybody!
2021-02-05 14:39:06 Not anybody!
2021-02-05 14:39:08  Someone is closing!
2021-02-05 14:39:08some body here!
2021-02-05 14:39:09some body here!
2021-02-05 14:39:10some body here!
2021-02-05 14:39:11some body here!
2021-02-05 14:39:12some body here!
2021-02-05 14:39:13some body here!
2021-02-05 14:39:14some body here!
2021-02-05 14:39:15some body here!
2021-02-05 14:39:16some body here!
2021-02-05 14:39:17some body here!
2021-02-05 14:39:18some body here!
2021-02-05 14:39:19some body here!
2021-02-05 14:39:20some body here!
2021-02-05 14:39:21some body here!
2021-02-05 14:39:22some body here!
2021-02-05 14:39:23some body here!
2021-02-05 14:39:24some body here!
2021-02-05 14:39:25some body here!
2021-02-05 14:39:26some body here!
2021-02-05 14:39:27some body here!
2021-02-05 14:39:28some body here!
2021-02-05 14:39:29some body here!
2021-02-05 14:39:30some body here!
2021-02-05 14:39:31some body here!
2021-02-05 14:39:32some body here!
2021-02-05 14:39:33some body here!
2021-02-05 14:39:34some body here!
2021-02-05 14:39:35some body here!
2021-02-05 14:39:36some body here!
2021-02-05 14:39:37some body here!
2021-02-05 14:39:38some body here!
2021-02-05 14:39:39some body here!
2021-02-05 14:39:40some body here!
2021-02-05 14:39:41some body here!
2021-02-05 14:39:42some body here!
2021-02-05 14:39:43some body here!
2021-02-05 14:39:44some body here!
2021-02-05 14:39:45some body here!
2021-02-05 14:39:46some body here!
2021-02-05 14:39:47some body here!
2021-02-05 14:39:48some body here!
2021-02-05 14:39:49some body here!
2021-02-05 14:39:50some body here!
2021-02-05 14:39:51some body here!
2021-02-05 14:39:52some body here!
2021-02-05 14:39:53some body here!
2021-02-05 14:39:54some body here!
2021-02-05 14:39:55some body here!
2021-02-05 14:39:56some body here!
2021-02-05 14:39:57some body here!
2021-02-05 14:39:58some body here!
2021-02-05 14:39:59some body here!
2021-02-05 14:40:00some body here!
2021-02-05 14:40:01some body here!
2021-02-05 14:40:02some body here!
2021-02-05 14:40:03some body here!
2021-02-05 14:40:04some body here!
2021-02-05 14:40:05some body here!
2021-02-05 14:40:06some body here!
2021-02-05 14:40:07some body here!
2021-02-05 14:40:08some body here!
2021-02-05 14:40:09some body here!
2021-02-05 14:40:10some body here!
2021-02-05 14:40:11some body here!
2021-02-05 14:40:12some body here!
2021-02-05 14:40:13some body here!
2021-02-05 14:40:14some body here!
2021-02-05 14:40:15some body here!
2021-02-05 14:40:16some body here!
2021-02-05 14:40:17some body here!
2021-02-05 14:40:18some body here!
2021-02-05 14:40:19some body here!
2021-02-05 14:40:20some body here!
2021-02-05 14:40:21some body here!
2021-02-05 14:40:22some body here!
2021-02-05 14:40:23some body here!
2021-02-05 14:40:24some body here!
2021-02-05 14:40:25some body here!
2021-02-05 14:40:26some body here!
2021-02-05 14:40:27some body here!
2021-02-05 14:40:28some body here!
2021-02-05 14:40:29some body here!
2021-02-05 14:40:30some body here!
2021-02-05 14:40:31some body here!
2021-02-05 14:40:32some body here!
2021-02-05 14:40:33some body here!
2021-02-05 14:40:34some body here!
2021-02-05 14:40:35some body here!
2021-02-05 14:40:36some body here!
2021-02-05 14:40:37some body here!
2021-02-05 14:40:38some body here!
2021-02-05 14:40:39some body here!
2021-02-05 14:40:40some body here!
2021-02-05 14:40:41some body here!
2021-02-05 14:40:42some body here!
2021-02-05 14:40:43some body here!
2021-02-05 14:40:44some body here!
2021-02-05 14:40:45some body here!
2021-02-05 14:40:46some body here!
2021-02-05 14:40:47some body here!
2021-02-05 14:40:48some body here!
2021-02-05 14:40:49some body here!
2021-02-05 14:40:50some body here!
2021-02-05 14:40:51some body here!
2021-02-05 14:40:52some body here!
2021-02-05 14:40:53some body here!
2021-02-05 14:40:54some body here!
2021-02-05 14:40:55some body here!
2021-02-05 14:40:56some body here!
2021-02-05 14:40:57some body here!
2021-02-05 14:40:58some body here!
2021-02-05 14:40:59some body here!
2021-02-05 14:41:00some body here!
2021-02-05 14:41:01some body here!
2021-02-05 14:41:02some body here!
2021-02-05 14:41:03some body here!
2021-02-05 14:41:04some body here!
2021-02-05 14:41:05some body here!
2021-02-05 14:41:06some body here!
2021-02-05 14:41:09 Not anybody!
2021-02-05 14:41:11 Not anybody!
2021-02-05 14:41:13 Not anybody!
2021-02-05 14:41:15 Not anybody!
2021-02-05 14:41:17 Not anybody!
2021-02-05 14:41:19 Not anybody!
2021-02-05 14:41:21 Not anybody!
2021-02-05 14:41:23 Not anybody!
2021-02-05 14:41:25 Not anybody!
2021-02-05 14:41:27 Not anybody!
2021-02-05 14:41:29 Not anybody!
2021-02-05 14:41:31 Not anybody!
2021-02-05 14:41:33 Not anybody!
2021-02-05 14:41:35 Not anybody!
2021-02-05 14:41:37 Not anybody!
2021-02-05 14:41:39 Not anybody!
2021-02-05 14:41:41 Not anybody!
2021-02-05 14:41:43 Not anybody!
2021-02-05 14:41:45 Not anybody!
2021-02-05 14:41:47 Not anybody!
2021-02-05 14:41:49 Not anybody!
2021-02-05 14:41:51 Not anybody!
2021-02-05 14:41:53 Not anybody!
2021-02-05 14:41:55 Not anybody!
2021-02-05 14:41:57 Not anybody!
2021-02-05 14:41:59 Not anybody!
2021-02-05 14:42:01 Not anybody!
2021-02-05 14:42:03 Not anybody!
2021-02-05 14:42:05 Not anybody!
2021-02-05 14:42:07 Not anybody!
2021-02-05 14:42:09 Not anybody!
2021-02-05 14:42:11  Someone is closing!
2021-02-05 14:42:11some body here!
2021-02-05 14:42:12some body here!
2021-02-05 14:42:13some body here!
2021-02-05 14:42:14some body here!
2021-02-05 14:42:15some body here!
2021-02-05 14:42:16some body here!
2021-02-05 14:42:17some body here!
2021-02-05 14:42:18some body here!
2021-02-05 14:42:19some body here!
2021-02-05 14:42:20some body here!
2021-02-05 14:42:21some body here!
2021-02-05 14:42:22some body here!
2021-02-05 14:42:23some body here!
2021-02-05 14:42:24some body here!
2021-02-05 14:42:25some body here!
2021-02-05 14:42:26some body here!
2021-02-05 14:42:27some body here!
2021-02-05 14:42:28some body here!
2021-02-05 14:42:29some body here!
2021-02-05 14:42:30some body here!
2021-02-05 14:42:31some body here!
2021-02-05 14:42:32some body here!
2021-02-05 14:42:33some body here!
2021-02-05 14:42:34some body here!
2021-02-05 14:42:35some body here!
2021-02-05 14:42:36some body here!
2021-02-05 14:42:37some body here!
2021-02-05 14:42:38some body here!
2021-02-05 14:42:39some body here!
2021-02-05 14:42:40some body here!
2021-02-05 14:42:41some body here!
2021-02-05 14:42:42some body here!
2021-02-05 14:42:43some body here!
2021-02-05 14:42:44some body here!
2021-02-05 14:42:45some body here!
2021-02-05 14:42:46some body here!
2021-02-05 14:42:47some body here!
2021-02-05 14:42:48some body here!
2021-02-05 14:42:49some body here!
2021-02-05 14:42:50some body here!
2021-02-05 14:42:51some body here!
2021-02-05 14:42:52some body here!
2021-02-05 14:42:53some body here!
2021-02-05 14:42:54some body here!
2021-02-05 14:42:55some body here!
2021-02-05 14:42:56some body here!
2021-02-05 14:42:57some body here!
2021-02-05 14:42:58some body here!
2021-02-05 14:42:59some body here!
2021-02-05 14:43:00some body here!
2021-02-05 14:43:01some body here!
2021-02-05 14:43:02some body here!
2021-02-05 14:43:03some body here!
2021-02-05 14:43:04some body here!
2021-02-05 14:43:05some body here!
2021-02-05 14:43:06some body here!
2021-02-05 14:43:07some body here!
2021-02-05 14:43:08some body here!
2021-02-05 14:43:09some body here!
2021-02-05 14:43:10some body here!
2021-02-05 14:43:11some body here!
2021-02-05 14:43:12some body here!
2021-02-05 14:43:13some body here!
2021-02-05 14:43:14some body here!
2021-02-05 14:43:15some body here!
2021-02-05 14:43:16some body here!
2021-02-05 14:43:17some body here!
2021-02-05 14:43:18some body here!
2021-02-05 14:43:19some body here!
2021-02-05 14:43:20some body here!
2021-02-05 14:43:21some body here!
2021-02-05 14:43:22some body here!
2021-02-05 14:43:23some body here!
2021-02-05 14:43:24some body here!
2021-02-05 14:43:25some body here!
2021-02-05 14:43:26some body here!
2021-02-05 14:43:27some body here!
2021-02-05 14:43:28some body here!
2021-02-05 14:43:29some body here!
2021-02-05 14:43:30some body here!
2021-02-05 14:43:31some body here!
2021-02-05 14:43:32some body here!
2021-02-05 14:43:33some body here!
2021-02-05 14:43:34some body here!
2021-02-05 14:43:35some body here!
2021-02-05 14:43:36some body here!
2021-02-05 14:43:37some body here!
2021-02-05 14:43:38some body here!
2021-02-05 14:43:39some body here!
2021-02-05 14:43:40some body here!
2021-02-05 14:43:41some body here!
2021-02-05 14:43:42some body here!
2021-02-05 14:43:43some body here!
2021-02-05 14:43:44some body here!
2021-02-05 14:43:45some body here!
2021-02-05 14:43:46some body here!
2021-02-05 14:43:47some body here!
2021-02-05 14:43:48some body here!
2021-02-05 14:43:49some body here!
2021-02-05 14:43:50some body here!
2021-02-05 14:43:51some body here!
2021-02-05 14:43:52some body here!
2021-02-05 14:43:53some body here!
2021-02-05 14:43:54some body here!
2021-02-05 14:43:55some body here!
2021-02-05 14:43:56some body here!
2021-02-05 14:43:57some body here!
2021-02-05 14:43:58some body here!
2021-02-05 14:43:59some body here!
2021-02-05 14:44:00some body here!
2021-02-05 14:44:01some body here!
2021-02-05 14:44:02some body here!
2021-02-05 14:44:03some body here!
2021-02-05 14:44:04some body here!
2021-02-05 14:44:05some body here!
2021-02-05 14:44:06some body here!
2021-02-05 14:44:07some body here!
2021-02-05 14:44:08some body here!
2021-02-05 14:44:09some body here!
2021-02-05 14:44:12 Not anybody!
2021-02-05 14:44:14 Not anybody!
2021-02-05 14:44:16 Not anybody!
2021-02-05 14:44:18 Not anybody!
2021-02-05 14:44:20  Someone is closing!
2021-02-05 14:44:20some body here!
2021-02-05 14:44:21some body here!
2021-02-05 14:44:24 Not anybody!
2021-02-05 14:44:26  Someone is closing!
2021-02-05 14:44:26some body here!
2021-02-05 14:44:27some body here!
2021-02-05 14:44:28some body here!
2021-02-05 14:44:29some body here!
2021-02-05 14:44:30some body here!
2021-02-05 14:44:31some body here!
2021-02-05 14:44:32some body here!
2021-02-05 14:44:33some body here!
2021-02-05 14:44:34some body here!
2021-02-05 14:44:35some body here!
2021-02-05 14:44:36some body here!
2021-02-05 14:44:37some body here!
2021-02-05 14:44:38some body here!
2021-02-05 14:44:39some body here!
2021-02-05 14:44:40some body here!
2021-02-05 14:44:41some body here!
2021-02-05 14:44:42some body here!
2021-02-05 14:44:43some body here!
2021-02-05 14:44:44some body here!
2021-02-05 14:44:45some body here!
2021-02-05 14:44:46some body here!
2021-02-05 14:44:47some body here!
2021-02-05 14:44:48some body here!
2021-02-05 14:44:49some body here!
2021-02-05 14:44:50some body here!
2021-02-05 14:44:51some body here!
2021-02-05 14:44:52some body here!
2021-02-05 14:44:53some body here!
2021-02-05 14:44:54some body here!
2021-02-05 14:44:55some body here!
2021-02-05 14:44:58 Not anybody!
2021-02-05 14:45:00 Not anybody!
2021-02-05 14:45:02 Not anybody!
2021-02-05 14:45:04 Not anybody!
2021-02-05 14:45:06 Not anybody!
2021-02-05 14:45:08  Someone is closing!
2021-02-05 14:45:08some body here!
2021-02-05 14:45:09some body here!
2021-02-05 14:45:10some body here!
2021-02-05 14:45:11some body here!
2021-02-05 14:45:12some body here!
2021-02-05 14:45:13some body here!
2021-02-05 14:45:14some body here!
2021-02-05 14:45:15some body here!
2021-02-05 14:45:16some body here!
2021-02-05 14:45:18some body here!
2021-02-05 14:45:19some body here!
2021-02-05 14:45:20some body here!
2021-02-05 14:45:21some body here!
2021-02-05 14:45:22some body here!
2021-02-05 14:45:23some body here!
2021-02-05 14:45:24some body here!
2021-02-05 14:45:25some body here!
2021-02-05 14:45:26some body here!
2021-02-05 14:45:27some body here!
2021-02-05 14:45:28some body here!
2021-02-05 14:45:29some body here!
2021-02-05 14:45:30some body here!
2021-02-05 14:45:31some body here!
2021-02-05 14:45:32some body here!
2021-02-05 14:45:33some body here!
2021-02-05 14:45:34some body here!
2021-02-05 14:45:35some body here!
2021-02-05 14:45:36some body here!
2021-02-05 14:45:37some body here!
2021-02-05 14:45:38some body here!
2021-02-05 14:45:39some body here!
2021-02-05 14:45:42 Not anybody!
2021-02-05 14:45:44 Not anybody!
2021-02-05 14:45:46 Not anybody!
2021-02-05 14:45:48 Not anybody!
2021-02-05 14:45:50  Someone is closing!
2021-02-05 14:45:50some body here!
2021-02-05 14:45:51some body here!
2021-02-05 14:45:52some body here!
2021-02-05 14:45:53some body here!
2021-02-05 14:45:54some body here!
2021-02-05 14:45:55some body here!
2021-02-05 14:45:56some body here!
2021-02-05 14:45:57some body here!
2021-02-05 14:45:58some body here!
2021-02-05 14:45:59some body here!
2021-02-05 14:46:00some body here!
2021-02-05 14:46:01some body here!
2021-02-05 14:46:02some body here!
2021-02-05 14:46:03some body here!
2021-02-05 14:46:04some body here!
2021-02-05 14:46:05some body here!
2021-02-05 14:46:06some body here!
2021-02-05 14:46:07some body here!
2021-02-05 14:46:08some body here!
2021-02-05 14:46:09some body here!
2021-02-05 14:46:10some body here!
2021-02-05 14:46:11some body here!
2021-02-05 14:46:12some body here!
2021-02-05 14:46:13some body here!
2021-02-05 14:46:14some body here!
2021-02-05 14:46:15some body here!
2021-02-05 14:46:16some body here!
2021-02-05 14:46:17some body here!
2021-02-05 14:46:18some body here!
2021-02-05 14:46:21 Not anybody!
2021-02-05 14:46:23  Someone is closing!
2021-02-05 14:46:23some body here!
2021-02-05 14:46:24some body here!
2021-02-05 14:46:25some body here!
2021-02-05 14:46:26some body here!
2021-02-05 14:46:27some body here!
2021-02-05 14:46:28some body here!
2021-02-05 14:46:29some body here!
2021-02-05 14:46:30some body here!
2021-02-05 14:46:31some body here!
2021-02-05 14:46:32some body here!
2021-02-05 14:46:33some body here!
2021-02-05 14:46:34some body here!
2021-02-05 14:46:35some body here!
2021-02-05 14:46:36some body here!
2021-02-05 14:46:37some body here!
2021-02-05 14:46:38some body here!
2021-02-05 14:46:39some body here!
2021-02-05 14:46:40some body here!
2021-02-05 14:46:41some body here!
2021-02-05 14:46:42some body here!
2021-02-05 14:46:43some body here!
2021-02-05 14:46:44some body here!
2021-02-05 14:46:45some body here!
2021-02-05 14:46:46some body here!
2021-02-05 14:46:47some body here!
2021-02-05 14:46:48some body here!
2021-02-05 14:46:49some body here!
2021-02-05 14:46:50some body here!
2021-02-05 14:46:51some body here!
2021-02-05 14:46:54 Not anybody!
2021-02-05 14:46:56 Not anybody!
2021-02-05 14:46:58  Someone is closing!
2021-02-05 14:46:58some body here!
2021-02-05 14:46:59some body here!
2021-02-05 14:47:02 Not anybody!
2021-02-05 14:47:04 Not anybody!
2021-02-05 14:47:06  Someone is closing!
2021-02-05 14:47:06some body here!
2021-02-05 14:47:09 Not anybody!
2021-02-05 14:47:11 Not anybody!
2021-02-05 14:47:13 Not anybody!
2021-02-05 14:47:15  Someone is closing!
2021-02-05 14:47:15some body here!
2021-02-05 14:47:18 Not anybody!
2021-02-05 14:47:20  Someone is closing!
2021-02-05 14:47:20some body here!
2021-02-05 14:47:23 Not anybody!
2021-02-05 14:47:25 Not anybody!
2021-02-05 14:47:27 Not anybody!
2021-02-05 14:47:29 Not anybody!
2021-02-05 14:47:31  Someone is closing!
2021-02-05 14:47:31some body here!
2021-02-05 14:47:32some body here!
2021-02-05 14:47:33some body here!
2021-02-05 14:47:34some body here!
2021-02-05 14:47:35some body here!
2021-02-05 14:47:36some body here!
2021-02-05 14:47:37some body here!
2021-02-05 14:47:38some body here!
2021-02-05 14:47:39some body here!
2021-02-05 14:47:40some body here!
2021-02-05 14:47:41some body here!
2021-02-05 14:47:44 Not anybody!
2021-02-05 14:47:46  Someone is closing!
2021-02-05 14:47:46some body here!
2021-02-05 14:47:47some body here!
2021-02-05 14:47:48some body here!
2021-02-05 14:47:49some body here!
2021-02-05 14:47:50some body here!
2021-02-05 14:47:51some body here!
2021-02-05 14:47:52some body here!
2021-02-05 14:47:53some body here!
2021-02-05 14:47:54some body here!
2021-02-05 14:47:55some body here!
2021-02-05 14:47:56some body here!
2021-02-05 14:47:59 Not anybody!
2021-02-05 14:48:01 Not anybody!
2021-02-05 14:48:03 Not anybody!
2021-02-05 14:48:05 Not anybody!
2021-02-05 14:48:07  Someone is closing!
2021-02-05 14:48:07some body here!
2021-02-05 14:48:08some body here!
2021-02-05 14:48:09some body here!
^[[A2021-02-05 14:48:10some body here!
2021-02-05 14:48:11some body here!
^CTraceback (most recent call last):
  File "66.py", line 40, in <module>
    detct()
  File "66.py", line 30, in detct
    beep()
  File "66.py", line 17, in beep
    time.sleep(0.5)
KeyboardInterrupt
pi@raspberrypi:~ $ sudo python3 66.py 
2021-02-05 14:48:14  Hello sky!
2021-02-05 14:48:14  Someone is closing!
2021-02-05 14:48:14some body here!
2021-02-05 14:48:15some body here!
2021-02-05 14:48:16some body here!
2021-02-05 14:48:17some body here!
2021-02-05 14:48:20 Not anybody!
2021-02-05 14:48:22 Not anybody!
2021-02-05 14:48:24  Someone is closing!
2021-02-05 14:48:24some body here!
2021-02-05 14:48:25some body here!
2021-02-05 14:48:26some body here!
2021-02-05 14:48:27some body here!
2021-02-05 14:48:28some body here!
2021-02-05 14:48:29some body here!
2021-02-05 14:48:30some body here!
^CTraceback (most recent call last):
  File "66.py", line 40, in <module>
    detct()
  File "66.py", line 30, in detct
    beep()
  File "66.py", line 19, in beep
    time.sleep(0.5)
KeyboardInterrupt
pi@raspberrypi:~ $ cat 66.py 
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
pi@raspberrypi:~ $ vi duoremi.py
pi@raspberrypi:~ $ ls
66.py  Bookshelf  didi.py  duoremi.py  ez_setup.py  setuptools-33.1.1.zip
pi@raspberrypi:~ $ sudo python3 duoremi.py 
duoremi.py:7: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(11, GPIO.OUT)
pi@raspberrypi:~ $ sudo python3 duoremi.py 
duoremi.py:7: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(11, GPIO.OUT)
pi@raspberrypi:~ $ 
pi@raspberrypi:~ $ 
pi@raspberrypi:~ $ 
pi@raspberrypi:~ $ 
pi@raspberrypi:~ $ sudo python3 duoremi.py 
duoremi.py:7: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(11, GPIO.OUT)
pi@raspberrypi:~ $ ll
-bash: ll: command not found
pi@raspberrypi:~ $ ls
66.py  Bookshelf  didi.py  duoremi.py  ez_setup.py  setuptools-33.1.1.zip
pi@raspberrypi:~ $ sudo python3 didi.py 
didi.py:4: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(11, GPIO.OUT)
^Cpi@raspberrypi:~ $ 
pi@raspberrypi:~ $ 
pi@raspberrypi:~ $ 
pi@raspberrypi:~ $ sudo python3 didi.py 
^Cpi@raspberrypi:~ $ sudo python3 didi.py 
^Cpi@raspberrypi:~ $ sudo python3 didi.py 
^Cpi@raspberrypi:~ $ 
pi@raspberrypi:~ $ 
pi@raspberrypi:~ $ 
pi@raspberrypi:~ $ 
pi@raspberrypi:~ $ sudo python3 duoremi.py 
pi@raspberrypi:~ $ sudo python3 duoremi.py 
duoremi.py:7: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(11, GPIO.OUT)
pi@raspberrypi:~ $ sudo python3 duoremi.py 
duoremi.py:7: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(11, GPIO.OUT)
pi@raspberrypi:~ $ 
pi@raspberrypi:~ $ 
pi@raspberrypi:~ $ 
pi@raspberrypi:~ $ 
pi@raspberrypi:~ $ 
pi@raspberrypi:~ $ sudo python3 duoremi.py 
duoremi.py:7: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(11, GPIO.OUT)
pi@raspberrypi:~ $ cat 66.py 
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
