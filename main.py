import os
from dotenv import load_dotenv

load_dotenv()
CLIENT_ACCESS_TOKEN = os.getenv("CLIENT_ACCESS_TOKEN")

# Hey it works!
print(CLIENT_ACCESS_TOKEN)

""""
git pull origin main: to pull updated main branch
"""
