import logging
import os
import uuid
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from authlib.integrations.starlette_client import OAuth
import requests

logger = logging.getLogger(__name__)

app = FastAPI()
oauth = OAuth()
discord = oauth.register(
    name="discord",
    client_id=os.getenv("DISCORD_CLIENT_ID"),
    client_secret=os.getenv("DISCORD_CLIENT_SECRET"),
    access_token_url="https://discord.com/api/oauth2/token",
    authorize_url="https://discord.com/api/oauth2/authorize",
    api_base_url="https://discord.com/api/",
    client_kwargs={"scope": "identify"},
)
app.add_middleware(SessionMiddleware, secret_key=uuid.uuid4().hex)

@app.get("/")
async def authenticate(request: Request):
    if request.session.get("user"):
        user = request.session["user"]
        return {"message": f"Hello, {user['username']}#{user['discriminator']}!"}
    return RedirectResponse(url=request.url_for("auth"))

@app.get("/login")
async def auth(request: Request):
    redirect_uri = request.url_for("auth_callback")
    return await oauth.discord.authorize_redirect(request, redirect_uri=redirect_uri)

@app.get("/auth")
async def auth_callback(request: Request):
    token = await oauth.discord.authorize_access_token(request)
    ident = requests.get("https://discord.com/api/users/@me", headers={"Authorization": f"Bearer {token['access_token']}"}).json()
    request.session.update({"user": ident})
    return RedirectResponse(url="/")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)