import logging
import os
import uuid
from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from starlette.middleware.sessions import SessionMiddleware
from authlib.integrations.starlette_client import OAuth
import requests
import ban_appeal.html_data as html_data

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
async def home(request: Request):
    user = request.session.get("user", {})

    html_content = html_data.main_page(user)

    return HTMLResponse(content=html_content)

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

@app.post("/appeal")
async def appeal(request: Request, appeal_text: str = Form(...)):
    if not request.session.get("user"):
        return RedirectResponse(url="/login", status_code=303)
    
    user = request.session["user"]
    
    # Validate appeal text length
    if len(appeal_text) < 100 or len(appeal_text) > 5000:
        send_to_discord_webhook(f"User [{user['username']}] ({user['id']}) tried to bypass the appeal length restriction with a length of {len(appeal_text)} characters.")
        return HTMLResponse(
            content=html_data.FAILED_APPEAL(len(appeal_text)),
            status_code=400
        )
    
    
    logger.info(f"Appeal submitted by user {user['username']} ({user['id']}): {appeal_text[:100]}...")
    send_to_discord_webhook(f"New appeal from [{user['username']}] ({user['id']}):\n{appeal_text}")
    content=html_data.SUCCESSFUL_APPEAL(user=user, appeal_text=appeal_text)
    request.session.clear()
    return HTMLResponse(
        content=content,
        status_code=200
    )

def send_to_discord_webhook(content: str):
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        logger.error("DISCORD_WEBHOOK_URL is not set.")
        return
    
    data = {
        "content": content
    }
    
    response = requests.post(webhook_url, json=data)
    
    if response.status_code != 204:
        logger.error(f"Failed to send message to Discord webhook: {response.status_code} - {response.text}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)