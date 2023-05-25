import time
import board
import bitbangio
from adafruit_max7219 import matrices
from digitalio import DigitalInOut

cs_pin = DigitalInOut(board.GP7)
spi_mosi = board.GP5
spi_clk = board.GP4
spi = bitbangio.SPI(spi_clk, spi_mosi)

display = matrices.Matrix8x8(spi, cs_pin)

# replace this with the path to your frame and brightness file
FRAME_FILE_PATH = 'movies/5-heart.txt'

def rotate_frame_90_degrees_clockwise(frame):
    rotated_frame = [0] * 8

    for x in range(8):
        for y in range(8):
            pixel = (frame[7-y] >> x) & 0b1  # we're reading the original frame in a "rotated" way
            if pixel:
                rotated_frame[x] |= (1 << (7-y))  # we're writing the pixel into the new location in the rotated frame

    return rotated_frame

def read_frames_from_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read().split('\n\n')
        frames_and_brightness = []

        for section in content:
            lines = section.split('\n')
            lines = [line.strip() for line in lines if line.strip()]  # strip and filter out empty lines
            if not lines:  # skip section if it's empty after filtering
                continue

            while lines:
                brightness = int(lines.pop(0), 10)  # get the first line as brightness
                frame = []
                try:
                    # get next 8 lines as a frame
                    for _ in range(8):
                        frame.append(int(lines.pop(0), 2))
                except ValueError:
                    print(f"Error converting binary string to int. lines: {lines}")
                    continue
                frames_and_brightness.append((brightness, frame))

        return frames_and_brightness


frames_and_brightness = read_frames_from_file(FRAME_FILE_PATH)

while True:
    for brightness, frame in frames_and_brightness:
        # set brightness
        display.brightness(brightness)

        # rotate frame
        frame = rotate_frame_90_degrees_clockwise(frame)

        # display frame
        for row in range(8):
            for col in range(8):
                pixel = (frame[row] >> (7-col)) & 0b1  # we're reading the rotated frame normally
                display.pixel(col, row, pixel)  # Note that we swapped col and row here
        display.show()

        # pause before next frame
        time.sleep(0.2)

