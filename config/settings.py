"""Butun ayarlar bir yerde. Deyerler .env faylindan oxunur."""
import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "http://localhost:8090")
TIMEOUT = int(os.getenv("TIMEOUT", "15"))
