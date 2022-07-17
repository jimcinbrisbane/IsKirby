<<<<<<< Updated upstream
from flask import Flask, render_template, request, redirect, url_for
=======
from flask import Flask, render_template, request
from helper import check_upload_file, get_rgb_value, get_path, CipherAES

>>>>>>> Stashed changes
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files["fileToUpload"]
<<<<<<< Updated upstream
        return render_template('index.html')
    elif request.method == 'GET':
        return render_template('index.html')

=======
        check_upload_file(file)
        old_key = get_rgb_value(get_path(file.filename))
        key = CipherAES.get_hash_sha512(old_key)
        return render_template('key.html', key = key)
    elif request.method == 'GET':
        return render_template('index.html')
          
>>>>>>> Stashed changes
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