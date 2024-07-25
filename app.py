from flask import Flask, render_template, request, redirect, url_for, flash
from gtts import gTTS
from PyPDF2 import PdfReader
import os
import webbrowser
from threading import Timer
import subprocess

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necessary for flash messages

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def extract_text_from_pdf(file_path):
    print(f"Extracting text from: {file_path}")
    pdfreader = PdfReader(file_path)
    text = ""
    for page in pdfreader.pages:
        text += page.extract_text()
    return text

def read_text_aloud(text):
    print("Reading text aloud...")
    tts = gTTS(text)
    tts.save("output.mp3")

    # Use afplay to play the mp3 file on macOS
    subprocess.run(["afplay", "output.mp3"])

    os.remove("output.mp3")

@app.route('/', methods=['GET', 'POST'])
def index():
    print("Rendering index page")
    if request.method == 'POST':
        print("Received POST request")
        if 'file' not in request.files:
            flash('No file part')
            print("No file part")
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            print("No selected file")
            return redirect(request.url)
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            text = extract_text_from_pdf(file_path)
            if text.strip():
                read_text_aloud(text)
                flash('File successfully processed and read out loud!')
            else:
                flash('No text found in the PDF file.')
            return redirect(url_for('index'))
    return render_template('index.html')

def open_browser():
    print("Opening browser...")
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    print("Starting Flask app...")
    Timer(1, open_browser).start()
    app.run(debug=True)
