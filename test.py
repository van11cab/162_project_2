import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

class ImageViewer:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.label = tk.Label(self.frame)
        self.label.pack()

        self.previous_button = tk.Button(self.frame, text="Previous", command=self.previous)
        self.previous_button.pack(side='left')

        self.next_button = tk.Button(self.frame, text="Next", command=self.next)
        self.next_button.pack(side='left')

        self.browse_button = tk.Button(self.frame, text="Browse", command=self.browse)
        self.browse_button.pack(side='left')

        self.folder_path = ''
        self.image_files = []
        self.current_image_index = 0

    def browse(self):
        self.folder_path = filedialog.askdirectory()
        self.image_files = [file for file in os.listdir(self.folder_path) if file.endswith('.jpg')]
        self.current_image_index = 0
        self.display_image()

    def previous(self):
        if not self.image_files:
            return
        self.current_image_index = (self.current_image_index - 1) % len(self.image_files)
        self.display_image()

    def next(self):
        if not self.image_files:
            return
        self.current_image_index = (self.current_image_index + 1) % len(self.image_files)
        self.display_image()

    def display_image(self):
        file_path = os.path.join(self.folder_path, self.image_files[self.current_image_index])
        image = Image.open(file_path)
        image = image.resize((400, 400), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        self.label.config(image=image)
        self.label.image = image

if __name__ == "__main__":
    root = tk.Tk()
    viewer = ImageViewer(root)
    root.mainloop()
