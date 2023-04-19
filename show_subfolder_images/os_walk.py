import os
import matplotlib.pyplot as plt
import cv2 as cv
list_file = []

for (root, dirs, files) in os.walk('Data', topdown=True):
    # show file of Data
    for file in dirs:
        print(file)
    # show all of files
    for file in files:
        print(file)
    

    # show images with path
    for name in files:
        print(os.path.join(root, name))
    
    
