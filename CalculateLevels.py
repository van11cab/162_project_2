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

                currpixel = currpixelmap[x,y]

                currmax = currmaxpixelmap[x,y]
                currmax0 = currmax[0] -10
                currmax1 = currmax[1] -10
                currmax2 = currmax[2] -10
                currmin = currminpixelmap[x,y]
                currmin0 = currmin[0]
                currmin1= currmin[1]
                currmin2 = currmin[2]
                
                #r
                if currpixel[0] > currmax0:
                    R = currmax0
                elif currpixel[0] < currmin0:
                    R = currmin0
                else:
                    R = currpixel[0]
                
                #g
                if currpixel[1] > currmax1:
                    G = currmax1
                elif currpixel[1] < currmin1:
                    G = currmin1
                else:
                    G = currpixel[1]
                
                #B
                if currpixel[2] > currmax2:
                    B = currmax2
                elif currpixel[2] < currmin2:
                    B = currmin2
                else:
                    B = currpixel[2]
                    
                
                difference_img[x][y] = [ R,G,B]

        difference_img_library.append(difference_img)

    return difference_img_library
        
    

    
                
                


                    

 