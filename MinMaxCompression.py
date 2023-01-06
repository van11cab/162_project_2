import os
import numpy as np
from PIL import Image, ImageTk

def maxPixelValue(folderpath):

    imgdirectory = os.listdir(folderpath)
    imgfilepath = folderpath + "/" + imgdirectory[0]
    testImage = Image.open(imgfilepath, 'r')    
    # testImage = Image.open(folderpath + directory[0], 'r')
    testImage = testImage.convert("RGB")
    # width, height = testImage.size
    width, height = testImage.size

    max_imgR = [[0] * height for _ in range(width)]
    max_imgG = [[0] * height for _ in range(width)]
    max_imgB = [[0] * height for _ in range(width)]

    for file in imgdirectory:
        imgfilepath = folderpath + "/" +file
        image = Image.open(imgfilepath, 'r')
        image = image.convert("RGB")
        width, height = image.size
        print(file)

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

    max_img = np.zeros((width, height, 3), dtype = np.uint8)

    for x in range(0, width):
        for y in range(0, height):
            holder= [max_imgR[x][y], max_imgG[x][y], max_imgB[x][y]]
            max_img[x,y] = holder

    final_max = Image.fromarray(max_img)
    # final_max.show()
    return final_max

def minPixelValue(folderpath):
    imgdirectory = os.listdir(folderpath)
    imgfilepath = folderpath + "/" + imgdirectory[0]
    testImage = Image.open(imgfilepath, 'r')    
    # testImage = Image.open(folderpath + directory[0], 'r')
    testImage = testImage.convert("RGB")
    # width, height = testImage.size
    width, height = testImage.size

    min_imgR = [[255] * height for _ in range(width)]
    min_imgG = [[255] * height for _ in range(width)]
    min_imgB = [[255] * height for _ in range(width)]

    for file in imgdirectory:
        imgfilepath = folderpath + "/" +file
        image = Image.open(imgfilepath, 'r')
        image = image.convert("RGB")
        width, height = image.size
        print(file)

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

    min_img = np.zeros((width, height, 3), dtype = np.uint8)

    for x in range(0, width):
        for y in range(0, height):
            holder= [min_imgR[x][y], min_imgG[x][y], min_imgB[x][y]]
            min_img[x,y] = holder

    final_min = Image.fromarray(min_img)
    # final_min.show()
    return final_min
    print("...")
