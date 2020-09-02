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
    print(form_data)
    response_message = {
      "response_type": "ephemeral",
      "text": ":v: We have received your request and working on it. :v:"
    }
    return response_message
