import os
from dotenv import load_dotenv

load_dotenv()
CLIENT_ACCESS_TOKEN = os.getenv("CLIENT_ACCESS_TOKEN")

print(CLIENT_ACCESS_TOKEN)
