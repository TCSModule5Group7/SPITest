#!/usr/bin/python
import spidev

op_tx = 0b00000001
no_data = 0b00000000

four_byte_array = [op_tx, no_data, no_data, no_data]

spi = spidev.SpiDev()
spi.open(0, 0)
spi.mode = 0b01
spi.max_speed_hz = 125000000
iterations = 24
errors = 0
if __name__ == "__main__":
    try:
        while iterations >= 0:
            response = spi.xfer2(four_byte_array)
            print(format(response[0], '#010b') + "|" + format(response[1], '#010b') + "|" + format(response[2], '#010b') + "|" + format(response[3], '#010b'))
            iterations -= 1
            if response[3] == 0:
                errors += 1
    finally:
        print(errors)
        spi.close()

