from bs4 import beautifulsoup
import requests
try:
    page = requests.get("https://twitter.com/adhikaritaiwan")
    soup = beautifulsoup(page.content, 'html.parser')
    all_item = soup.find_all(class_="content")

for content in all_item:
    tweet_text = content.find(class_="js-tweet-text-contains")
    print(tweet_text)
except Exception as ex:
    print("Couldn't connect to twitter")
    