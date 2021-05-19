import time
import sys
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat' 
matrix = RGBMatrix(options=options)

while True:
    
    # image output by Prod_Prediction_Ticker
    image_file = 'Prod_Board_Photo.png'
    image = Image.open(image_file)

    # Create a thumbnail that first our screen
    image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
    matrix.SetImage(image.convert('RGB'))

    time.sleep(10) # sleep 10 seconds before refresh