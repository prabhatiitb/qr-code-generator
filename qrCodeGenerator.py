# import sys
# print(sys.executable)
# print(sys.version)

# import qrcode
# from PIL import Image, ImageDraw
# url=input("Enter the url here: ").strip()
# filename=input("Enter FileName: ").strip()

# qr = qrcode.QRCode(box_size='10',border='4')
# qr.add_data(url)
# image= qr.make_image(fill_color='black',back_color='white')
# image.save(f'{filename}.jpg')
# print("Image saved!")

import qrcode
from PIL import Image
import streamlit as st

st.title("QR Code Generator")

url = st.text_input("Enter the URL:")
filename = st.text_input("Enter filename (without extension):")

if st.button("Generate QR Code"):
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(url)
    image = qr.make_image(fill_color='black', back_color='white')
    image.save(f"{filename}.jpg")
    st.success(f"{filename}.jpg saved!")
    st.image(f"{filename}.jpg")