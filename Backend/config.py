import os
from dotenv import load_dotenv

load_dotenv()

# Load env variables
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

if not SPOTIFY_CLIENT_ID or not SPOTIFY_CLIENT_SECRET or not REDIRECT_URI:
	raise RuntimeError("Missing Spotify vars, check .env vars")

