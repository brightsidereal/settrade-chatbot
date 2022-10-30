from fastapi import FastAPI, Request, Header
import settrade_v2
import json
from settrade_v2 import Investor
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, PostbackEvent, TextMessage, TextSendMessage,
    FlexSendMessage, QuickReply, QuickReplyButton, MessageAction,
    PostbackAction
)

lineaccesstoken = 'your-line-access-token'
line_bot_api = LineBotApi(lineaccesstoken)
handler = WebhookHandler('your-secret-key')

investor = Investor(
    app_id="fsY7Xno94oIrhdGr",
    app_secret="AKMWjn8JCB68cYy//3hEvfPbO5WSZhqCLU2P7UXxOYrt",
    broker_id="SANDBOX",
    app_code="SANDBOX",
    is_auto_queue=False)

deri = investor.Derivatives(account_no="bright66-D")

try:
    account_info = deri.get_account_info()
except Exception as e:
    print(e)

print(json.dumps(account_info, indent=2))


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Bright"}
  
@app.get("/account")
def read_account():
  return account_info

