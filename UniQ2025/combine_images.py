from PIL import Image
import os

# Directories containing the images
facial_images_dir = r"C:\Users\wildw\OneDrive\Desktop\UniQuantumSense\Dataset\Faces"
non_facial_images_dir = r"C:\Users\wildw\OneDrive\Desktop\UniQuantumSense\Dataset\Non_Faces"

# List to hold all images
images = []

# List of specific facial images to load
facial_image_files = ["1.png", "7.png", "8.png", "12.png", "21.png", "26.png", "31.png", "41.png"]

# Load specified facial images (PNG)
for filename in facial_image_files:
    img_path = os.path.join(facial_images_dir, filename)
    if os.path.isfile(img_path):
        img = Image.open(img_path)
        images.append(img)
    else:
        print(f"Facial Image {filename} not found at {img_path}.")

# List of specific non-facial images to load
non_facial_image_files = ["146.jpg", "150.jpg", "154.jpg", "162.jpg", "170.jpg", "174.jpg", "199.jpg"]

# Load specified non-facial images (JPG)
for filename in non_facial_image_files:
    img_path = os.path.join(non_facial_images_dir, filename)
    if os.path.isfile(img_path):
        img = Image.open(img_path)
        images.append(img)
    else:
        print(f"Non-Facial Image {filename} not found at {img_path}.")

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

    # Save the combined image to the specified output path
    output_image_path = r"C:\Users\wildw\OneDrive\Desktop\UniQuantumSense\Dataset\combined_image.png"
    combined_image.save(output_image_path)
    print(f"Combined image saved as {output_image_path}")
else:
    print("No images to combine.")