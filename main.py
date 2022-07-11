import tweepy

# environment variables
import os
# import .env file
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import requests
from bs4 import BeautifulSoup

import urllib
import urllib.request
from selenium import webdriver # for navigating DALLE mini
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

# (code from https://realpython.com/twitter-bot-python-tweepy/ )
# AUTHENTICATE TO TWITTER
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
# (code from https://www.freecodecamp.org/news/web-scraping-python-tutorial-how-to-scrape-data-from-a-website/ )
page = requests.get('https://artprompts.org/creature-prompts/')

soup = BeautifulSoup(page.content, 'html.parser')
creature_prompt = soup.select('p')[1].text # text of second p element (THE PROMPT)
print("Prompt:", creature_prompt)

# INPUT PROMPT INTO DALLE MINI/CRAIYON (https://www.craiyon.com/)

s = Service('/Applications/chromedriver') # changed to avoid DeprecationWarning
driver = webdriver.Chrome(service=s)

driver.get("https://www.craiyon.com/")

prompt_input = driver.find_element(By.ID, "prompt")
prompt_input.send_keys(creature_prompt)
time.sleep(70) # delay (seconds) to let DALLE mini generate an image

# RETRIEVE ONE OF THE IMAGES AND SAVE TO FOLDER

images = driver.find_elements(By.XPATH, '//img') # gets list of images on DALLE mini site
img_path = "/Users/ashleyhummel/Desktop/creature_bot_images"
file_name = creature_prompt + ".png"
full_file_name = os.path.join(img_path, file_name)

src = images[3].get_attribute('src') # images[3] is the FIRST generated image
urllib.request.urlretrieve(src, full_file_name) # save image to specific folder with a file name

driver.quit()

# POST TO TWITTER :D

media = api.media_upload(img_path + "/" + file_name)

# post tweet
api.update_status(status=creature_prompt, media_ids=[media.media_id])