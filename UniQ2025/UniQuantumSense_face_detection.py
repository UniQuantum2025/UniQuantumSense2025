import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import simpledialog
import cv2
from PIL import Image, ImageTk
import tensorflow as tf
import numpy as np
import hashlib

# Load the trained model
model = None

def load_model():
    global model
    model_path = r"C:\Users\wildw\OneDrive\Desktop\UniQuantumSense\facial_detection_model.keras"

    try:
        model = tf.keras.models.load_model(model_path)
        print("Model loaded successfully!")
    except Exception as e:
        print(f"Error loading model: {e}")

# Set to store hashes of processed images
processed_hashes = set()

def hash_image(image):
    """
    Compute the SHA-256 hash of an image.

    Args:
        image (numpy.ndarray): The image to hash.

    Returns:
        str: The SHA-256 hash of the image.
    """
    image_bytes = cv2.imencode('.jpg', image)[1].tobytes()
    return hashlib.sha256(image_bytes).hexdigest()

def load_image():
    """
    Load and process an image for face detection.

    Prompts the user to select an image file and determines whether it contains a face or not.
    Displays the result in a message box.

    Returns:
        None
    """
    choice = simpledialog.askstring("Select Type", "Enter 'Faces' or 'Non_Faces':")
    if choice is None:
        return  # User canceled the dialog

    choice = choice.strip().lower()
    if choice not in ['faces', 'non_faces']:
        messagebox.showerror("Error", "Invalid selection. Please enter 'Faces' or 'Non_Faces'.")
        return

    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    img = cv2.imread(file_path)
    if img is None:
        messagebox.showerror("Error", "Could not load image.")
        return

    image_hash = hash_image(img)
    if image_hash in processed_hashes:
        messagebox.showinfo("Result", "This image has already been processed.")
        return
    else:
        processed_hashes.add(image_hash)

    resized_img = cv2.resize(img, (224, 224))
    normalized_img = resized_img / 255.0
    input_img = np.expand_dims(normalized_img, axis=0)

    # Predict if there is a face in the image
    if model is not None:
        prediction = model.predict(input_img)
        is_face_detected = prediction[0][0] > 0.5

        if choice == 'faces':
            if is_face_detected:
                messagebox.showinfo("Result", "Face detected!")
            else:
                messagebox.showinfo("Result", "No face detected.")
        else:
            if is_face_detected:
                messagebox.showinfo("Result", "Unexpected face detected.")
            else:
                messagebox.showinfo("Result", "No face detected as expected.")
    else:
        messagebox.showerror("Error", "Model is not loaded. Please restart the application.")

    display_image(img)

def display_image(img):
    """
    Display the given image in a new Tkinter window.

    Args:
        img (numpy.ndarray): The image to display.

    Returns:
        None
    """
    global window

    window = tk.Toplevel()
    window.title("Image Display")

    if hasattr(display_image, 'panel') and display_image.panel is not None:
        try:
            display_image.panel.destroy()
        except Exception as e:
            print(f"Error destroying previous image panel: {e}")

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    img_resized = img_pil.resize((400, 300), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img_resized)
    display_image.panel = tk.Label(window, image=img_tk)
    display_image.panel.image = img_tk
    display_image.panel.grid(row=1, column=0, columnspan=2)

    window.deiconify()
    window.update_idletasks()
def run_quantum_circuit_qiskit():
    """
    Placeholder function for running a quantum circuit using Qiskit.
    Implement your quantum circuit logic here.
    """
    print("Running quantum circuit...")

# Create the main window
window = tk.Tk()
window.title("Face Detection Application")

# Load the model at the start
load_model()

# Create a button to load an image
load_button = tk.Button(window, text="Load Image", command=load_image)
load_button.grid(row=0, column=0, padx=10, pady=10)

# Create a button to run the quantum function
quantum_button = tk.Button(window, text="Run Quantum Circuit", command=run_quantum_circuit_qiskit)
quantum_button.grid(row=0, column=1, padx=10, pady=10)

# Start the Tkinter main loop
window.mainloop()