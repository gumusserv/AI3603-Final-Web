from flask import Flask,request,render_template,redirect,url_for, jsonify, send_file
from werkzeug.utils import secure_filename
import os
import shutil
from eval import *

app = Flask(__name__)





def process_image(image_path):
    # 在这里集成您的模型，处理图片
    # 返回处理后的图片路径或URL
    processed_image_path = original_evaluate(image_path)
    print(processed_image_path)
    return processed_image_path

@app.route('/upload_image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join('', filename)
        file.save(file_path)
        
        # 调用你的图像处理模型
        processed_image_path = process_image(file_path) # 这是一个假设的函数
        os.remove(file_path)

        return send_file(processed_image_path, mimetype='image/jpeg') # 或返回文件的URL

@app.route('/',methods = ['GET'])
def home():
    return render_template('home.html')

@app.route('/apply',methods = ['GET'])
def apply():
    return render_template('apply.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 5000,debug = True)