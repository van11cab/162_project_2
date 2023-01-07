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
    #hold image directory
    imgdirectory = os.listdir(folderpath)
    imgfilepath = folderpath + "/" + imgdirectory[0]
    testImage = Image.open(imgfilepath, 'r')    
    # testImage = Image.open(folderpath + directory[0], 'r')
    testImage = testImage.convert("RGB")

    # width, height = testImage.size
    width, height = testImage.size
    print(type(minImage))
    print(type(testImage))
    #2d array that holds the levels of an image
    lvl_imgR = [[0] * height for _ in range(width)]
    lvl_imgG = [[0] * height for _ in range(width)]
    lvl_imgB = [[0] * height for _ in range(width)]
    currmaxpixelmap = maxImage.load()
    currminpixelmap = minImage.load()
    #create 2d array na maghold sa 3 values (mao na ni ang differences sa pictures nato)
    pixel = [0,0,0]
    difference_img_library = []
    rangeshift = 20
    for file in imgdirectory:
        print("enteering ", file)
        imgfilepath = folderpath + "/" + file
        image = Image.open(imgfilepath, 'r')
        image = image.convert("RGB")
        width, height = image.size
        currpixelmap = image.load()
        difference_img = [[pixel] * height for _ in range(width)]
        # for y in range(minImage.height): #original
        #     for x in range(minImage.width):
        for x in range(minImage.width): #testing purposes
            for y in range(minImage.height):
                #take the current pixel of max, min, and current image
                #unedited pixel value
                currpixel = currpixelmap[x,y]

                currmax = currmaxpixelmap[x,y]
                
                currmin = currminpixelmap[x,y]
                #r
                if currpixel[0] > currmax[0]:
                    R = currmax[0]-rangeshift
                elif currpixel[0] < (currmin[0]+rangeshift):
                    R = currmin[0]
                else:
                    R = currpixel[0]-rangeshift
                
                #g
                if currpixel[1] > currmax[1]:
                    G = currmax[1]-rangeshift
                elif currpixel[1] < currmin[1]+rangeshift:
                    G = currmin[1]
                else:
                    G = currpixel[1]-rangeshift
                
                #B
                if currpixel[2] > currmax[2]:
                    B = currmax[2]-rangeshift
                elif currpixel[2] < currmin[2]+rangeshift:
                    B = currmin[2]
                else:
                    B = currpixel[2]-rangeshift

                
                difference_img[x][y] = [R,G,B]

        difference_img_library.append(difference_img)

    return difference_img_library
        