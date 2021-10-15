import RPi.GPIO as GPIO
import time

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

def increasecount1():
   global input1count
   input1count =+ 1

def increasecount2():
   global input2count
   input1count =+ 1

def increasecount3():
   global input3count
   input1count =+ 1

def increasecount4():
   global input4count
   input1count =+ 1

GPIO.add_event_detect(12, GPIO.RISING, callback=increasecount1())
GPIO.add_event_detect(13, GPIO.RISING, callback=increasecount2())
GPIO.add_event_detect(18, GPIO.RISING, callback=increasecount3())
GPIO.add_event_detect(19, GPIO.RISING, callback=increasecount4())


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
      print("Input 1 = "+ input1count," Input 2 = "+ input2count," Input 3 = "+ input3count," Input 4 = "+ input4count,end='\r')


     
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
   print("Keyboard interrupt")

except:
   print("FUCK, some error occured") 

finally:
   print("clean up") 
   GPIO.cleanup() # cleanup all GPIO 