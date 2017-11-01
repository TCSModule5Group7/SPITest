#!/usr/bin/python
import spidev
print('Imported spidev library')
spi = spidev.SpiDev()
print('Initialized spi object')
spi.open(0, 0)
print('Opened spi connection on bus 0 and device 0')
spi.max_speed_hz = 31200000
print('Set spidev max clock speed to 31.2MHz')
spidev.mode = 0b00
print('Set spidev mode to 0b00 so CLOP = 0 and CPHA = 0')
spi.writebyes([0xFF])
print('Written 0xFF')
