# ReadOutLoud

ReadOutLoud is a simple web application that converts text from PDF files into speech. This application uses Flask as the web framework, PyPDF2 for extracting text from PDFs, and pyttsx3 for text-to-speech conversion. This tool is particularly useful for users who prefer to listen to text content instead of reading it.

## Features

- Upload PDF files
- Extract text from uploaded PDF files
- Convert extracted text to speech
- Play the speech through the browser

## Requirements

- Python 3.6 or higher
- Flask
- PyPDF2
- pyttsx3
- pyobjc (for macOS users)

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/tradervijeth/ReadOutLoud.git
cd ReadOutLoud
```
### 2. Setup a Virtual Environment 
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Required Packages
```bash
pip install flask pyttsx3 PyPDF2 pyobjc
```
### 4. Create Necessary Directories and Files
```bash
mkdir static templates uploads
touch static/style.css templates/index.html app.py
touch static/favicon.ico  # optional
```

### 5. Run the Application
```bash
python app.py
```
The application will start and open in your default web browser at http://127.0.0.1:5000/.

### Usage
#### 1.Open the web application in your browser.
#### 2.Upload a PDF file using the provided form.
#### 3.Click the "Convert to Audiobook" button.
#### 4.The application will extract text from the PDF and read it aloud.


### File Structure
```bash
ReadOutLoud/
├── app.py                 # Main application file
├── venv/                  # Virtual environment directory
├── static/                # Directory for static files
│   ├── style.css          # CSS file for styling
│   └── favicon.ico        # Favicon file (optional)
├── templates/             # Directory for HTML templates
│   └── index.html         # Main HTML template
└── uploads/               # Directory for uploaded PDF files
```

### Code Explanation
#### app.py
The main application script which sets up the Flask web server, handles file uploads, extracts text from PDFs, and converts the text to speech.

#### templates/index.html
The HTML template for the application's main page. It contains a form for uploading PDF files and displays messages to the user.

#### static/style.css
The CSS file for styling the HTML template.


### Contributing
Contributions are welcome! Please open an issue or submit a pull request on GitHub.


### License
This project is licensed under the MIT License.


