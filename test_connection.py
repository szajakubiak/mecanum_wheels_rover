import board
from busio import UART

buffer=bytearray(14)
uart = UART(board.TX, board.RX, baudrate=115200)

while True:
    c = uart.read(1)
    if c == b" ":
        c = uart.read(1)
        if c == b"@":
            uart.readinto(buffer)
            ch1 = buffer[1] * 255 + buffer[0]
            ch2 = buffer[3] * 255 + buffer[2]
            ch3 = buffer[5] * 255 + buffer[4]
            ch4 = buffer[7] * 255 + buffer[6]
            ch5 = buffer[9] * 255 + buffer[8]
            ch6 = buffer[11] * 255 + buffer[10]
            print('ch  1-',ch1,'  2-',ch2,'  3-',ch3,'  4-',ch4,'  5-',ch5,'   6-',ch6)
