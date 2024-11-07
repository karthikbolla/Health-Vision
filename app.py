from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import numpy as np
from classify import classify  # Import classify function from classify.py

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return redirect(url_for('home'))

    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('home'))

    img = Image.open(file.stream).convert('RGB')
    img_array = np.array(img)
    prediction = classify(img_array)

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
