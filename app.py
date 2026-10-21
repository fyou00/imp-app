import numpy as np
import streamlit as st
import cv2

st.title("IMP (Image Processing) App")

st.write("Hello world!")

# feat rgb2gray
def cv_grayscale(image):
  return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
  
uploaded_file = st.file_uploader("Please upload an image...", type=["png", "jpg"], max_upload_size=10)

if uploaded_file is not None:
  bytes_data = np.frombuffer(uploaded_file.getvalue(), dtype=np.uint8)  
  
  image = cv2.imdecode(bytes_data, cv2.IMREAD_COLOR)
  image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  
  st.write('input')
  st.image(image_rgb, channels="RGB")
 
  result = cv_grayscale(image_rgb)
 
  st.write('output')
  st.image(cv_grayscale(image_rgb))

  # feat button download
  success, encoded_image = cv2.imencode(".png", result)

  if success:
    st.download_button( 
      "Download Image", 
      data=encoded_image.tobytes(),
      file_name="hasil.png",
    )