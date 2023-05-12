from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
import time

mh = Raspi_MotorHAT(addr=0x6f)
myMotor = mh.getMotor(2)


#myMotor.setSpeed(150)
#myMotor.run(Raspi_MotorHAT.FORWARD)
myMotor.start_slow(200)
time.sleep(3)
myMotor.stop_slow()

#myMotor.run(Raspi_MotorHAT.RELEASE)
