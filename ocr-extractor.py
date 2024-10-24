import pytesseract
from PIL import Image
import os

# Set the path for the Tesseract executable
# Update the path below if Tesseract is not in your PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path: str) -> str:
    """
    Extracts text from the given image file using OCR.

    :param image_path: Path to the image file
    :return: Extracted text as a string
    """
    try:
        with Image.open(image_path) as img:
            text = pytesseract.image_to_string(img)
            return text
    except Exception as e:
        print(f"Error processing file {image_path}: {e}")
        return ""

def main():
    image_directory = 'images'  # Change this to your image directory

    for filename in os.listdir(image_directory):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(image_directory, filename)
            print(f"Processing {image_path}...")
            extracted_text = extract_text_from_image(image_path)
            print(f"Extracted Text from {filename}:\n{extracted_text}\n")

if __name__ == "__main__":
    main()
