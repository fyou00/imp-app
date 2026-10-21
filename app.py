import numpy as np
import streamlit as st
import cv2

st.title("IMP (Image Processing) App")

st.write("Hello world!")

uploaded_file = st.file_uploader("Please upload an image...", type=["png", "jpg"], max_upload_size=10)

if uploaded_file is not None:
  bytes_data = np.frombuffer(uploaded_file.getvalue(), dtype=np.uint8)  
  
  image = cv2.imdecode(bytes_data, cv2.IMREAD_COLOR)
  image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  
  st.write('input')
  st.image(image_rgb, channels="RGB")

  # feat rgb2gray
  image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)
  
  st.write('output')
  st.image(image_gray)

  # feat button download
  success, encoded_image = cv2.imencode(".png", image_gray)

  if success:
    st.download_button( 
      "Download Image", 
      data=encoded_image.tobytes(),
      file_name="hasil.png",
    )