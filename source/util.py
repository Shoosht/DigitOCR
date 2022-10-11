import streamlit as st
import pytesseract as ts
import numpy as np
import cv2 as cv
from PIL import Image


def centered_title(title):
    st.markdown("<h1 style='text-align: center; color: white;'>" + title + "</h1>", unsafe_allow_html=True)


def centered_text(text):
    st.markdown("<h2 style='text-align: center; color: white;'>" + text + "</h2>", unsafe_allow_html=True)


def load_image(image_file):
	return Image.open(image_file)


def show_image(image):
    st.image(image, use_column_width=True)


def process_image(image, use_blur):
    image = np.array(image)
    image = cv.cvtColor(src=image, code=cv.COLOR_RGB2GRAY)

    if use_blur:
        image = cv.morphologyEx(src=image, op=cv.MORPH_CLOSE, kernel=np.ones((5, 5), np.uint8))
        image = cv.GaussianBlur(src=image, ksize=(5, 5), sigmaX=0, sigmaY=0)

    return Image.fromarray(image.astype(np.uint8))


def draw_boxes(image, boxes, color=(30, 180, 130)):
    height = image.height
    image = cv.cvtColor(np.array(image), cv.COLOR_GRAY2RGB)
    for b in boxes.splitlines():
        b = b.split(' ')
        image = cv.rectangle(image, (int(b[1]), height - int(b[2])), (int(b[3]), height - int(b[4])), color, 2)
    return Image.fromarray(image)


def fix_digits(digit_data):
    return "".join(c for c in digit_data if c in "0123456789")


def read_digits(image, use_blur=False, show_processed=False, config="--psm 13 digits"):
    image = process_image(image, use_blur)

    if show_processed:
        boxes = ts.image_to_boxes(image, config=config)
        show_image(draw_boxes(image, boxes))

    digit_data = ts.image_to_string(image, config=config)
    return fix_digits(digit_data)
