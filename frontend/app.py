from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from pathlib import Path
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files["fileToUpload"]
        path = check_upload_file(file)
        return render_template('index.html')
    elif request.method == 'GET':
        return render_template('index.html')

def check_upload_file(file):
          # get file data from form
          fp = file
          filename= fp.filename
          # get the current path of the module file... store file relative to this path
          BASE_DIR = Path(__file__).resolve().parent
          #uploadfilelocation – directory of this file/static/image
          # store relative path in DB as image location in HTML is relative
          db_upload_path= secure_filename(filename)
          # save the file and return the dbupload path
          fp.save(str(BASE_DIR) + "/img/" + db_upload_path )
          return db_upload_path
          
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