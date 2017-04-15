from flask import Flask, render_template, request
from random import randint
from werkzeug import secure_filename
import os

svc_web_parser = Flask(__name__)

#Каталог для сохранения файлов:
svc_web_parser.config['UPLOAD_FOLDER'] = 'uploads/'

@svc_web_parser.route('/')
def index():
    return render_template('index.html')


@svc_web_parser.route('/allstats')
def allstats():
    return render_template('allstats.html')    


@svc_web_parser.route('/<upload_id>')
def stats_visualization_by_id(upload_id):
    return render_template('results.html')


@svc_web_parser.route('/upload', methods=['POST'])
def upload():
    upload_id = randint(100000, 999999)
    #!!!!Don't forget to check if upload_id unique!!!!
    uploaded_files = request.files.getlist("file[]")
    print(uploaded_files)
    filenames = []
    for file in uploaded_files:
        filename = secure_filename(file.filename) 
        file.save(os.path.join(svc_web_parser.config['UPLOAD_FOLDER'], filename))
        filename = svc_web_parser.config['UPLOAD_FOLDER'] + filename
        filenames.append(filename)
    print(filenames)
    return render_template('upload.html', upload_id = upload_id)

if __name__ == "__main__":
    svc_web_parser.run(debug=True)


