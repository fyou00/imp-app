import numpy as np
import streamlit as st
import cv2

st.title("IMP (Image Processing) App")

st.write("Hello world!")

# feat adjust image preview
def resize_keep_aspect(img, target_width=None, target_height=None):
  h, w = img.shape[:2]
  
  if target_width is None and target_height is None:
    return img
  
  if target_width is not None:
    ratio = target_width / float(w)
    dim = (target_width, int(h * ratio))
  else:
    ratio = target_height / float(h)
    dim = (int(w * ratio), target_height)
  
  return cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

# feat rgb2gray
def cv_grayscale(img):
  return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
  
uploaded_file = st.file_uploader("Please upload an image...", type=["png", "jpg"], max_upload_size=10)

if uploaded_file is not None:
  bytes_data = np.frombuffer(uploaded_file.getvalue(), dtype=np.uint8)  
  
  image = cv2.imdecode(bytes_data, cv2.IMREAD_COLOR_RGB)
  
  st.write('input')
  st.image(resize_keep_aspect(image, 400))
 
  result = cv_grayscale(image)
 
  st.write('output')
  st.image(resize_keep_aspect(result, 400))

  # feat button download
  success, encoded_image = cv2.imencode(".png", result)

  if success:
    st.download_button( 
      "Download Image", 
      data=encoded_image.tobytes(),
      file_name="hasil.png",
    )