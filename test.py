#!/usr/bin/python
import sys
import os

ap_path = os.getcwd()
sys.path.append(ap_path + "/control")
sys.path.append(ap_path + "/recognition")
sys.path.append(ap_path + "/gui")
from control.Raspi_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x6F)

servoDefualt = 270
servoMin = 180  # Min pulse length out of 4096
servoMax = 350  # Max pulse length out of 4096

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print ("%d us per period" % pulseLength)
  pulseLength /= 4096                     # 12 bits of resolution
  print ("%d us per bit" % pulseLength)
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWM(1, 0, servoDefualt)
pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
for i in range(3):
  # Change speed of continuous servo on channel O
  pwm.setPWM(1, 0, servoMin)
  time.sleep(1)
  pwm.setPWM(1, 0, servoMax)
  time.sleep(1)
  
  
pwm.setPWM(1, 0, servoDefualt)
  
  



