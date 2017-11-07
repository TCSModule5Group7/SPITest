#!/usr/bin/python
import spidev
from time import sleep

byteArray = [None] * 0b11111111

for i in range(0b00000000, 0b11111111):
    if i % 2 ==0:
        byteArray[i] = 0x0F
    else:
        byteArray[i] = 0xF0

transfer = 0b00000000
read = 0b10000000
write = 0b01000000
nop = 0b11000000

spi = spidev.SpiDev()
spi.open(0, 0)
spi.mode = 0b00
spi.max_speed_hz = 31200000
def bytestohex(bytes):
    result = []
    for byte in bytes:
        result.append(format(byte, '#010b'))
    return result

def loop():
    try:
        temp = [0x00, 0x0F]
        resp = spi.xfer2(temp)
        print("message: " + str(bytestohex(temp)) + " | response: " + str(bytestohex(resp)))
        """
        while True:
            print("loop")
            for b in byteArray:
                temp = [transfer, 0xf0]
                resp = spi.xfer2(temp)
                print("message: " + str(bytestohex(temp)) +  " | response: " + str(bytestohex(resp)))
                sleep(0.5)
        """
    except KeyboardInterrupt:
        spi.close()

loop()

