from fastapi import FastAPI, Query
from fastapi.responses import RedirectResponse
from config import SPOTIFY_CLIENT_ID, REDIRECT_URI, SPOTIFY_CLIENT_SECRET
import urllib.parse
import secrets
from auth_token import exchange_code_for_tokens
import httpx

app = FastAPI()

# TEMP Storage
TOKENS_BY_SESSION = {}

@app.get("/")
def health_check():
	return {"status": "ok"}

@app.get("/auth/callback")
async def auth_callback(code: str = Query(None), state: str = Query(None), error: str = Query(None)):
	if error:
		return {"ok": False, "error": error}

	if not code:
		return {"ok": False, "error": "No code returned"}

	# Token exchange happens
	token_json = await exchange_code_for_tokens(code)
	access_token = token_json["access_token"]

	# verify token works by calling /me
	async with httpx.AsyncClient(timeout=20) as client:
		me_resp = await client.get("https://api.spotify.com/v1/me", headers={"Authorization": f"Bearer {access_token}"})
		if me_resp.status_code != 200:
			return {"ok": False, "error": "Token works but /me failed", "details": me_resp.text}
		me = me_resp.json()

	# Store tokens keyed by spotify user id (dev approach)
	spotify_user_id = me["id"]
	TOKENS_BY_SESSION[spotify_user_id] = token_json
	
	
	return RedirectResponse(url="http://127.0.0.1:5173/home", status_code=302)


@app.get("/api/login")
def login():
	scope = "user-top-read playlist-modify-public playlist-modify-private playlist-read-private playlist-read-collaborative user-library-read"
	state = secrets.token_urlsafe(32)

	params = {
		"response_type": "code",
		"client_id": SPOTIFY_CLIENT_ID,
		"scope": scope,
		"redirect_uri": REDIRECT_URI,
		# redo
		"state": state
	}
	url = "https://accounts.spotify.com/authorize?" + urllib.parse.urlencode(params)
	return RedirectResponse(url)

