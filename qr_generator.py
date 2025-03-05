import qrcode
import streamlit as st
import os  # To handle directory creation
from urllib.parse import urlparse

# Function to validate URL
def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])  # Ensures it has a scheme (http, https) and a domain
    except ValueError:
        return False

# Function to generate QR code
def generate_qr_code(url, filename, fill_color="black", back_color="white", box_size=10, border=4):
    # Ensure the 'qr_codes' directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(filename)

# Page configuration
st.set_page_config(page_title="QR CODES GENERATOR", page_icon="🌐", layout="centered")
st.image("qr_title.png", use_container_width=True)

# URL input
url = st.text_input("Enter the URL to generate the QR code:")

# Customizable color and size
fill_color = st.color_picker("Select the QR code color", value="#000000")
back_color = st.color_picker("Select the background color", value="#ffffff")
box_size = st.slider("QR box size", min_value=5, max_value=20, value=10)
border = st.slider("QR border thickness", min_value=1, max_value=10, value=4)

# Check if the URL is valid and generate the QR code
if st.button("Generate the QR Code"):
    if not url:
        st.warning("Please, enter a valid URL.")
    elif not is_valid_url(url):
        st.error("The entered URL is not valid. Make sure it has the correct format (e.g., http://).")
    else:
        # Directory for the QR image
        filename = "qr_codes/qr_code.png"
        
        # Generate and save the QR code
        generate_qr_code(url, filename, fill_color, back_color, box_size, border)
        
        st.image(filename, use_container_width=True)
        
        # Download the generated QR code
        with open(filename, "rb") as f:
            image_data = f.read()
        st.download_button(label="Download the QR", data=image_data, file_name="generated_qr.png", mime="image/png")

#streamlit run qr_generator.py
