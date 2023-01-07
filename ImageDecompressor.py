import pickle
from PIL import Image, ImageOps
import numpy as np
import os
import time

def decompressImages(compressedFile):
    print("Image Extraction Starting ...")
    start = time.perf_counter()

    extractedFolder = "./extractedImages/"
    if not os.path.exists(extractedFolder):
        os.mkdir(extractedFolder)

    for fileName in os.listdir(extractedFolder):
        file = extractedFolder + fileName
        if os.path.isfile(file):
            os.remove(file) 

    with open(compressedFile, "rb") as file:
        compressedImage = pickle.load(file)

    # with open("content.txt", "w") as n:
    #     compre

    # print(compressedImage[0])
    # testingImage = Image.fromarray(compressedImage[0])
    # testingImage.show()

    # for i in range(len(compressedImage)):
    #     testArray = compressedImage[i]
    #     testArray = np.array(testArray)
    #     testImage = Image.fromarray((testArray*255).astype(np.uint8))

    #     testImage.save(f"{extractedFolder}extractedImage-{i}", "JPEG")

    for i in range(len(compressedImage)):
        imageWidth = len(compressedImage[0])
        imageHeight = len(compressedImage[0][0])
        blankRGBImage = np.zeros((imageWidth, imageHeight, 3), np.uint8)
        for x in range(imageWidth):
            for y in range(imageHeight):
                blankRGBImage[x][y] = (compressedImage[i][x][y][0], compressedImage[i][x][y][1], compressedImage[i][x][y][2])
        
        extractedImage = Image.fromarray(blankRGBImage)
        extractedImage = ImageOps.mirror(extractedImage)
        extractedImage = extractedImage.rotate(90, expand=1)
        extractedImage.save(f"{extractedFolder}extractedImage-{i}", "JPEG")
        # print(f"extractedImage-{i} generated ...")

    end = time.perf_counter()
    print(f"ALL IMAGES SUCCESSFULLY EXTRACTED!!")


    print("Image Extraction finished ...")
    print("Elapsed Time: ", end, start)
    imageExtractionTime = end-start
    print("Elapsed time [IMAGE EXTRACTION] during the whole program in seconds: ", format((imageExtractionTime), ".2f"), "seconds!")

    extractedImages = os.listdir(extractedFolder)
    totalSize = 0
    for images in extractedImages:
        # print(f"Image: {extractedFolder+images}")
        totalSize += os.path.getsize(f"{extractedFolder+images}")

    extractedImageTotalSize = totalSize/1024
    extractedImageAverageSize = extractedImageTotalSize/len(extractedImages)

    print(f"total size of all extracted images: {extractedImageTotalSize} KB")
    print(f"average size of extracted images: {extractedImageAverageSize} KB")

    return extractedFolder, imageExtractionTime, extractedImageTotalSize, extractedImageAverageSize

