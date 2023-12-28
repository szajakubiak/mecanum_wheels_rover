import board
import digitalio
import pwmio
from adafruit_motor import motor
from time import sleep

MAX_SPD = 0.75
RIDE_TME = 2

mfr_in1 = pwmio.PWMOut(board.D7, frequency=5000, duty_cycle=0)
mfr_in2 = pwmio.PWMOut(board.D8, frequency=5000, duty_cycle=0)
mfr_pwm = digitalio.DigitalInOut(board.D9)
mfr_pwm.direction = digitalio.Direction.OUTPUT
mfr_pwm.value = True

mfl_in1 = pwmio.PWMOut(board.D4, frequency=5000, duty_cycle=0)
mfl_in2 = pwmio.PWMOut(board.D5, frequency=5000, duty_cycle=0)
mfl_pwm = digitalio.DigitalInOut(board.D6)
mfl_pwm.direction = digitalio.Direction.OUTPUT
mfl_pwm.value = True

mbr_in1 = pwmio.PWMOut(board.D14, frequency=5000, duty_cycle=0)
mbr_in2 = pwmio.PWMOut(board.D15, frequency=5000, duty_cycle=0)
mbr_pwm = digitalio.DigitalInOut(board.D16)
mbr_pwm.direction = digitalio.Direction.OUTPUT
mbr_pwm.value = True

mbl_in1 = pwmio.PWMOut(board.D17, frequency=5000, duty_cycle=0)
mbl_in2 = pwmio.PWMOut(board.D18, frequency=5000, duty_cycle=0)
mbl_pwm = digitalio.DigitalInOut(board.D19)
mbl_pwm.direction = digitalio.Direction.OUTPUT
mbl_pwm.value = True

mfr = motor.DCMotor(mfr_in1, mfr_in2)
mfl = motor.DCMotor(mfl_in1, mfl_in2)
mbr = motor.DCMotor(mbr_in1, mbr_in2)
mbl = motor.DCMotor(mbl_in1, mbl_in2)

sleep(5)
while True:
    mfr.throttle = MAX_SPD
    mfl.throttle = MAX_SPD
    mbr.throttle = MAX_SPD
    mbl.throttle = MAX_SPD
    sleep(RIDE_TME)
    mfr.throttle = 0
    mfl.throttle = 0
    mbr.throttle = 0
    mbl.throttle = 0
    sleep(RIDE_TME)
    mfr.throttle = -MAX_SPD
    mfl.throttle = -MAX_SPD
    mbr.throttle = -MAX_SPD
    mbl.throttle = -MAX_SPD
    sleep(RIDE_TME)
    mfr.throttle = 0
    mfl.throttle = 0
    mbr.throttle = 0
    mbl.throttle = 0
    sleep(RIDE_TME)
