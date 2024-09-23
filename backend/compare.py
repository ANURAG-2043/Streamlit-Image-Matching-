
from PIL import Image
import numpy as np

def compare_images(image1_path, image2_path):
    """Compare two images and return similarity score."""
    img1 = Image.open(image1_path)
    img2 = Image.open(image2_path)

    # Resize images to the same size
    img1 = img1.resize((256, 256))
    img2 = img2.resize((256, 256))

    # Convert images to numpy arrays
    arr1 = np.array(img1)
    arr2 = np.array(img2)

    # Calculate the difference
    diff = np.sum(np.abs(arr1 - arr2))
    similarity = 100 - (diff / (256 * 256 * 3)) * 100  # Simple similarity score

    return similarity
