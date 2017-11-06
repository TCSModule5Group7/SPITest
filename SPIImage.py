#!/usr/bin/python
# import spidev
#
import numpy as np

# import scipy.misc as smp
#
# spi = spidev.SpiDev()
# spi.open(0, 0)
# spi.mode = 0b00
# spi.max_speed_hz = 125000000
#
op_read = 0b10000000
no_data = 0b00000000
four_byte_array = [op_read, no_data, op_read, no_data, op_read, no_data, op_read, no_data]

# The camera records at 640 * 480
rows = 480
columns = 640
color_channels = 3


horizontal_blank_array = np.zeros(160, dtype=np.uint8)
for i in xrange(0, 16):
    horizontal_blank_array.item() = 1

for i in xrange(111, 160):
    horizontal_blank_array[i] = 1

for i in np.nditer(horizontal_blank_array):
    print str(i) + "|" + str(horizontal_blank_array.get)

vertical_blank_array = np.zeros(45, dtype=np.uint8)
for i in xrange(0, 10):
    vertical_blank_array[i] = 1

for i in xrange(12, 45):
    vertical_blank_array[i] = 1

for i in np.nditer(vertical_blank_array):
    print str(i) + "|" + str(vertical_blank_array[i])

if __name__ == "__main__":
    frame = np.zeros((rows, columns, color_channels), dtype=np.uint8)
    #
    # v_sync = 0
    # h_sync = 0
    # row = 0
    # column = 0
    # while column < columns or row < rows:
    #     pixel = spi.xfer2(four_byte_array)
    #     h_sync_new = (pixel[] >>) & 0b00000001
    #     v_sync_new = (pixel[] >>) & 0b00000001
    #     if h_sync_new == 1 and v_sync_new == 1:
    #         frame[row_i][y][0] = pixel[]  # Red
    #         frame[row_i][y][1] = pixel[]  # Green
    #         frame[row_i][y][2] = pixel[]  # Blue
    #         x += 1
    #
    #     elif h_sync_new == 1 and h_sync_old == 0:
    #         x = 0
    #         y += 1
    #
    #     elif v_sync_new == 1 and v_sync_old == 0:
    #         y = 0
    # img = smp.toimage(frame)
    # img.show()
    # spi.close()
