import os
import requests

class DiscordHandler():
    webhook = None
    
    def __init__(self):
         self.webhook = os.getenv("DISCORD_WEBHOOK_URL")

    def post(self, message):
        JSON = {
            'embeds': [
                {
                    "title": "Message from Lepus",
                    "color": "5763719",
                    "description": message
                }
            ]
        }
        requests.post(self.webhook, json=JSON)