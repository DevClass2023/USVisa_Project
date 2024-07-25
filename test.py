import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the MongoDB URL from environment variable
mongo_db_url = os.getenv("MONGODB_URL")
print("MongoDB URL:", mongo_db_url)
