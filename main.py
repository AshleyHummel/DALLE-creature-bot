import webbrowser
import tweepy
import logging

# environment variables
import os
# import .env file
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

logger = logging.getLogger()

# (code from https://realpython.com/twitter-bot-python-tweepy/ )
# authenticate to Twitter
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_secret = os.getenv("ACCESS_SECRET")


auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)
# create API object
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication successful")
except:
    print("Authentication failed")
