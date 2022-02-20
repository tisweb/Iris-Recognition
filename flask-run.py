
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
# from os.path import os
import os

app = Flask(__name__)

# app.config['SERVER_NAME'] = 'localhost:5000'


# os.makedirs('IRIS_ENROLL_IMAGES')
isdir = os.path.isdir('IRIS_ENROLL_IMAGES')
print(isdir)
if isdir != True:
    os.makedirs('IRIS_ENROLL_IMAGES')

basedir = os.path.abspath(os.path.dirname(__file__))
Iris_Enroll_Images = os.path.join(basedir, 'IRIS_ENROLL_IMAGES') 

    

@app.route('/verify',methods=['GET'])
def hello_world():
    d = {}
    d['Query'] = request.args['Query']
    return jsonify(d)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename = secure_filename(file.filename)
    print(filename)
    file.save(os.path.join(Iris_Enroll_Images, filename))
    d = {}
    d['Result'] = "Uploaded"
    return jsonify(d)
    # return "Response uploaded"

if __name__ == '__main__':
    app.run()
