import os

API_TOKEN = os.environ.get("API_TOKEN")
PORT = int(os.environ.get("PORT", 8000))
UPLOAD_DIR = os.environ.get("UPLOAD_DIR", "uploads")
MAX_FILE_SIZE_MB = int(os.environ.get("MAX_FILE_SIZE_MB", 25))
MIN_DURATION_SEC = int(os.environ.get("MIN_DURATION_SEC", 5))
MAX_DURATION_SEC = int(os.environ.get("MAX_DURATION_SEC", 25))
