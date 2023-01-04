import os

#print('Get current directory:', os.path.dirname(__file__))
path = os.path.dirname(__file__)

#print('Get contents of directory', os.listdir(path))
directory = os.listdir(path)
#print(type(directory))

filepath = path + "\\" + directory[0]
#print("filepath of 1st file", filepath)


#print('Get contents of directory', imgdirectorry)


from PIL import Image, ImageTk
from tkinter import Label, LabelFrame
import numpy as np


#get the max values of image
#access the folder
imgdirectorry = os.listdir("C:/Users/Van Joseph/Documents/class/162/split images")
for file in imgdirectorry:
    imgfilepath = "C:/Users/Van Joseph/Documents/class/162/split images/" + file

    image = Image.open(imgfilepath, 'r')
    image = image.convert("RGB")
    width, height = image.size
    pixelmap = image.load()

    max_imgR = [[0] * height for _ in range(width)]
    max_imgG = [[0] * height for _ in range(width)]
    max_imgB = [[0] * height for _ in range(width)]

    for x in range (0, width):
        for y in range(0, height):
            

            currpixel = image.getpixel((x,y))

            #R
            if(currpixel[0] > max_imgR[x][y]):
                max_imgR[x][y] = currpixel[0]
            #G
            if(currpixel[1] > max_imgR[x][y]):
                max_imgG[x][y] = currpixel[1]
            #B
            if(currpixel[2] > max_imgR[x][y]):
                max_imgB[x][y] = currpixel[2]


#get the min values of image
#access the folder
imgdirectorry = os.listdir("C:/Users/Van Joseph/Documents/class/162/split images")
for file in imgdirectorry:
    imgfilepath = "C:/Users/Van Joseph/Documents/class/162/split images/" + file

    image = Image.open(imgfilepath, 'r')
    image = image.convert("RGB")
    width, height = image.size
    pixelmap = image.load()

    min_imgR = [[255] * height for _ in range(width)]
    min_imgG = [[255] * height for _ in range(width)]
    min_imgB = [[255] * height for _ in range(width)]

    for x in range (0, width):
        for y in range(0, height):
            currpixel = image.getpixel((x,y))

            #R
            if(currpixel[0] < min_imgR[x][y]):
                max_imgR[x][y] = currpixel[0]
            #G
            if(currpixel[1] < min_imgR[x][y]):
                max_imgG[x][y] = currpixel[1]
            #B
            if(currpixel[2] < min_imgR[x][y]):
                max_imgB[x][y] = currpixel[2]

print("finih")
            


