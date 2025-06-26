from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import random

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploaded_images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Dummy butterfly class list
butterfly_classes = [
    "Monarch", "Swallowtail", "Painted Lady", "Red Admiral", "Blue Morpho",
    "Zebra Longwing", "Gulf Fritillary", "Common Buckeye", "Peacock", "Small Tortoiseshell"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            return "No file selected"
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Dummy prediction
        prediction = random.choice(butterfly_classes)
        return render_template('predict.html', prediction=prediction, image_url=filepath)

    return render_template('predict.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)
