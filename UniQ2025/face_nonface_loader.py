from PIL import Image
import os

# Directories for test and trial images
test_faces_dir = r"C:\Users\wildw\OneDrive\Desktop\UniQuantumSense\Dataset\Predict Images\Test\Faces"
test_non_faces_dir = r"C:\Users\wildw\OneDrive\Desktop\UniQuantumSense\Dataset\Predict Images\Test\Non_Faces"
trial_faces_dir = r"C:\Users\wildw\OneDrive\Desktop\UniQuantumSense\Dataset\Predict Images\Trial\Faces"
trial_non_faces_dir = r"C:\Users\wildw\OneDrive\Desktop\UniQuantumSense\Dataset\Predict Images\Trial\Non_Faces"

# Function to load images
def load_images(directory, file_range, file_type):
    images = []
    for i in file_range:
        img_path = os.path.join(directory, f"{i}.{file_type}")
        if os.path.isfile(img_path):
            img = Image.open(img_path)
            images.append(img)
        else:
            print(f"Image {i}.{file_type} not found at {img_path}.")
    return images

# Load Test Images
test_faces = load_images(test_faces_dir, range(96, 116), 'png')
test_non_faces = load_images(test_non_faces_dir, range(180, 191), 'jpg')  # Adjust this if needed

# Load Trial Images
trial_faces = load_images(trial_faces_dir, range(116, 136), 'png')
trial_non_faces = load_images(trial_non_faces_dir, range(181, 196), 'jpg')  # Adjust this if needed

# Process and evaluate images (your evaluation logic here)
print(f"Loaded {len(test_faces)} test face images and {len(test_non_faces)} test non-face images.")
print(f"Loaded {len(trial_faces)} trial face images and {len(trial_non_faces)} trial non-face images.")