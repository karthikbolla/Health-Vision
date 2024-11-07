# Medical Image Classification with Flask

This project is a Flask web application that classifies different types of medical images. Users can upload an image, and the app will predict the category and diagnosis based on the model.

## Project Structure

- `models/`: Contains pre-trained TensorFlow models for various medical classifications.
- `app/`: Contains the application code, including views and model inference logic.
- `static/` and `templates/`: CSS and HTML files for the web interface.

## Requirements

- Flask
- TensorFlow
- NumPy
- OpenCV
- Pillow (for image processing)

## How to Run

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
