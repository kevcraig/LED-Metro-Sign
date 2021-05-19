import time
import sys
from rgbmatrix import RGBMatrix, RGBMatrixOptions # https://github.com/hzeller/rpi-rgb-led-matrix
from PIL import Image

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat' # my hat hardware
matrix = RGBMatrix(options=options)

# update image passed from Prod_Prediction_Ticker.py
while True:
    
    # image output by Prod_Prediction_Ticker
    image_file = 'Prod_Board_Photo.png'
    image = Image.open(image_file)

    # create a thumbnail that fits screen
    image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
    matrix.SetImage(image.convert('RGB'))

    time.sleep(10) # sleep 10 seconds before refresh