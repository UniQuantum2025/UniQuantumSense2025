import os
import tensorflow as tf

# Define the model path
model_path = r"C:\Users\wildw\OneDrive\Desktop\UniQuantumSense\models\facial_detection_model.keras"

# Initialize model variable
model = None


def load_model():
    global model  # Declare model as global to modify it in this function
    print("Checking model path...")  # Debug statement

    # Check if the model path exists
    if not os.path.exists(model_path):
        print(f"Model file does not exist at the specified path: {model_path}")
        return
    try:
        # Load the model using TensorFlow/Keras
        model = tf.keras.models.load_model(model_path)
        print("Model loaded successfully!")  # Debug statement
    except Exception as e:
        print(f"Error loading model: {e}")


def load_image(input_img):
    global model  # Using the global model variable
    if model is None:
        print("Model is not loaded.")  # Debug statement
        return None

    # Make prediction
    print("Making prediction...")  # Debug statement
    prediction = model.predict(input_img)
    return prediction


# Call load_model to initialize the model when this script runs
load_model()
