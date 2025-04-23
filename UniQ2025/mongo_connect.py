from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Update the URI with your actual password
uri = "mongodb+srv://dammyers07:<KXdwpCJXHwF9SW4S>@uniq2025.qsehnnq.mongodb.net/?retryWrites=true&w=majority&appName=UniQ2025"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Could not connect to MongoDB:", e)
finally:
    client.close()