# Driver's License Scanner Project

[View the live deployed project here.](https://crispina.pythonanywhere.com/)

This project is a web application designed to scan and extract information from driver's licenses using a camera. The extracted data includes the full name, address, issuance date, and expiration date from the driver's license image. The architecture involves a Flask backend server and an HTML front-end interface.

## Project Architecture

The project consists of two main components:

1. **Frontend (HTML/CSS/JS):**
   - The HTML file (`index.html`) provides the user interface for capturing images from the device camera.
   - It includes elements such as a video element for displaying the camera feed, a capture button to take a snapshot, and a div for displaying the extracted data.

2. **Backend (Flask):**
   - The Flask application (`app.py`) serves as the backend server.
   - It utilizes the `flask_cors` extension for enabling Cross-Origin Resource Sharing (CORS).
   - The backend includes routes for serving the HTML file and handling image extraction.
   - Image processing is performed using the `PIL` (Python Imaging Library) and optical character recognition (OCR) using `pytesseract`.
   - Extracted text from the image is parsed using regular expressions to retrieve relevant information.

## Technologies Used

- **Flask:** Flask is a micro web framework for building web applications in Python.
- **HTML:** HTML is used for creating the user interface elements.
- **JavaScript:** JavaScript is used to interact with the DOM and handle user actions (e.g., capturing images).
- **PIL (Python Imaging Library):** PIL is used for image processing tasks such as resizing and enhancing images.
- **pytesseract:** pytesseract is a Python wrapper for Google's Tesseract-OCR Engine, used for optical character recognition.
- **Regular Expressions:** Regular expressions are used for pattern matching to extract specific information from the extracted text.

## Obstacles and Assumptions

During development, some obstacles and assumptions were encountered:

- **Error Handling:** Error handling is implemented to handle cases such as no image uploaded, no image selected, and general exceptions during image processing.
- **Image Preprocessing:** An image preprocessing technique such as resizing has been added to improve OCR accuracy.
- **CORS:** Cross-Origin Resource Sharing (CORS) is enabled to allow communication between the frontend and backend, assuming they are hosted on different domains.
- **Camera Access:** The project assumes that the device has a camera accessible via the `navigator.mediaDevices.getUserMedia` API in the browser.
- **Camera and Picture Quality:** The backend assumes that the camera and user ability to take a steady picture of their ID is optimal. Meaning the picutre is well lit and the user did not shake at all when taking the picture. This is relying on many factors that are outside of the ability of the program to extract correct data. An obstacle here is that if the data is not readable the API returns null values.
- **License:** The project uses open-source libraries and does not impose any specific license restrictions. However, it's essential to check the licenses of dependencies used in the project.

## Usage

1. Clone the repository.
2. Install the required dependencies:
    ```
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
4. Run the Flask application using `python3 app.py`.
5. Access the application in a web browser at `http://127.0.0.1:5000/`.

## Conclusion

The Driver's License Scanner project provides a simple yet effective solution for extracting information from driver's licenses using a web-based interface. By leveraging Flask for the backend and HTML/JavaScript for the frontend, along with image processing and OCR libraries, the application offers a seamless user experience for capturing and processing driver's license images.
