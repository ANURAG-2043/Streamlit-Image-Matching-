import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.compare import compare_images

if not os.path.exists('images'):
    os.makedirs('images')
    
st.title("Images Comparison using SNN")
st.write("Upload two images")

uploaded_file1 = st.file_uploader("Choose the first image", type=['jpg', 'png', 'bmp'], key="file_uploader1")
uploaded_file2 = st.file_uploader("Choose the second image", type=['jpg', 'png', 'bmp'], key="file_uploader2")  

if st.button("Compare"):
    if uploaded_file1 and uploaded_file2:
        img1_path = os.path.join("images", uploaded_file1.name)
        img2_path = os.path.join("images", uploaded_file2.name)
        
        with open(img1_path, "wb") as f:
            f.write(uploaded_file1.getbuffer())
        with open(img2_path, "wb") as f:
            f.write(uploaded_file2.getbuffer())

        similarity_score = compare_images(img1_path, img2_path)
        
        st.success(f"Similarity Score: {similarity_score:.2f}%")
    else:
        st.error("Please upload two images.")
