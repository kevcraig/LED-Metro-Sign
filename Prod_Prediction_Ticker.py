import platform
import os
import http.client, urllib.request, urllib.parse, urllib.error, json, time 
import pandas as pd
from PIL import ImageFont # image
from PIL import Image # image
from PIL import ImageDraw # image

# WMATA API key
api_key = open("WMATA_API_KEY.txt", "r") 
WMATA_KEY = api_key.read()
headers = {
    'api_key': WMATA_KEY
    }

# Get station data from API
def get_stations(line_code):
    
    # params
    params = urllib.parse.urlencode({
    'LineCode': line_code
    })
    
    # hit api
    try:
        conn = http.client.HTTPSConnection('api.wmata.com')
        conn.request("GET", "/Rail.svc/json/jStations?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        return(json.loads(data))
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

# Get predictions from api
def get_preds(StationCode):

    # params
    params = { 
        'StationCodes': StationCode
        }
    # hit api
    try:
        conn = http.client.HTTPSConnection('api.wmata.com')
        conn.request("GET", "/StationPrediction.svc/json/GetPrediction/" + params['StationCodes'] ,"{body}", headers)
        response = conn.getresponse()
        data = response.read()
        return(json.loads(data))
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

# function to control font switches between debuging on mac and raspberrypi
def get_font():
    platform_name = platform.system()
    if platform_name == 'Linux': # raspberry pi os
        font = ImageFont.truetype('FreeMono.ttf', 8)
    elif platform_name =='Darwin': # mac os
        font = ImageFont.truetype("Arial.ttf",15)
    return(font)

# lookup table for spelling changes. Do this so text fits on screen at 8pt font
line_lookup = {'Brnch Av' : 'BrchAv',
               'Ft.Tottn' : 'Ft.Ttn',
               'Glenmont' : 'Glnmnt',
               'Shady Gr' : 'ShdyGr',
               'NewCrltn' : 'NwCrtn',
               'Wiehle'   : 'Wiehle',
               'Largo'    : 'Largo',
               'Vienna'   : 'Vienna',
               'Grnbelt'  : 'Grnblt',
               'Hntingtn' : 'Hntngn'}

# lookup table for boarding and arriving code changes
code_lookup = {'ARR' : 'A',
               'BRD' : 'B'}

# Run program
station = 'E03' # U-street station is defualt. Use get_stations() function to find the station code for your line/station
lines_to_print = 3 # anything less than 4 will fit
while True:
    # get preds
    pred_data = get_preds(station)['Trains']
    # check if data is present. If not make blank screen
    if len(pred_data) == 0:
        img=Image.new("RGBA", (64,32),(0,0,0)) # mode, size, color
        draw = ImageDraw.Draw(img)
        img.save("Prod_Board_Photo.png")
    # if data is present, print on screen
    else: 
        pred_keys = pred_data[0].keys() 
        pred_df = pd.DataFrame(pred_data, columns = pred_keys) # convert to pd df
        # intialize list
        board_text = []
        # print between 1 and 3 lines depending on number of trains
        lines_avail = pred_df.shape[0]
        if lines_avail < 3:
            lines_to_print = lines_avail
        for i in range(0,lines_to_print):
            # change names based on lookup to fit nicely on the board
            if pred_df['Destination'][i] in list(line_lookup.keys()):
                pred_df['Destination'][i] = line_lookup[pred_df['Destination'][i]]
            # change ARR code to fit on board
            if pred_df['Min'][i] == 'ARR':
                pred_df['Min'][i] = code_lookup[pred_df['Min'][i]]
            # change BRD code to fit on board
            elif pred_df['Min'][i] == 'BRD':
                pred_df['Min'][i] = code_lookup[pred_df['Min'][i]]
            # build text string
            text = pred_df['Line'][i] + '|' + pred_df['Destination'][i]  + '|' + pred_df['Min'][i]
            # retain
            print(text)
            board_text.append(text)
        # create image through PIL
        img=Image.new("RGBA", (64,32),(0,0,0)) # mode, size, color
        draw = ImageDraw.Draw(img) # draw blank image
        draw.text((1, 0), '\n'.join(board_text) ,(255,255,255), font = get_font()) # add text to image
        draw = ImageDraw.Draw(img) # redraw image with text
        img.save("Prod_Board_Photo.png") # save image

    time.sleep(10) # sleep 10 seconds before refresh