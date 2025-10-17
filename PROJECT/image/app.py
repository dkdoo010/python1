import streamlit as st
import cv2
import tensorflow as tf
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt 
import google.protobuf


def predict(filt):
    image = np.array(Image.open(file))
    plt.imshow(image)
    plt.axis('off')
    plt.show()

    resnet50=tf.keras.applications.resnet.ResNet50(
    weights='imagenet', input_shape=(224, 224, 3)
    )

    image_resize = cv2.resize(image, (224,224))
    image_reshape = image_resize.reshape([1, 224, 224, 3])

    pred=resnet50.predict(image_reshape)
    decoded_pred = tf.keras.applications.imagenet_utils.decode_predictions(pred)
    return decoded_pred[0]
    # for idx, pred in enumerate(decoded_pred[0]):
    #     print(f'{idx+1}위: {pred[1]}({pred[2] * 100:.2f}%)')

st.title('이미지분류 인공지능 페이지')
file =st.file_uploader('이미지를 올려주세요', type=['jpg', 'png'])
if file:
    # 중앙 정렬을 위한 열 분할
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image(file, caption='', width=150)

    with st.spinner('기다려주세요'):
        preds = predict(file)
        for idx, pred in enumerate(preds):
            st.success(f'{idx+1}위: {pred[1]}({pred[2] * 100:.2f}%)')
