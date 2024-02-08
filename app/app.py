from flask import Flask, request, jsonify, send_file
from flask_cors import CORS 
from PIL import Image
import pytesseract
import re

app = Flask(__name__)
CORS(app)

def parse_driver_license(text):
    # Regular expressions to match patterns in the DL text
    name_pattern = r"([A-Z]+(?: [A-Z]+)*)+"
    address_pattern = r"(\d+\s+[A-Z]+\s+[A-Z]+\s+\d+\s+[A-Z]+(?:,\s+[A-Z]+)*\s+\d{5})"
    date_pattern = r"(\d{2}/\d{2}/\d{4})"

    # Extracting full name
    full_name_match = re.search(name_pattern, text)
    full_name = full_name_match.group(1) if full_name_match else None

    # Extracting address
    address_match = re.search(address_pattern, text)
    address = address_match.group(0) if address_match else None

    # Extracting issuance and expiration dates
    date_matches = re.findall(date_pattern, text)
    issuance_date = date_matches[1] if date_matches else None
    expiration_date = date_matches[-1] if date_matches else None

    return {
        "full_name": full_name,
        "address": address,
        "issuance_date": issuance_date,
        "expiration_date": expiration_date
    }

def process_image(image):
    # Preprocess the image (resize, enhance)
    image = image.resize((800, 600))  # Resize to improve OCR accuracy
    # Enhance the image as needed
    
    # Use OCR to extract text
    text = pytesseract.image_to_string(image)
    return text

# Route to serve the index.html file
@app.route('/')
def serve_index():
    return send_file('index.html')

# Route for handling image extraction
@app.route('/extract', methods=['POST'])
def extract_data():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image = request.files['image']
    if image.filename == '':
        return jsonify({'error': 'No image selected'}), 400

    try:
        # Open the image using PIL
        img = Image.open(image)
        extracted_text = process_image(img)

        # Parse the extracted text to get relevant fields
        parsed_text = parse_driver_license(extracted_text)

        # Option - validate and store the extracted data in a database

        return jsonify({'data': parsed_text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)