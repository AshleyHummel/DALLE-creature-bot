import tweepy

# environment variables
import os
# import .env file
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import requests
from bs4 import BeautifulSoup

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

# GETTING CREATURE PROMPT FROM https://artprompts.org/creature-prompts/
# (from https://www.freecodecamp.org/news/web-scraping-python-tutorial-how-to-scrape-data-from-a-website/ )
page = requests.get('https://artprompts.org/creature-prompts/')

soup = BeautifulSoup(page.content, 'html.parser')
second_p_text = soup.select('p')[1].text # text of second p element (THE PROMPT)
print(second_p_text)