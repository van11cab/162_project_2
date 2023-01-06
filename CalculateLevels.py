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
                currmin = currminpixelmap[x,y]
                #need to calculate levels of an image
                
                
                #if x or y-axis is 0, meaning the first row/ column, manually calculate the levels
                if (x == 0 or y == 0):
                    #for each color, if max and min are equal, assume 0
                    #r
                    if(currmax[0] == currmin[0]):
                        lvl_imgR[x][y]= 0
                    else:
                        #calculate level of R
                        print("entered else")
                        lvl_imgR[x][y] = calculate_level(currpixel[0], currmin[0], currmax[0])
                        
                    
                    #g
                    if(currmax[1] == currmin[1]):
                        lvl_imgG[x][y]= 0
                    else:
                        #calculate level of G
                        print("entered")
                        lvl_imgG[x][y] = calculate_level(currpixel[1], currmin[1], currmax[1])
                    
                    #b
                    if(currmax[2] == currmin[2]):
                        lvl_imgB[x][y]= 0
                    else:
                        #calculate level of B
                        print("entered")
                        lvl_imgB[x][y] = calculate_level(currpixel[2], currmin[2], currmax[2])
                else:
                    #calculate via mmp2
                    #R
                    lvl_imgR[x][y]=  (lvl_imgR[x][y-1] +  lvl_imgR[x-1][y]) /2
                    #G
                    lvl_imgG[x][y]=  (lvl_imgG[x][y-1] +  lvl_imgG[x-1][y]) /2
                    #B
                    lvl_imgB[x][y]=  (lvl_imgB[x][y-1] +  lvl_imgB[x-1][y])/2

                #given the levels, calculate the predictive value
                #R
                predicted_R = predicted(currmin[0], lvl_imgR[x][y], currmax[0])
                #G
                predicted_G = predicted(currmin[1], lvl_imgG[x][y], currmax[1])
                #B
                predicted_B = predicted(currmin[2], lvl_imgB[x][y], currmax[2])

                #save the predicted values to the difference image
                difference_img[x][y] = [currpixel[0] - predicted_R, currpixel[1] - predicted_G, currpixel[2] - predicted_B]


        
        difference_img_library.append(difference_img)

    return difference_img_library
        
    

    
                
                


                    

 