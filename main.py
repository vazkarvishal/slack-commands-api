from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional
import json

#
# class Data(BaseModel):
#     payload: Optional[dict] = Form


app = FastAPI()


@app.get("/")
def root_page():
    return {"message": "welcome to my api"}


@app.post("/slack")
async def initial_slack_payload(request: Request):

    form_data = await request.form()
    response_list = form_data.multi_items()
    response_payload = {}
    for item in response_list:
        key, value = item
        response_payload.update({key: value})

    print(json.dumps(response_payload, indent= 4, sort_keys=True))
    response_message = {
      "response_type": "ephemeral",
      "text": ":v: We have received your request and working on it. :v:"
    }
    return response_message
