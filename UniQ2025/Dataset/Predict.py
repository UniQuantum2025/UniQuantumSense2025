import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Define model function
def create_model():
    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Flatten())
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))  
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Set the directory dataset
train_dir = r"C:\Users\wildw\OneDrive\Documents\CMIT-450 Senior Seminar Project\Assignment\Week 14\UniQuantumSense\UniQ2025\Dataset\Predict Images"

# Create an ImageDataGenerator instance for loading images
train_datagen = ImageDataGenerator(rescale=1./255)  

# Load images from the directory
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(224, 224),  # Resize images
    batch_size=32,
    class_mode='binary'  
)

# Create and train model
model = create_model()
model.fit(train_generator, epochs=10) 

# Save the model
model.save('facial_detection_model.keras')
print("Model saved as facial_detection_model.keras")