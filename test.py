import os
from dotenv import load_dotenv
# Load secret .env file
load_dotenv()
# Store credentials
pwd = os.getenv('MY_PASSWORD')
key = os.getenv('MY_API_KEY')
# Verify it worked
print(pwd)
