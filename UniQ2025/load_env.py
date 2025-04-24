import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the variables
secret_key = os.getenv('SECRET_KEY')
api_url = os.getenv('API_URL')
