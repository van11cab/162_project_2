import os
from PIL import Image

N = 20
def calculate_level(Value, min, max):
    level = N * ((Value - min) / (max - min))
    return level

def predicted(min, L, max):
    predicted = min + ((L/N)*(max - min))
    return round(predicted, 2)

def calculatePixelLevels(folderpath, minImage, maxImage):
    imgdirectory = os.listdir(folderpath)
    imgfilepath = folderpath + "/" + imgdirectory[0]
    testImage = Image.open(imgfilepath, 'r')    
    testImage = testImage.convert("RGB")

    width, height = testImage.size

    lvl_imgR = [[0] * height for _ in range(width)]
    lvl_imgG = [[0] * height for _ in range(width)]
    lvl_imgB = [[0] * height for _ in range(width)]

    currmaxpixelmap = maxImage.load()
    currminpixelmap = minImage.load()

    pixel = [0,0,0]
    difference_img_library = []
    rangeshift = 40
    for file in imgdirectory:
        print("enteering ", file)
        imgfilepath = folderpath + "/" + file
        image = Image.open(imgfilepath, 'r')
        image = image.convert("RGB")
        width, height = image.size
        currpixelmap = image.load()
        difference_img = [[pixel] * height for _ in range(width)]
        for x in range(minImage.width):
            for y in range(minImage.height):
                currpixel = currpixelmap[x,y]
                currmax = currmaxpixelmap[x,y]              
                currmin = currminpixelmap[x,y]

                if currpixel[0] >= currmax[0]:
                    R = currmax[0]-rangeshift
                elif currpixel[0] < (currmin[0]+rangeshift):
                    R = currmin[0]
                else:
                    R = currpixel[0]-rangeshift
                
                if currpixel[1] >= currmax[1]:
                    G = currmax[1]-rangeshift
                elif currpixel[1] < currmin[1]+rangeshift:
                    G = currmin[1]
                else:
                    G = currpixel[1]-rangeshift
                
                if currpixel[2] >= currmax[2]:
                    B = currmax[2]-rangeshift
                elif currpixel[2] < currmin[2]+rangeshift:
                    B = currmin[2]
                else:
                    B = currpixel[2]-rangeshift
                                
                if(R < 0):
                    R=0
                elif(R > 255):
                    R = 255
                if(B < 0):
                    B = 0
                elif(B > 255):
                    B = 255
                if(G < 0):
                    G = 0
                elif(G > 255):
                    G = 255
                
                difference_img[x][y] = [R,G,B]

        difference_img_library.append(difference_img)

    return difference_img_library
        