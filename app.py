from flask import Flask, render_template, request, jsonify
import os
import base64
import io
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

app = Flask(__name__)

model_path = 'model/trash_classifier.h5'
model = load_model(model_path)
label_map = {
    0: {'class': 'Cardboard', 'bin': 'Blue'},
    1: {'class': 'Glass', 'bin': 'Blue'},
    2: {'class': 'Metal', 'bin': 'Blue'},
    3: {'class': 'Paper', 'bin': 'Blue'},
    4: {'class': 'Plastic', 'bin': 'Blue'},
    5: {'class': 'Trash', 'bin': 'Brown'}
}


def process_image(image):
    img = image.resize((224, 224))
    img = np.asarray(img)
    img = img / 255.0
    return img

def predict_label(image):
    image = np.expand_dims(image, axis=0)
    prediction = model.predict(image)
    label_info = label_map[np.argmax(prediction)]
    return label_info


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    data = request.json
    image_data = data['image'].split(',')[1]
    image = Image.open(io.BytesIO(base64.b64decode(image_data)))
    processed_image = process_image(image)
    label_info = predict_label(processed_image)
    return jsonify(label_info)


if __name__ == '__main__':
    app.run(debug=True)
