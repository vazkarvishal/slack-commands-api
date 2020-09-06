from fastapi import FastAPI, Request, BackgroundTasks
import os
import json
import time
import asyncio
from slack import WebClient
import logging
# logging.basicConfig(level=logging.DEBUG)

client = WebClient(token=os.environ["SLACK_SIGNING_SECRET"])
app = FastAPI()

@app.get("/")
def root_page():
    return {"message": "welcome to my api"}


@app.post("/slack")
async def initial_slack_payload(request: Request, background_task: BackgroundTasks):
    form_data = await request.form()
    response_list = form_data.multi_items()
    request_payload = {}
    for item in response_list:
        key, value = item
        request_payload.update({key: value})

    response_message = {
        "response_type": "ephemeral",
        "text": ":v: We have received your request and working on it. :v:"
    }
    background_task.add_task(test_modal, request_payload)
    return response_message


async def test_modal(request_payload):
    response_url = request_payload["response_url"]
    response_message = {
        "response_type": "ephemeral",
        "text": ":v:Booms. :v:",
        "replace_original": "true"
    }

    # Show the ordering dialog to the user
    modal_response = client.views_open(
        trigger_id=request_payload["trigger_id"],
        view={
            "type": "modal",
            "callback_id": "modal-id",
            "title": {
                "type": "plain_text",
                "text": "Awesome Modal"
            },
            "submit": {
                "type": "plain_text",
                "text": "Submit"
            },
            "close": {
                "type": "plain_text",
                "text": "Cancel"
            },
            "blocks": [
                {
                    "type": "input",
                    "block_id": "b-id",
                    "label": {
                        "type": "plain_text",
                        "text": "Input label",
                    },
                    "element": {
                        "action_id": "a-id",
                        "type": "plain_text_input",
                    }
                }
            ]
        }
    )

    print(modal_response)
