import os
import tempfile
import subprocess as sp
from werkzeug.utils import secure_filename
from flask import Flask, request, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return 'Welcome to chanmo/tesseract'

@app.route("/ocr", methods=['POST'])
def ocr():
    if 'file' not in request.files:
        return {
            'success': False,
            'message': 'file is required.'
        }

    file = request.files['file']
    with tempfile.NamedTemporaryFile() as infile:
        file.save(infile.name)
        res = sp.run(['tesseract', infile.name, '-', '-l', 'eng+chi_sim'], capture_output=True, check=True)

    return res.stdout
