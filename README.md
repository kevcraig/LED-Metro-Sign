# LED-Metro-Sign

Build you own real time Washington DC Metro board! This board was made to resemble the train prediction board found in DC metro stations. 

## Hardware:
  1. Raspberry Pi Zero WH
  2. Adafruit RGB Matrix Bonnet for Raspberry Pi
  3. 64x32 RGB LED Matrix - 6mm pitch
  4. 16GB Micro SD Card
  5. 5V power supply
  
  <a href='https://howchoo.com/pi/raspberry-pi-led-matrix-panel'> Here </a> is a helpful guide that I used to set up hardware components for a LED matrix.

## Software:
I wrote Prod_Prediction_Ticker.py & Prod_Display_Image.py to fetch from the WMATA API, format responses for the LED board, and display refreshed information at 10-second intervals. I used the existing rpi-rgb-led-matrix library by Henner Zeller to handle the connection between images stored on the PI and the physical LED board.

Once a connection to the Raspberry Pi is established, follow these steps. Note that I used a Raspberry Pi Zero WH running Raspberry Pi OS 32-bit with a headless connection through SSH. The following is a list of shell commands to install dependencies and items from this repo.

1. Install Python Dependencies.
    - sudo apt-get install python-dev libatlas-base-dev # numpy/pandas dependency
    - sudo pip3 install pandas
    - sudo pip3 install numpy
    - sudo apt-get install -y git python3-dev python3-pillow # dependencies for Pillow
    - git clone https://github.com/hzeller/rpi-rgb-led-matrix.git # rgbmatrix library

2. Setup rpi-rgb-led-matrix library
    - cd rpi-rgb-led-matrix
    - make build-python PYTHON=$(which python3)
    - sudo make install-python PYTHON=$(which python3)

3. Clone this repo
    - git clone https://github.com/kevcraig/LED-Metro-Sign.git

4. Create your own WMATA_API_KEY.txt file in the LED-Metro-Sign directory. Request a WMATA <b>developer</b> key <a href = 'https://developer.wmata.com/'> here </a>
    - touch WMATA_API_KEY.txt # create file
    - cat > WMATA_API_KEY.txt # paste your key and take note to not enter any excess spaces or lines

5. Update the board_station variable in line 11 of the Prod_Prediction_Ticker.py file to match your desired station

6. Run both python programs from the LED-Metro-Sign directory. Sign will still run even if you quit SSH connection
    - sudo nohup python3 Prod_Prediction_Ticker.py & sudo nohup python3 Prod_Display_Image.py

7. OPTIONAL: Kill all processes on the raspberrypi if you want to troubleshoot something
    - sudo killall python3

6.1 Kill all python processes on the raspberrypi if you want to troubleshoot something
    - sudo killall python3