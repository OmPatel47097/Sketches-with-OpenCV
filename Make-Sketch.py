# Description:
# This
# todo complate this project.

# importing OpenCV Library
import cv2

# get the image location and File name
imgLocation = 'E:/Projects/Sketches-with-OpenCV/Source Code/camera.jpg'

# getting the image
img = cv2.imread(imgLocation)

# Make Gray Scale Image
gry_Scale =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# invert image
inverated_img = 255 - gry_Scale

# Blure the image with Gussen Blur
blured_img = cv2.GaussianBlur(inverated_img, (21 , 21), 0)  # todo  ---DONE

# Invert the Blured Image
inverted_blured_img = 255 - blured_img

# creating the pencil sketch img
sketch_img = cv2.divide(gry_Scale,inverted_blured_img, scale= 256.0)

# Printing the image
cv2.imshow('Main Image',img)
cv2.imshow('The Sketch Image',sketch_img)
cv2.waitKey(0)