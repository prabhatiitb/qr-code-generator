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

import streamlit as st
import qrcode
from PIL import Image
import io

st.title("QR Code Generator")

url = st.text_input("Enter the URL")

if st.button("Generate QR Code") and url:
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Convert to in-memory bytes
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)

    st.image(buf, caption="Generated QR Code")