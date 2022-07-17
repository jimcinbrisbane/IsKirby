from flask import Flask, render_template, request
from helper import check_upload_file, get_rgb_value, get_path, CipherAES

app = Flask(__name__)
from helper import CipherAES
import cv2
import numpy as np
import random 
#image location, file location
def toRGB(inimg): 
    img = cv2.imread(inimg, cv2.IMREAD_COLOR)
    np.savetxt('foo.txt', img.reshape((3,-1)), fmt="%s", header=str(img.shape))
    
def string_key():
    with open('foo.txt') as f:
        lines = f.readlines()

    return str(lines)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files["fileToUpload"]
        check_upload_file(file)
        old_key = get_rgb_value(get_path(file.filename))
        key = CipherAES.get_hash_sha512(old_key)
        return render_template('key.html', key = key)
    elif request.method == 'GET':
        return render_template('index.html')
          
@app.route('/confirmation', methods=['GET', 'POST'])
def confirmation():
    if request.method == 'POST':
        return render_template('confirmation.html')
    elif request.method == 'GET':
        return render_template('confirmation.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        return render_template('about.html')
    elif request.method == 'GET':
        return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)