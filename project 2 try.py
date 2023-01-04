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
fwidth = 0
fheight = 0
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
            if(currpixel[1] > max_imgG[x][y]):
                max_imgG[x][y] = currpixel[1]
            #B
            if(currpixel[2] > max_imgB[x][y]):
                max_imgB[x][y] = currpixel[2]


#get the min values of image
#access the folder
imgdirectorry = os.listdir("C:/Users/Van Joseph/Documents/class/162/split images")
for file in imgdirectorry:
    imgfilepath = "C:/Users/Van Joseph/Documents/class/162/split images/" + file

    image = Image.open(imgfilepath, 'r')
    image = image.convert("RGB")
    width, height = image.size
    fwidth, fheight = image.size
    pixelmap = image.load()

    min_imgR = [[255] * height for _ in range(width)]
    min_imgG = [[255] * height for _ in range(width)]
    min_imgB = [[255] * height for _ in range(width)]

    for x in range (0, width):
        for y in range(0, height):
            currpixel = image.getpixel((x,y))

            #R
            if(currpixel[0] < min_imgR[x][y]):
                min_imgR[x][y] = currpixel[0]
            #G
            if(currpixel[1] < min_imgG[x][y]):
                min_imgG[x][y] = currpixel[1]
            #B
            if(currpixel[2] < min_imgB[x][y]):
                min_imgB[x][y] = currpixel[2]

print(height)
print(width)

#lets create an image based on max and min
import numpy as np
import scipy.misc as smp

#create an image size equal to width and height
min_img = np.zeros((fwidth, fheight, 3), dtype = np.uint8)
max_img = np.zeros((fwidth, fheight, 3), dtype = np.uint8)

for x in range(0, fwidth):
    for y in range(0, fheight):
        holder= [min_imgR[x][y], min_imgG[x][y], min_imgB[x][y]]
        min_img[x,y] = holder

        holder= [max_imgR[x][y], max_imgG[x][y], max_imgB[x][y]]
        max_img[x,y] = holder

final_min = Image.fromarray(min_img)
final_max = Image.fromarray(max_img)
final_min.show()
final_max.show()
print("finih")


            


