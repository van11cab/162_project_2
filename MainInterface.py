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

def clearFrames(): #Function responsible for clearing the label frame responsible for clearing the widgets and texts from the User interface
    if displayImageLabel.winfo_children()!=[]:
        for widgets in displayImageLabel.winfo_children():
            widgets.destroy()
    if imageSlider.winfo_children()!=[]:
        for widgets in imageSlider.winfo_children():
            widgets.destroy()
    informationLabel.configure(text="")
    imageList.clear()
    imageVariables.clear()

def modifiedClearFrames(): #modified version of the clearFrames() that utilizes the same function but catered specficially for openExtractedFolder()
    if displayImageLabel.winfo_children()!=[]:
        for widgets in displayImageLabel.winfo_children():
            widgets.destroy()
    if imageSlider.winfo_children()!=[]:
        for widgets in imageSlider.winfo_children():
            widgets.destroy()
    imageList.clear()
    imageVariables.clear()

def openMinMax(): #Function which is responsible for the entire compression process -- it holds for the transformation of images as well its extraction
    print("Image Compression Starting ...")
    start = time.perf_counter()
    
    #lines 44-51: minPixelValue and maxPixelValue are called to identify the maximum and mininum values of each pixels' varying on every sequence of images inside the argument folder
    global minImage, maxImage
    maxImage = maxPixelValue(folderPath)
    maxImage = ImageOps.mirror(maxImage)
    maxImage = maxImage.rotate(90, expand = 1)

    minImage = minPixelValue(folderPath)
    minImage = ImageOps.mirror(minImage)
    minImage = minImage.rotate(90, expand=1)

    #after the minImage and maxImage are identified, the sequence of images are then passed to the calculatePixelLevel which returns a concatenated single file with all the compressed images
    compresssed_img_lib = calculatePixelLevels(folderPath, minImage, maxImage)
    end = time.perf_counter()
    
    imageCompressionTime = end-start
    
    #generation of the single-file containing the images
    with open("compressedFile.cmp", "wb") as compressedImage:
        pickle.dump(compresssed_img_lib, compressedImage)

    #lines 63-74: calculates for the size of images in the argument folder containing the original images
    originalImages = os.listdir(folderPath)
    totalSize = 0
    for images in originalImages:
        totalSize += os.path.getsize(f"{folderPath}/{images}")

    originalImageTotalSize = totalSize/1024
    originalImageAverageSize = originalImageTotalSize/len(originalImages)

    extractedFolder, imageExtractionTime, extractedImageTotalSize, extractedImageAverageSize = decompressImages("compressedFile.cmp")
    compressionRatio = (originalImageTotalSize - extractedImageTotalSize)/(originalImageTotalSize) * 100
    compressionRatio = round(compressionRatio, 3)

    #line 77-89: openDialog presents the information necessary about the Image compression process. It includes the overall running time, the original and compressed sizes, and the compression ratio
    openDialog(imageCompressionTime, imageExtractionTime, originalImageTotalSize, extractedImageTotalSize, originalImageAverageSize, extractedImageAverageSize, extractedFolder, compressionRatio)

    informationLabel.configure(
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

def openExtractedImages(extractedFolder): #Helper function for the dialog which displays the information about Image compression
    pop.destroy()
    openExtractedFolder(extractedFolder)

#line 96-116: openDialog displays the information about the entire Image compression process
def openDialog(imageCompressionTime, imageExtractionTime, originalImageTotalSize, extractedImageTotalSize, originalImageAverageSize, extractedImageAverageSize, extractedFolder, compressionRatio):
    global pop
    pop = tk.Toplevel(mainWindow)
    pop.title("Image Compression Results")
    pop.geometry("600x300")
    
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

def openFolder(): #Helper function that asks the user for the argument folder containing the original sequence of images
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

def openExtractedFolder(extractedFolder): #modified openFolder function that displays the compressed images after the compression
    imageFiles = os.listdir(extractedFolder)

    modifiedClearFrames()

    for i in range(0, len(imageFiles)):
        imageList.append([
            ImageTk.PhotoImage(Image.open(extractedFolder+imageFiles[i]).resize((50,50))),
            ImageTk.PhotoImage(Image.open(extractedFolder+imageFiles[i])),
        ]),
        imageVariables.append(f"img_{i}")

    for i in range(len(imageVariables)):
        globals()[imageVariables[i]] = tk.Button(imageSlider, image=imageList[i][0], bd=0, command=lambda i=i:displayImage(i))
        globals()[imageVariables[i]].pack(side=tk.LEFT)

    displayImage(0)

def displayImage(index): #displays the image on the user-interface
    displayImageLabel.config(image=imageList[index][1])

#line 158-196: TKINTER codes for the user-interface
mainWindow = tk.Tk()
mainWindow.title("CMSC 162 - Final Project")

width = mainWindow.winfo_screenwidth()
height = mainWindow.winfo_screenheight()
mainWindow.geometry("1000x800")


mainMenuBar = tk.Menu(mainWindow)
mainWindow.config(menu = mainMenuBar)

fileMenu = tk.Menu(mainMenuBar, tearoff=0)
fileMenu.add_command(label="Open Folder", command=openFolder)
mainMenuBar.add_cascade(label="File", menu=fileMenu)

compressionMenu = tk.Menu(mainMenuBar, tearoff=0)
compressionMenu.add_command(label="Min and Max Compression", command=openMinMax)
mainMenuBar.add_cascade(label="Compression", menu=compressionMenu)

displayImageLabel = tk.Label(mainWindow)
displayImageLabel.pack(anchor=tk.CENTER)

informationLabel = tk.Label(mainWindow)
informationLabel.pack(pady=10)

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