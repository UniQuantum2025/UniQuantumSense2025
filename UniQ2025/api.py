from fastapi import FastAPI, UploadFile, File
import psycopg2
import numpy as np
from PIL import Image
import io

app = FastAPI()

# Connect to PostgreSQL
def connect_db():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="@XyYxLoOl662@$%",
        host="localhost",
        port="5432"
    )

@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    content = await file.read()
    image = Image.open(io.BytesIO(content))
    
    # Save image to PostgreSQL
    conn = connect_db()
    with conn.cursor() as cursor:
        img_binary = np.array(image).tobytes()
        cursor.execute("INSERT INTO images (image_data) VALUES (%s)", (psycopg2.Binary(img_binary),))
        conn.commit()
    conn.close()
    
    return {"filename": file.filename, "status": "Image uploaded successfully!"}