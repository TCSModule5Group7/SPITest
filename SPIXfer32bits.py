#!/usr/bin/python
import spidev

op_tx = 0b00000000
no_data = 0b00000000

four_byte_array = [op_tx, no_data, no_data, no_data]

spi = spidev.SpiDev()
spi.open(0, 0)
spi.mode = 0b00
spi.max_speed_hz = 125000000

if __name__ == "__main__":
    try:
        while True:
            response = spi.xfer2(four_byte_array)
            print(bin(response[0]) + "|" + bin(response[1]) + "|" + bin(response[2]) + "|" + bin(response[3]))
    except KeyboardInterrupt:
        spi.close()

