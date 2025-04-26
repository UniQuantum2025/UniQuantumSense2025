import time
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

# Load the trained model
model = load_model(r"C:\Users\wildw\OneDrive\Desktop\UniQuantumSense\models\facial_detection_model.keras")

# Function to load and preprocess images
def load_and_preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

# Function to measure performance for a given image
def measure_performance(img_path):
    # Measure loading time
    start_time = time.time()
    new_data = load_and_preprocess_image(img_path)
    load_time = time.time() - start_time

    # Measure prediction time
    start_time = time.time()
    predictions = model.predict(new_data)
    prediction_time = time.time() - start_time

    return load_time, prediction_time

# Test Cases with updated paths
test_cases = {}

# List of specific facial images to test
facial_image_files = ["1.png", "7.png", "8.png", "12.png", "21.png", "26.png", "31.png", "41.png"]

# List of specific non-facial images to test
non_facial_image_files = ["146.jpg", "150.jpg", "154.jpg", "162.jpg", "170.jpg", "174.jpg", "199.jpg"]

# Adding facial images to test cases
for filename in facial_image_files:
    test_cases[f"Single Image (Facial) {filename}"] = os.path.join(r"C:\Users\wildw\OneDrive\Desktop\UniQuantumSense\Dataset\Faces", filename)

# Adding non-facial images to test cases
for filename in non_facial_image_files:
    test_cases[f"Single Image (Non-Facial) {filename}"] = os.path.join(r"C:\Users\wildw\OneDrive\Desktop\UniQuantumSense\Dataset\Non_Faces", filename)

# Execute tests
for case, img_path in test_cases.items():
    if os.path.exists(img_path):  # Check if the file exists
        load_time, prediction_time = measure_performance(img_path)
        total_time = load_time + prediction_time
        print(f"{case} - Load Time: {load_time:.2f} s, Prediction Time: {prediction_time:.2f} s, Total Time: {total_time:.2f} s")
    else:
        print(f"{case} - Error: File not found at {img_path}")