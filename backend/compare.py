
from PIL import Image
import numpy as np
import cv2
from keras.models import load_model
import os

def compare_images(image1_path, image2_path):
    """Compare two images and return similarity score."""
    
    imgs = np.empty((2, 96, 96), dtype = np.uint8)
    img = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (96, 96)).astype(np.float32) / 255.
    imgs[0] = img
    
    img = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (96, 96)).astype(np.float32) / 255.
    imgs[1] = img
    
    rx1 = imgs[0].reshape((1, 96, 96)).astype(np.float32) / 255.
    rx2 = imgs[1].reshape((1, 96, 96)).astype(np.float32) / 255.

    # Calculate the difference
    model = load_model(r"C:\Users\omgha\OneDrive\Documents\GitHub\Streamlit-Image-Matching-\backend\FpM_Model_1.h5")
    similarity  = model.predict([rx1, rx2])

    return similarity
