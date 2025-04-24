from PIL import Image
import os

# Directories containing the images
facial_images_dir = r"C:\Users\wildw\OneDrive\Documents\CMIT-450 Senior Seminar Project\Assignment\Week 14\UniQuantumSense\UniQ2025\Dataset\Trained Images\Faces"
non_facial_images_dir = r"C:\Users\wildw\OneDrive\Documents\CMIT-450 Senior Seminar Project\Assignment\Week 14\UniQuantumSense\UniQ2025\Dataset\Trained Images\Non_Faces"

# List to hold all images
images = []

# Load facial images (PNG)
for i in range(1, 100):  # From 1 to 99
    img_path = os.path.join(facial_images_dir, f"{i}.png")
    if os.path.isfile(img_path):
        img = Image.open(img_path)
        images.append(img)
    else:
        print(f"Facial Image {i}.png not found at {img_path}.")

# Load non-facial images (JPG)
for i in range(136, 182):  # From 136 to 181
    img_path = os.path.join(non_facial_images_dir, f"{i}.jpg")
    if os.path.isfile(img_path):
        img = Image.open(img_path)
        images.append(img)
    else:
        print(f"Non-Facial Image {i}.jpg not found at {img_path}.")

# Also include the last few non-facial images (196 to 199)
for i in range(196, 200):  # From 196 to 199
    img_path = os.path.join(non_facial_images_dir, f"{i}.jpg")
    if os.path.isfile(img_path):
        img = Image.open(img_path)
        images.append(img)
    else:
        print(f"Non-Facial Image {i}.jpg not found at {img_path}.")

# Combine images horizontally
if images:
    total_width = sum(img.width for img in images)
    max_height = max(img.height for img in images)

    # Create new image with the total width and max height
    combined_image = Image.new('RGB', (total_width, max_height))

    # Paste each image into the new image
    x_offset = 0
    for img in images:
        combined_image.paste(img, (x_offset, 0))
        x_offset += img.width

    # Save the combined image
    output_image_path = r"C:\Users\wildw\OneDrive\Documents\CMIT-450 Senior Seminar Project\Assignment\Week 14\UniQuantumSense\UniQ2025\Dataset\combined_image.png"
    combined_image.save(output_image_path)
    print(f"Combined image saved as {output_image_path}")
else:
    print("No images to combine.")