
from PIL import Image
import numpy as np
import tensorflow as tf
import os
import cv2
from keras.models import load_model


def compare_images(image1_path, image2_path):
    """Compare two images and return similarity score."""
    #img1 = Image.open(image1_path)
    #img2 = Image.open(image2_path)

    imgs = np.empty((2, 96, 96), dtype = np.uint8)
    labels = np.empty( (2, 4), dtype= np.uint16)
    # Resize images to the same size
    img = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (96, 96))
    imgs[0] = img
    # Extracting labels from the filename
    #labels[0] = extract_label_real(image1_path)
    
    
    img = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (96, 96))
    imgs[1] = img
    # Extracting labels from the filename
    #labels[1] = extract_label_real(image2_path)
    
    # Convert images to numpy arrays
    #arr1 = np.array(img1)
    #arr2 = np.array(img2)

    model = load_model(r'C:\Users\omgha\OneDrive\Documents\GitHub\FingerPrintMatchingSNN\FpM_Model_1.h5')
    
    matching_score = model.predict([imgs[0], imgs[1]])

    return matching_score
