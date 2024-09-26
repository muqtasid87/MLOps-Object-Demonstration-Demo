import modal
from fastapi import FastAPI
import requests

# Set up Modal app
app = modal.App(name="wandb-webhook")

@app.post("/webhook")
async def handle_webhook(data: dict):
    # Log the incoming data for debugging purposes
    print("Received webhook data:", data)

    # GitHub Actions endpoint and token
    github_url = "https://api.github.com/repos/muqtasid87/mlops_demo_try_2/dispatches"
    github_token = "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"  # Replace with your actual GitHub token

    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json",
    }

    payload = {
        "event_type": "trigger_model_download",
        "client_payload": {
            "model_name": "muqtasid87-international-islamic-university-malaysia-org/wandb-registry-model/toll_plaza:v9"
        }
    }

    # Trigger the GitHub Action
    response = requests.post(github_url, json=payload, headers=headers)

    # Return the response from GitHub Actions
    return {"status": "Webhook received", "response": response.json()}


# Use app.asgi to deploy the FastAPI app
@app.asgi()
def fastapi_app_deployment():
    return app

# Run the app on Modal
if __name__ == "__main__":
    modal.run(fastapi_app_deployment())
