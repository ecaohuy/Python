import pytesseract
from PIL import Image

# Set the path to the Tesseract executable
# Replace the path with the path to the Tesseract executable on your system
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/ecaohuy/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

# Open the image using Pillow
image = Image.open(r'C:\Personal\Kieu_passport.jpg')

# Perform OCR on the image
text = pytesseract.image_to_string(image)

# Save the text to a file
with open('output_text.txt', 'w') as text_file:
    text_file.write(text)

print("Text has been successfully written to output_text.txt")
