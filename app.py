import os

from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from function.inference import *

UPLOAD_FOLDER = 'static/'
app = Flask(__name__, template_folder='templates')
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route('/')
def index():
    return render_template('upload_img.html')


@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No Image.')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image is selected !')
        return redirect(request.url)
    if file and allowed_image(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('Image successfully displayed and save')
        txt_print = get_txt(filename)
        return render_template('upload_img.html', filename=filename, txt_print = txt_print)
    else:
        flash("Allowed Image Format are: png, jpg. jpeg. gif")
        return redirect(request.url)


@app.route('/display/<filename>')
def display_img(filename):
    return redirect(url_for('static', filename=filename, code=301))


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_image(filename):
    return '.' in filename \
           and filename.rsplit('.', 1)[1].lower() \
           in ALLOWED_EXTENSIONS
