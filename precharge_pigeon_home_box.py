import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(34, GPIO.OUT)    # Setup gpio ENABLE
GPIO.setup(35, GPIO.OUT)    # Setup gpio as output O1 = Negative contactor
GPIO.setup(36, GPIO.OUT)    # Setup gpio as output O2 = Positive contactor
GPIO.setup(37, GPIO.OUT)    # Setup gpio as output O3 = precharge contactor

GPIO.output(34, False)      # Enable
GPIO.output(35, False)      # Start at zero
GPIO.output(40, False)      # Start at zero
GPIO.output(41, False)      # Start at zero

print("Precharge function for Homebox PiGEON")

try:
     prechargetime = input("Enter a time in seconds: ") 
     GPIO.output(35, True)
     print("Connected positive contactor waiting for 3 sec")
     time.sleep(3)
     GPIO.output(41, True)
     print("Precharging for " + str(prechargetime) + " sec")
     time.sleep(prechargetime)
     GPIO.output(40, True)
     print("Negative contactor connected. Precharge done, exiting program in 20 sec")
     time.sleep(20)

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
   print("Keyboard interrupt")

except:
   print("some error") 

finally:
   print("clean up") 
   GPIO.cleanup() # cleanup all GPIO 
