# LED-Metro-Sign

Build you own real time Washington DC Metro board!

## Hardware:
  1. Raspberry Pi Zero WH
  2. Adafruit RGB Matrix Bonnet for Raspberry Pi
  3. 64x32 RGB LED Matrix - 6mm pitch
  4. 16GB Micro SD Card
  5. 5V power supply
  

## Software:
I wrote Prod_Prediction_Ticker.py & Prod_Display_Image.py to fetch from the WMATA API, format responses for the LED board, and display refreshed information at 10-second intervals. I levered the existing rpi-rgb-led-matrix by Henner Zeller to handle the connection between images stored on the PI and the physical LED board.

Once a connection to the Raspberry Pi is established, you can follow these steps. Note that I am using a Raspberry Pi Zero WH running Raspberry Pi OS 32-bit with a headless connection through SSH. 

1. Install Python Dependencies.
    sudo apt-get install python-dev libatlas-base-dev # numpy/pandas dependency
    sudo pip3 install pandas
    sudo pip3 install numpy
    sudo apt-get install -y git python3-dev python3-pillow # dependencies for Pillow
    git clone https://github.com/hzeller/rpi-rgb-led-matrix.git # rgbmatrix library

2. Setup rpi-rgb-led-matrix library
    cd rpi-rgb-led-matrix
    make build-python PYTHON=$(which python3)
    sudo make install-python PYTHON=$(which python3)

3. Clone this repo
    clone

4. Create your own WMATA_API_KEY.txt file in the LED-Metro-Sign directory
    touch WMATA_API_KEY.txt
    nano WMATA_API_KEY.txt > add your key and save

5. Run both python programs from the LED-Metro-Sign directory and quit ssh connection
    nohup python3 Prod_Prediction_Ticker.py & sudo nohup python3 Prod_Display_Image.py
