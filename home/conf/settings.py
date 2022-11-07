import os

from dotenv import load_dotenv


load_dotenv()

CERTIFICATE = os.getenv("CERTIFICATE")
DATABASEURL = os.getenv("databaseURL")