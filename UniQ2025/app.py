import os
import streamlit as st
import numpy as np
import cv2
from PIL import Image
import psycopg2
import sentry_sdk
import asyncio
import websockets
import json
import requests
import threading
from UniQuantumSense_face_detection import load_image, run_quantum_circuit_qiskit

# Load environment variables
from load_env import load_dotenv
load_dotenv()

# Initialize Sentry for error monitoring
sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),  
    send_default_pii=True,
)

# Connect to PostgreSQL
def connect_db():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

# WebSocket Server Function
async def websocket_handler(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        response = {"message": "Hello, Client!"}
        await websocket.send(json.dumps(response))

# Function to start WebSocket server
async def start_websocket_server():
    async with websockets.serve(websocket_handler, "localhost", 8765):
        print("WebSocket server started at ws://localhost:8765")
        await asyncio.Future()  # Run forever

# Function to run the WebSocket server in a separate thread
def start_server_thread():
    asyncio.run(start_websocket_server())

# Start the WebSocket server thread
threading.Thread(target=start_server_thread, daemon=True).start()

# Streamlit app title
st.title("UniQuantumSense")

# File uploader for image input
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

if uploaded_file is not None:

    # Open the image using PIL
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    # Button to trigger face detection and quantum circuit execution
    if st.button('Detect Face'):
        image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)  # Convert from RGB to BGR

        try:
            # Call the load_image function to process the image
            load_image(image_cv)  # Assuming load_image handles face detection

            # Run the quantum circuit
            features = [1, 1, 0]  # Example features, adjust as necessary
            result = run_quantum_circuit_qiskit(features)  # Call your quantum function

            # Display the result of the quantum circuit
            st.write("Quantum Circuit Result:", result)

            # Save image to PostgreSQL (convert image to binary)
            conn = connect_db()
            with conn.cursor() as cursor:
                img_binary = np.array(image).tobytes()
                cursor.execute("INSERT INTO images (image_data) VALUES (%s)", (psycopg2.Binary(img_binary),))
                conn.commit()
            conn.close()
            st.success("Image saved to database successfully.")

            # Upload image to API
            if st.button('Upload Image to API'):
                files = {'file': uploaded_file.getvalue()}
                response = requests.post("http://localhost:8000/upload-image/", files=files)
                if response.status_code == 200:
                    st.success(response.json()["status"])
                else:
                    st.error("Failed to upload image.")

            # Call WebSocket client
            async def call_websocket_client():
                async with websockets.connect("ws://localhost:8765") as websocket:
                    await websocket.send("Image processed successfully!")
                    response = await websocket.recv()
                    st.write("WebSocket Response:", response)

            asyncio.run(call_websocket_client())

        except Exception as e:
            sentry_sdk.capture_exception(e)
            st.error("An error occurred while processing the image.")