import os 
from dotenv import load_dotenv
from atproto import Client
from bunpost.TwitterHandler import TwitterHandler
from bunpost.DiscordHandler import DiscordHandler

# Load the environment variables.
load_dotenv()
# Load the Bluesky password into a variable
USER_BLUESKY_PASSWORD   = os.getenv("BLUESKY_APP_PASSWORD")
USER_BLUESKY_HANDLE     = os.getenv("BLUESKY_APP_HANDLE")
# Create the Bluesky client
client = Client()
client.login(USER_BLUESKY_HANDLE, USER_BLUESKY_PASSWORD)
# Load the Twitter/X credentials
twitterClient = TwitterHandler()
twitterClient.get_user_access_token()
# Load the Discord Webhook
discordWebhook = DiscordHandler()

def handle_user_input():
    message = input("Provide your message: ")
    print(f"Sending ...")
    post = client.send_post( message )
    print(f"Send to Bluesky at: {post.uri}")
    twitterClient.send_text_tweet( message )
    print("Sent to Twitter")
    discordWebhook.post(message)
    print("Send to Discord!")

handle_user_input()