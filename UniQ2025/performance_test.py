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

# Adding facial images from 1.png to 95.png
for i in range(1, 96):  # From 1 to 95
    test_cases[f"Single Image (Facial) {i}"] = r"C:\Users\wildw\OneDrive\Desktop\UniQuantumSense\Dataset\Trained Images\Faces\{}.png".format(i)

# Adding non-facial images (136.jpg to 170.jpg)
for i in range(136, 171):  # From 136 to 170
    test_cases[f"Single Image (Non-Facial) {i}"] = r"C:\Users\wildw\OneDrive\Desktop\UniQuantumSense\Dataset\Trained Images\Non_Faces\{}.jpg".format(i)

# Adding additional non-facial images (171.jpg to 181.jpg)
for i in range(171, 182):  # From 171 to 181
    test_cases[f"Single Image (Non-Facial) {i}"] = r"C:\Users\wildw\OneDrive\Desktop\UniQuantumSense\Dataset\Trained Images\Non_Faces\{}.jpg".format(i)

# Adding additional non-facial images (196.jpg to 199.jpg)
for i in range(196, 200):  # From 196 to 199
    test_cases[f"Single Image (Non-Facial) {i}"] = r"C:\Users\wildw\OneDrive\Desktop\UniQuantumSense\Dataset\Trained Images\Non_Faces\{}.jpg".format(i)

# Execute tests
for case, img_path in test_cases.items():
    if os.path.exists(img_path):  # Check if the file exists
        load_time, prediction_time = measure_performance(img_path)
        total_time = load_time + prediction_time
        print(f"{case} - Load Time: {load_time:.2f} s, Prediction Time: {prediction_time:.2f} s, Total Time: {total_time:.2f} s")
    else:
        print(f"{case} - Error: File not found at {img_path}")