import os
from requests_oauthlib import OAuth1Session

class TwitterHandler():
        
    X_Client = None

    def __init__(self):
        self.X_Client = OAuth1Session(
            client_key=os.getenv("TWITTER_API_KEY"),
            client_secret=os.getenv("TWITTER_API_KEY_SECRET"),
            resource_owner_key=os.getenv("TWITTER_OAUTH_USER_TOKEN"),
            resource_owner_secret=os.getenv("TWITTER_OAUTH_USER_SECRET"),
            callback_uri="oob"
        )

    def send_text_tweet(self,message):
        self.X_Client.post('https://api.x.com/2/tweets', json={'text':message})

    def check_user_access_token_exists(self):
        if os.getenv('TWITTER_OAUTH_USER_TOKEN'):
            return True
        return False

    def get_user_access_token(self):   
        if self.check_user_access_token_exists() == True:
            print("Using stored access token for Twitter/X.")
            return 

        # 1a, 1b. App Authenticates to the API. API returns an authorisation request token.
        app_authorisation_token = self.X_Client.fetch_request_token("https://api.x.com/oauth/request_token")
        # 2a. Give the user a link to Twitter/X with the authorisation token
        authorisation_link = self.X_Client.authorization_url("https://api.x.com/oauth/authorize")
        print(authorisation_link)
        # 3a. Pass the code to the API 
        authorisation_code = input("Enter the authorisation code: ")
        # 3b. Receive the authorisation bundle/access token
        access_token_package = self.X_Client.fetch_access_token('https://api.x.com/oauth/access_token', authorisation_code)

        # Append to the .env file.
        with open(".env", "a") as envFile: 
            envFile.write("\n")
            envFile.write(f"TWITTER_OAUTH_USER_TOKEN={access_token_package['oauth_token']}\n")
            envFile.write(f"TWITTER_OAUTH_USER_SECRET={access_token_package['oauth_token_secret']}\n")

            # Recreate/Update the Session
            self.X_Client = OAuth1Session(
                client_key=os.getenv("TWITTER_API_KEY"),
                client_secret=os.getenv("TWITTER_API_KEY_SECRET"),
                resource_owner_key=os.getenv("TWITTER_OAUTH_USER_TOKEN"),
                resource_owner_secret=os.getenv("TWITTER_OAUTH_USER_SECRET"),
                callback_uri="oob"
            )