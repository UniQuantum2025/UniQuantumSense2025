import sys
from tensorflow.keras.models import load_model

# Path to the model
model_path = r"C:\Users\wildw\OneDrive\Documents\CMIT-450 Senior Seminar Project\Assignment\Week 14\UniQuantumSense\UniQ2025\Dataset\Trained Images"

try:
    # Load the model
    model = load_model(model_path)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")