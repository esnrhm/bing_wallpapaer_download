import datetime
import json
import os
from os import path
import time
import requests

drive = 'D:\\'
folder = 'Bing-picture'
# check connection is active
host = "4.2.2.4"
response = os.system("ping -n 1 " + host)

# create directory
# get image url
# and then check the response...
if response == 0:

    # create directory
    directory = os.path.join(drive, folder)
    dirExist = (os.path.isdir(directory))
    if dirExist:
        print("directory is exist")
    else:
        os.mkdir(directory)
        print("create directory")

    res = ''
    while res != 200:
        try:

            # get image url
            # and then check the response...

            headers = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'}
            response = requests.get("https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US",
                                    headers=headers)
            image_data = json.loads(response.text)
            res = response.status_code
            print('response code is ' + str(res))
            image_url = image_data["images"][0]["url"]
            image_url = image_url.split("&")[0]
            full_image_url = "https://www.bing.com" + image_url
            name = image_data["images"][0]["fullstartdate"]
            # image's name
            # image_name = datetime.date.today().strftime("%Y%m%d")
            image_extension = image_url.split(".")[-1]
            image_name = name + "." + image_extension
            a = (path.exists(directory + "\\" + image_name))
            if a:
                print("File exist")
                time.sleep(1)
            else:
                print("File not exist")
                # download and save image
                img_data = requests.get(full_image_url).content
                name = directory + "\\" + image_name
                with open(name, 'wb') as handler:
                    handler.write(img_data)
        except:
            pass
else:
    print("Network Error")
    time.sleep(2)

# ubuntu command to set wallpaper
# os.system("`which gsettings` set org.gnome.desktop.background picture-uri file:$PWD/" + image_name)
