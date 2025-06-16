#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import qrcode

def generate_qr_code(link, output_file):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code (1 is smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR Code grid
        border=4,  # Border size (minimum is 4 for QR codes)
    )
    # Add data to the QR code
    qr.add_data(link)
    qr.make(fit=True)

    # Create and save the image
    img = qr.make_image(fill_color="#bb1b2b", back_color="white")
    img.save(output_file)
    #print(f"QR Code saved to {output_file}")

# Example usage
link = ""
output_file = "qr_code_datavis.png"

generate_qr_code(link, output_file)


# In[ ]:




