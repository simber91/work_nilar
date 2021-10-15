import RPi.GPIO as GPIO
import time
import logging

logit = logging.getLogger(__name__)
logit.setLevel(logging.INFO)
file_handler = logging.FileHandler('count_and_pulsing.log')
formatter = logging.Formatter('%(asctime)s : %(message)s')
file_handler.setFormatter(formatter)
logit.addHandler(file_handler)

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN)     # Setup gpio as input I1 
GPIO.setup(13, GPIO.IN)     # Setup gpio as input I2
for i in range(18, 24):
   GPIO.setup(i, GPIO.IN)     # Setup gpio as input I3-I6
for i in range(34, 43):
   GPIO.setup(i, GPIO.OUT)    # Setup gpio ENABLE and O1-O8 as inputs
   GPIO.output(i, False)      # Start at zero

global input1count
global input2count
global input3count
global input4count
input1count = 0
input2count = 0
input3count = 0
input4count = 0

def incin1():
   global input1count
   input1count =+ 1

def incin2():
   global input2count
   input1count =+ 1

def incin3():
   global input3count
   input1count =+ 1

def incin4():
   global input4count
   input1count =+ 1

GPIO.add_event_detect(12, GPIO.RISING, callback=incin1())
GPIO.add_event_detect(13, GPIO.RISING, callback=incin2())
GPIO.add_event_detect(18, GPIO.RISING, callback=incin3())
GPIO.add_event_detect(19, GPIO.RISING, callback=incin4())

print("Test function pulsing on outputs and counting on inputs")

try:
   pulsetime = input("Enter a pulsetime in seconds: ") 
   while(True):

      print("Pulsing for "  + str(pulsetime) + " sec")
      for i in range(34, 43):
         GPIO.output(i, True)
      time.sleep(pulsetime)
      for i in range(34, 43):
         GPIO.output(i, False)    
      print("Input 1 = " + str(input1count) +" Input 2 = "+ str(input2count) + " Input 3 = " + str(input3count) + " Input 4 = " + str(input4count), end='\r')
      logit.info("Input 1 = " + str(input1count) +" Input 2 = "+ str(input2count) + " Input 3 = " + str(input3count) + " Input 4 = " + str(input4count)

     
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
   print("Keyboard interrupt")

except:
   print("FUCK, some error occured") 

finally:
   print("clean up") 
   GPIO.cleanup() # cleanup all GPIO 

