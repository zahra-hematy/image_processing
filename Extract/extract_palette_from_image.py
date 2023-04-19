# Import libraries
import csv
import cv2
from PIL import Image
import numpy as np
from scipy.stats import mode
import matplotlib.pyplot as plt
import numpy
import pandas as pd

class Palette:

    """
    This class do the following task for get palette from given image.
    1) get image and convert to 'P' mode
    2) get palette from converted image
    3) display palette ( for dispaly first palette convert to 3D array RGB)
    4) save palette as file csv

    """
    def __init__(self, image_path : str, palette_csv_path : str = "."):  
        self.image_path = image_path
        self.palette_csv_path = palette_csv_path

    # Get Image and convert to P mode
    def get_image(self):
        image = Image.open(self.image_path)
        self.ImageRGB = image.convert("P", palette=Image.ADAPTIVE, colors=256)
        self.ImageRGB_arr = np.array(self.ImageRGB)
        image_mode = self.ImageRGB.mode
        print('Image Mode is : {}, Type Array Image is : {}, Type Image is : {}'.format(image_mode, type(self.ImageRGB_arr),type(self.ImageRGB)))
        return self.ImageRGB

    # Get Image Palette
    def get_palette(self):
        self.palette = self.ImageRGB.getpalette()
        return self.palette

    def display_palette(self):
        # Reshape to array 3D with (n_colors, 1, 3) -> this 3D array represent the RGB values of each color in the palette
        pallet_array = np.reshape(self.palette, (len(self.palette) // 3, 1, 3))
        # Broadcasting palete at new axis
        color_map = np.broadcast_to(pallet_array, (len(self.palette) // 3, 256, 3))
        cv2.imwrite('./Output/nature.jpg', color_map)
        fig, ax = plt.subplots()
        ax.imshow(color_map)
        plt.show()

    # Save palette csv
    def creat_csv_palette(self):
        # Create a list of RGB tuples from the palette
        rgb_values = [(self.palette[i], self.palette[i+1], self.palette[i+2]) for i in range(0, len(self.palette), 3)]
        # Write the RGB values to a CSV file
        with open( self.palette_csv_path,"w", newline='') as csvfile:
            writer = csv.writer(csvfile)   
            writer.writerow(["R","G", "B"])
            writer.writerows(rgb_values)


extract_palette = Palette("./Input/nature.jpg", './Output/nature_paletten.csv')
# extract_palette.get_image()
# extract_palette.get_palette()
# extract_palette.display_palette()
# extract_palette.creat_csv_palette()

exec_methods = ["get_image", "get_palette","display_palette","creat_csv_palette"]
for method in exec_methods:
    getattr(extract_palette, method)()