# Import necessary libraries
import os  # For handling file paths and directories
import tensorflow as tf  # Import TensorFlow
from tensorflow.keras import layers, models  # Import layers and models from Keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator  # For image data augmentation
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint  # For training callbacks

def create_model():
    
    # Create a sequential model
    model = models.Sequential()

    # Add convolutional layers and pooling layers
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Flatten())
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))

    # Compile the model
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Adjust path based on dataset
train_dir = r"C:\Users\wildw\OneDrive\Documents\CMIT-450 Senior Seminar Project\Assignment\Week 14\UniQuantumSense\UniQ2025\Dataset"

# Create an instance of ImageDataGenerator for data preprocessing
train_datagen = ImageDataGenerator(rescale=1./255)

try:
    # Load images from the directory and set parameters
    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(224, 224),
        batch_size=32,
        class_mode='binary'
    )
except Exception as e:

    # Print error message and exit if dataset loading fails
    print(f"Error loading dataset: {e}")
    exit()

# Create the model
model = create_model()
model.summary()  # Print model summary

# Early stopping and model checkpointing to prevent overfitting
early_stopping = EarlyStopping(monitor='loss', patience=3)
model_checkpoint = ModelCheckpoint('best_model.keras', save_best_only=True)

# Fit the model to the training data
model.fit(train_generator, epochs=10, callbacks=[early_stopping, model_checkpoint])

# Save the trained model
model.save(r"C:\Users\wildw\OneDrive\Documents\CMIT-450 Senior Seminar Project\Assignment\Week 14\UniQuantumSense\UniQ2025\Dataset\facial_detection_model.keras")
print("Model saved as facial_detection_model.keras")