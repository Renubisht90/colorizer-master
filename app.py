#!/usr/bin/env python
# coding: utf-8

import numpy as np
import cv2
import streamlit as st
from PIL import Image

def colorizer(img, prototxt):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    model = r"C:\Users\renu\Documents\Colorizer-master\Colorizer-master\models\colorization_release_v2.caffemodel"
    points = r"C:\Users\renu\Documents\Colorizer-master\Colorizer-master\models\pts_in_hull.npy"
    net = cv2.dnn.readNetFromCaffe(prototxt, model)
    pts = np.load(points)
    class8 = net.getLayerId("class8_ab")
    conv8 = net.getLayerId("conv8_313_rh")
    pts = pts.transpose().reshape(2, 313, 1, 1)
    net.getLayer(class8).blobs = [pts.astype("float32")]
    net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]
    scaled = img.astype("float32") / 255.0
    lab = cv2.cvtColor(scaled, cv2.COLOR_RGB2LAB)
    resized = cv2.resize(lab, (224, 224))
    L = cv2.split(resized)[0]
    L -= 50
    net.setInput(cv2.dnn.blobFromImage(L))
    ab = net.forward()[0, :, :, :].transpose((1, 2, 0))
    ab = cv2.resize(ab, (img.shape[1], img.shape[0]))
    L = cv2.split(lab)[0]
    colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)
    colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2RGB)
    colorized = np.clip(colorized, 0, 1)
    colorized = (255 * colorized).astype("uint8")
    return colorized

st.write("# B&W Image Colorizer")
st.write("Upload your B&W image and watch it come to life in color!")

file = st.sidebar.file_uploader("Upload an image", type=["jpg", "png"])

if file is None:
    st.text("Please upload an image to start!")
else:
    image = Image.open(file)
    img = np.array(image)
    st.text("Original Image")
    st.image(image, use_container_width=True)
    prototxt = r"C:\Users\renu\Documents\Colorizer-master\Colorizer-master\models\models_colorization_deploy_v2.prototxt"
    st.text("Colorized Image")
    color = colorizer(img, prototxt)
    st.image(color, use_container_width=True)
    print("Colorization Done!")
