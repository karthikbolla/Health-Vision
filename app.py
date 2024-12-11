from flask import Flask, render_template, request, redirect, url_for
from PIL import Image, UnidentifiedImageError
import numpy as np
from classify import classify  # Import classify function from classify.py
import os

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    error = request.args.get('error')
    return render_template('index.html', error=error)

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return redirect(url_for('home', error="No file part in the request."))

    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('home', error="No selected file."))

    try:
        # Save the uploaded image
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        # Open the image and process it
        img = Image.open(filepath).convert('RGB')
        img_array = np.array(img)

        # Get the prediction
        prediction = classify(img_array)

        # Provide the uploaded image URL to the template
        uploaded_image_url = url_for('static', filename=f'uploads/{file.filename}')
    except UnidentifiedImageError:
        return redirect(url_for('home', error="Invalid image file. Please upload a valid image."))
    except Exception as e:
        return redirect(url_for('home', error="An error occurred during prediction."))

    return render_template('index.html', prediction=prediction, uploaded_image_url=uploaded_image_url)

if __name__ == '__main__':
    app.run(debug=True)
