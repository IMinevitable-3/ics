import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.environ.get("SECRET_KEY", "your'e secret key here ")
DEBUG = os.environ.get("DEBUG", True)
