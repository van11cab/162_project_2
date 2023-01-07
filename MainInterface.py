import pickle
import tkinter as tk
import numpy as np
from tkinter import filedialog, Label, Button
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps
import os
import time
from CalculateLevels import calculatePixelLevels
from MinMaxCompression import maxPixelValue, minPixelValue
from ImageDecompressor import decompressImages


imageList = []
imageVariables = []

def clearFrames():
    if displayImageLabel.winfo_children()!=[]:
        for widgets in displayImageLabel.winfo_children():
            widgets.destroy()
    if imageSlider.winfo_children()!=[]:
        for widgets in imageSlider.winfo_children():
            widgets.destroy()

    imageList.clear()
    imageVariables.clear()

def openMinMax():
    print("Image Compression Starting ...")
    start = time.perf_counter()
    
    global minImage, maxImage
    maxImage = maxPixelValue(folderPath)
    # maxImage.show()
    maxImage = ImageOps.mirror(maxImage)
    # maxImage.show()
    maxImage = maxImage.rotate(90, expand = 1)
    # maxImage.show()


    minImage = minPixelValue(folderPath)
    # minImage.show()
    minImage = ImageOps.mirror(minImage)
    # minImage.show()
    minImage = minImage.rotate(90, expand=1)
    # minImage.show()
    
    compresssed_img_lib = calculatePixelLevels(folderPath, minImage, maxImage)
    end = time.perf_counter()
    
    print("Image Compression finished ...")
    print("Elapsed Time: ", end, start)
    imageCompressionTime = end-start
    print("Elapsed time [IMAGE COMPRESION] during the whole program in seconds: ", format((imageCompressionTime), ".2f"), "seconds!")

    
    with open("compressedFile.cmp", "wb") as compressedImage:
        pickle.dump(compresssed_img_lib, compressedImage)

    # print(compresssed_img_lib)
    print("displaying images ...")

    originalImages = os.listdir(folderPath)
    totalSize = 0
    for images in originalImages:
        # print(f"Image: {extractedFolder+images}")
        totalSize += os.path.getsize(f"{folderPath}/{images}")

    originalImageTotalSize = totalSize/1024
    originalImageAverageSize = originalImageTotalSize/len(originalImages)

    print(f"number of Images: {len(originalImages)}")
    print(f"total size of all original images: {originalImageTotalSize} KB")
    print(f"average size of original images: {originalImageAverageSize} KB")

    extractedFolder, imageExtractionTime, extractedImageTotalSize, extractedImageAverageSize = decompressImages("compressedFile.cmp")
    openDialog(imageCompressionTime, imageExtractionTime, originalImageTotalSize, extractedImageTotalSize, originalImageAverageSize, extractedImageAverageSize, extractedFolder)

def openExtractedImages(extractedFolder):
    pop.destroy()
    openExtractedFolder(extractedFolder)



def openDialog(imageCompressionTime, imageExtractionTime, originalImageTotalSize, extractedImageTotalSize, originalImageAverageSize, extractedImageAverageSize, extractedFolder):
    # messagebox.showinfo("test", "test")
    global pop
    pop = tk.Toplevel(mainWindow)
    pop.title("Image Compression Results")
    pop.geometry("600x300")

    compressionRatio = (originalImageTotalSize - extractedImageTotalSize)/(originalImageTotalSize) * 100
    compressionRatio = round(compressionRatio, 3)
    
    popLabel = Label(pop,
    text=
        "Elapsed time [IMAGE COMPRESION]: %s seconds! \n" %(format((imageCompressionTime), ".2f")) +
        "Total size of all [ORIGINAL IMAGE]: %skb \n" %(format((originalImageTotalSize), ".2f")) +
        "Average size of [ORIGINAL IMAGE]: %skb\n\n" %(format((originalImageAverageSize), ".2f")) +
        "Elapsed time [IMAGE EXTRACTION]: %s seconds! \n" %(format((imageExtractionTime), ".2f")) +
        "Total size of all [EXTRACTED IMAGE]: %skb \n" %(format((extractedImageTotalSize), ".2f")) +
        "Average size of [EXTRACTED IMAGE]: %skb\n\n" %(format((extractedImageAverageSize), ".2f")) +
        "Compression Ratio [ORIGINAL/EXTRACTED]: %s\n" %(compressionRatio) +
        "Extracted images saved to: %s" %(extractedFolder)
    )
    popLabel.pack(pady=10)

    showExtractedImagesButton = Button(pop, text="Show Images", command=lambda: openExtractedImages(extractedFolder))
    showExtractedImagesButton.pack()

def openCalculateLevels():
    print("...")    

def openFolder():
    global folderPath
    folderPath = filedialog.askdirectory()
    imageFiles = os.listdir(folderPath)

    clearFrames()

    for i in range(0, len(imageFiles)):
        imageList.append([
            ImageTk.PhotoImage(Image.open(folderPath+'/'+imageFiles[i]).resize((50,50))),
            ImageTk.PhotoImage(Image.open(folderPath+'/'+imageFiles[i])),
        ]),
        imageVariables.append(f"img_{i}")

    for i in range(len(imageVariables)):
        globals()[imageVariables[i]] = tk.Button(imageSlider, image=imageList[i][0], bd=0, command=lambda i=i:displayImage(i))
        globals()[imageVariables[i]].pack(side=tk.LEFT)

def openExtractedFolder(extractedFolder):
    imageFiles = os.listdir(extractedFolder)

    clearFrames()

    for i in range(0, len(imageFiles)):
        imageList.append([
            ImageTk.PhotoImage(Image.open(extractedFolder+imageFiles[i]).resize((50,50))),
            ImageTk.PhotoImage(Image.open(extractedFolder+imageFiles[i])),
        ]),
        imageVariables.append(f"img_{i}")

    for i in range(len(imageVariables)):
        globals()[imageVariables[i]] = tk.Button(imageSlider, image=imageList[i][0], bd=0, command=lambda i=i:displayImage(i))
        globals()[imageVariables[i]].pack(side=tk.LEFT)

    # print("Opening folder ...")

def displayImage(index):
    displayImageLabel.config(image=imageList[index][1])


mainWindow = tk.Tk()
mainWindow.title("CMSC 162 - Final Project")

width = mainWindow.winfo_screenwidth()
height = mainWindow.winfo_screenheight()
# mainWindow.geometry("%dx%d" % (width, height))
mainWindow.geometry("800x600")


mainMenuBar = tk.Menu(mainWindow)
mainWindow.config(menu = mainMenuBar)

fileMenu = tk.Menu(mainMenuBar, tearoff=0)
fileMenu.add_command(label="Open Folder", command=openFolder)
mainMenuBar.add_cascade(label="File", menu=fileMenu)

compressionMenu = tk.Menu(mainMenuBar, tearoff=0)
compressionMenu.add_command(label="Min and Max", command=openMinMax)
compressionMenu.add_command(label="Calculate Levels", command=openCalculateLevels)
mainMenuBar.add_cascade(label="Compression", menu=compressionMenu)

displayImageLabel = tk.Label(mainWindow)
displayImageLabel.pack(anchor=tk.CENTER)

thumbnailCanvas = tk.Canvas(mainWindow, height=60)
thumbnailCanvas.pack(side=tk.BOTTOM, fill=tk.X)

xScrollBar = ttk.Scrollbar(mainWindow, orient=tk.HORIZONTAL)
xScrollBar.pack(side=tk.BOTTOM, fill=tk.X)
xScrollBar.config(command=thumbnailCanvas.xview)

thumbnailCanvas.config(xscrollcommand=xScrollBar.set)
thumbnailCanvas.bind("<Configure>", lambda e: thumbnailCanvas.bbox("all"))

imageSlider = tk.Frame(thumbnailCanvas)
thumbnailCanvas.create_window((0,0), window=imageSlider, anchor=tk.NW)

mainWindow.mainloop()