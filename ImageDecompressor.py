import pickle
from PIL import Image
import numpy as np
import os

def decompressImages(compressedFile):
    extractedFolder = "./extractedImages/"
    if not os.path.exists(extractedFolder):
        os.mkdir(extractedFolder)

    with open(compressedFile, "rb") as file:
        compressedImage = pickle.load(file)

    # with open("content.txt", "w") as n:
    #     compre

    # print(compressedImage[0])
    # testingImage = Image.fromarray(compressedImage[0])
    # testingImage.show()

    for i in range(len(compressedImage)):
        testArray = compressedImage[i]
        testArray = np.array(testArray)
        testImage = Image.fromarray((testArray*255).astype(np.uint8))

        testImage.save(f"{extractedFolder}extractedImage-{i}", "JPEG")

    # for i in range(len(compressedImage)):
    #     imageWidth = len(compressedImage[0])
    #     imageHeight = len(compressedImage[0][0])
    #     blankRGBImage = np.zeros((imageWidth, imageHeight, 3), np.uint8)
    #     for x in range(imageWidth):
    #         for y in range(imageHeight):
    #             blankRGBImage[x][y] = (compressedImage[i][x][y][0], compressedImage[i][x][y][1], compressedImage[i][x][y][2])
        
    #     extractedImage = 