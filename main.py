from fastapi import FastAPI, Response
import os
import vocode
from vocode.streaming.telephony.inbound_call_server import InboundCallServer
from vocode.streaming.models.message import BaseMessage
from vocode.streaming.models.telephony import TwilioConfig
from vocode.streaming.models.agent import ChatGPTAgentConfig

vocode.api_key = os.getenv("VOCODE_API_KEY")

app = FastAPI()

@app.get("/")
def root():
    vercel_url = f"https://{os.getenv('VERCEL_URL')}"
    return Response(
        content=f"<div>Paste the following URL into your Twilio config: {vercel_url}/vocode",
        media_type="text/html",
    )

def create_inbound_call_server():
    return InboundCallServer(
        agent_config=ChatGPTAgentConfig(
            initial_message=BaseMessage(text="Hello! What can I help you with?"),
            prompt_preamble="You are a helpful AI assistant. You respond in 10 words or less.",
        ),
        twilio_config=TwilioConfig(
            account_sid=os.getenv("TWILIO_ACCOUNT_SID"),
            auth_token=os.getenv("TWILIO_AUTH_TOKEN"),
        ),
    )

server = create_inbound_call_server()
