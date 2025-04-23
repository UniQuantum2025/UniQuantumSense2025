import time
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

# Load the trained model
model = load_model('facial_detection_model.keras')

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

# Test Cases with specified paths
test_cases = {
    "Single Image (Facial)": r"C:\Users\wildw\OneDrive\Documents\CMIT-450 Senior Seminar Project\Assignment\Week 14\UniQuantumSense\UniQ2025\Dataset\Trained Images\Faces\your_facial_image.jpg",  # Replace with actual image name
    "Single Image (Non-Facial)": r"C:\Users\wildw\OneDrive\Documents\CMIT-450 Senior Seminar Project\Assignment\Week 14\UniQuantumSense\UniQ2025\Dataset\Trained Images\Non_Faces\your_non_facial_image.jpg",  # Replace with actual image name
    "Multiple Images": r"C:\Users\wildw\OneDrive\Documents\CMIT-450 Senior Seminar Project\Assignment\Week 14\UniQuantumSense\UniQ2025\Dataset\Predict Images\your_multiple_images.jpg"  # Replace with actual image name
}

# Execute tests
for case, img_path in test_cases.items():
    if os.path.exists(img_path):  # Check if the file exists
        load_time, prediction_time = measure_performance(img_path)
        total_time = load_time + prediction_time
        print(f"{case} - Load Time: {load_time:.2f} s, Prediction Time: {prediction_time:.2f} s, Total Time: {total_time:.2f} s")
    else:
        print(f"{case} - Error: File not found at {img_path}")