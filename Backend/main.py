from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from config import SPOTIFY_CLIENT_ID, REDIRECT_URI
import urllib.parse

app = FastAPI()

@app.get("/")
def health_check():
	return {"status": "ok"}

@app.get("/callback")
def auth_callback(code: str = None, state: str = None, error: str = None):
	if error:
		return {"ok": False, "error": error}
	return {
		"ok": True,
		"code_received": code is not None,
		"code": code
	}


@app.get("/login")
def login():
	scope = "user-top-read playlist-modify-public playlist-modify-private"
	params = {
		"response_type": "code",
		"client_id": SPOTIFY_CLIENT_ID,
		"scope": scope,
		"redirect_uri": REDIRECT_URI,
		# redo
		"state": "dev_state"
	}
	url = "https://accounts.spotify.com/authorize?" + urllib.parse.urlencode(params)
	return RedirectResponse(url)

