#!/usr/bin/python
from spi import SPI

spi = SPI("/dev/spidev0.0")
spi.mode = SPI.MODE_0
spi.bits_per_word = 8
spi.speed = 125000000
received = spi.transfer([0x11, 0x22, 0xFF])
spi.write([0x12, 0x34, 0xAB, 0xCD])
received = spi.read(10)

op_tx = 0b00000000
no_data = 0b00000000

four_byte_array = [op_tx, no_data, no_data, no_data]

try:
    while True:
        response = spi.xfer2(four_byte_array)
        print(bin(response[0]) + "|" + bin(response[1]) + "|" + bin(response[2]) + "|" + bin(response[3]))
except KeyboardInterrupt:
    spi.close()
