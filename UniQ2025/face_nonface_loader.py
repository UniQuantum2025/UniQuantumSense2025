from PIL import Image
import os

# Directories for facial and non-facial images
facial_images_dir = r"C:\Users\wildw\OneDrive\Desktop\UniQuantumSense\Dataset\Faces"
non_facial_images_dir = r"C:\Users\wildw\OneDrive\Desktop\UniQuantumSense\Dataset\Non_Faces"

# List of specific facial images to load
facial_image_files = ["1.png", "7.png", "8.png", "12.png", "21.png", "26.png", "31.png", "41.png"]

# List of specific non-facial images to load
non_facial_image_files = ["146.jpg", "150.jpg", "154.jpg", "162.jpg", "170.jpg", "174.jpg", "199.jpg"]

# Function to load images
def load_images(directory, filenames):
    images = []
    for filename in filenames:
        img_path = os.path.join(directory, filename)
        if os.path.isfile(img_path):
            img = Image.open(img_path)
            images.append(img)
        else:
            print(f"Image {filename} not found at {img_path}.")
    return images

# Load Facial Images
facial_images = load_images(facial_images_dir, facial_image_files)

# Load Non-Facial Images
non_facial_images = load_images(non_facial_images_dir, non_facial_image_files)

# Process and evaluate images (your evaluation logic here)
print(f"Loaded {len(facial_images)} facial images and {len(non_facial_images)} non-facial images.")