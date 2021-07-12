import os
import base64
import hmac
import json
import random
from hashlib import sha256
from locust import HttpUser, task, constant


def generate_hmac_signature(body: str, secret: str) -> str:
    if not body or not secret:
        return ""
    h = hmac.new(secret.encode(), body.encode(), sha256)
    return base64.b64encode(h.digest()).decode()


class QuickstartUser(HttpUser):
    wait_time = constant(0)
    url = os.environ.get('TEST_DOMAIN', 'https://rapidpro.qa-hub.ie.gehosting.org/c/wa/43da1bd1-916e-4710-baa8-b4d91234a63f/receive')
    secret = os.environ.get('TEST_SECRET', '')

    @task
    def test_courier(self):
        text = "Lookup " + str(random.random())
        data = {"contacts":[{"profile":{"name":"Kerry Fisher"},"wa_id":"16315551234"}],"messages":[{"_vnd":{"v1":{"author":{"id":"16315551234","name":"Kerry Fisher","type":"OWNER"},"chat":{"assigned_to":None,"owner":"+16315551234","permalink":"https://app.turn.io/c/e3c3bdf6-9607-461a-8640-fd595cd1ca6f","state":"OPEN","state_reason":"Re-opened by inbound message.","unread_count":11,"uuid":text},"direction":"inbound","faq_uuid":None,"in_reply_to":None,"inserted_at":"2021-07-07T10:16:06.400299Z","labels":[],"rendered_content":None}},"from":"16315551234","id":"ABGGJ4Iyg3RPAhC44I-8dcG_we7DovTd0dop","text":{"body":text},"timestamp":"1625652966","type":"text"}]}

        headers= {
                'X-Turn-Hook-Signature': generate_hmac_signature(json.dumps(data), self.secret),
                'Content-Type': 'application/json',
            }
        self.client.post(self.url, json=data, headers=headers)

    def on_start(self):
        pass

    def on_stop(self):
        pass
