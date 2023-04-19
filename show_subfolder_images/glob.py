import cv2
import glob
from matplotlib import pyplot as plt

# Load 3 images of folder Data
image_list = []
for filename in glob.glob('./Data/*.jpg'):
    im = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # or im=Image.open(filename)
    image_list.append(im)

first_image = image_list[0]
plt.imshow(first_image)
plt.show()