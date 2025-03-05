# QR Code Generator - marour13

*Description*

This is a simple web application built with Streamlit that allows users to generate QR codes from URLs. The app provides a user-friendly interface to input a URL, customize the QR code's appearance, and download the generated QR code. It also validates URLs to ensure they are in the correct format before generating the QR code.

*Features*

· User-friendly interface

· URL validation before generating the QR code

· Customizable QR code appearance (color, size, and border)

· Downloadable QR code image

*Requirements*

· To run this application, you need to have Python installed along with the following dependencies:

    pip install streamlit qrcode[pil]

*How to Run*

1. Clone this repository or download the script.

2. Install the required dependencies using the command above.

3. Run the Streamlit app:

    streamlit run qr_generator.py

4. Open the provided local URL in your browser.

*Usage*

1. Enter a valid URL in the input field.

2. Customize the QR code by selecting the colors, size, and border thickness.

3. Click the "Generate the QR Code" button.

4. Once the QR code is generated, you can download it by clicking the "Download the QR" button.

*Notes*

· Ensure the URL is in the correct format (e.g., http:// or https://) for the app to generate the QR code.

· The app saves the generated QR code in a directory called `qr_codes`, and it will automatically download the QR code image when the button is clicked.

*Author*

    marour13
