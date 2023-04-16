from flask import Flask, render_template, request, redirect, url_for
import os
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

model_path = 'model/trash_classifier_model.h5'
model = load_model(model_path)
label_map = {0: 'Cardboard', 1: 'Glass', 2: 'Metal', 3: 'Paper', 4: 'Plastic', 5: 'Trash'}

def process_image(image_path):
    img = Image.open(image_path)
    img = img.resize((224, 224))
    img = np.asarray(img)
    img = img / 255.0
    return img

def predict_label(image):
    image = np.expand_dims(image, axis=0)
    prediction = model.predict(image)
    label = label_map[np.argmax(prediction)]
    return label

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        image = process_image(file_path)
        label = predict_label(image)
        return render_template('result.html', image_path=file_path, label=label)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
