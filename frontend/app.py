from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action1') == 'VALUE1':
            return redirect(url_for('confirmation'))
        elif  request.form.get('action2') == 'VALUE2':
            return redirect(url_for('about'))
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('index.html')
    return render_template("index.html")

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