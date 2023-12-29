import board
import digitalio
import pwmio
from adafruit_motor import motor
from busio import UART

buffer = bytearray(14)
uart = UART(board.TX, board.RX  , baudrate=115200)

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

def map_value(val, from_min=1000, from_max=2000, to_min=-1, to_max=1):
    if val < from_min:
        val = from_min
    if val > from_max:
        val = from_min
    
    percentage = (val - from_min) / (from_max - from_min)
    
    mapped_value = to_min + percentage * (to_max - to_min)
    
    return mapped_value

def read_commands():
    while uart.read(1) != b" ":
        pass
    c = uart.read(1)
    if c == b"@":
        uart.readinto(buffer)
        ch1 = buffer[1] * 255 + buffer[0]
        ch2 = buffer[3] * 255 + buffer[2]
        ch3 = buffer[5] * 255 + buffer[4]
        ch4 = buffer[7] * 255 + buffer[6]
        ch5 = buffer[9] * 255 + buffer[8]
        ch6 = buffer[11] * 255 + buffer[10]

        return (ch1, ch2, ch3, ch4, ch5, ch6)
    else:
        return (1500, 1500, 1500, 1000, 1000, 1000)

mfr.throttle = 0
mfl.throttle = 0
mbr.throttle = 0
mbl.throttle = 0

sleep(1)
while True:
    ch1, ch2, ch3, ch4, ch5, ch6 = read_commands()

    spd = map_value(ch2)

    mfr.throttle = spd
    mfl.throttle = spd
    mbr.throttle = spd
    mbl.throttle = spd
