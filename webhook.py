# webhook.py
from fastapi import FastAPI, Request
import httpx
import os

app = FastAPI()

GITHUB_REPO = "muqtasid87/mlops_demo_try_2"
GITHUB_TOKEN = "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" # Store GitHub Token securely in environment variables

@app.post("/webhook")
async def handle_wandb_webhook(request: Request):
    payload = await request.json()

    # Ensure the production alias has been added
    if payload.get("alias") == "production":
        # Trigger GitHub Action workflow
        headers = {
            "Authorization": f"token {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json"
        }
        url = f"https://api.github.com/repos/{GITHUB_REPO}/dispatches"
        data = {
            "event_type": "wandb_model_updated",  # Custom event type for GitHub Actions
            "client_payload": {
                "model_name": payload.get("model")  # Optional: pass model details to GitHub Action
            }
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=data, headers=headers)

        if response.status_code == 204:
            return {"message": "GitHub Action triggered successfully"}
        else:
            return {"error": "Failed to trigger GitHub Action", "details": response.text}

    return {"message": "Alias not production, no action taken"}
