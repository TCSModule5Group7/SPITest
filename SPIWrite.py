#!/usr/bin/python
import spidev
import time

byte_array_a = [0x00, 0xff] * 10
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 31200000
spi.mode = 0b00

def bytestohex(byte_array_b):
    result = []
    for byte in byte_array_b:
        result.append(hex(byte))
    return result

try:
    while True:
        print("loop")
        spi.writebytes(byte_array_a)      
        time.sleep(1)

except KeyboardInterrupt:
    spi.close()
