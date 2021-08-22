import requests
from bs4 import BeautifulSoup

url = 'https://www.washingtonpost.com/dc-md-va/2021/08/20/wise-brothers-afganistan-taliban/'
response = requests.get(url)
soup = BeautifulSoup(response.text, features="html.parser")

metas = soup.find_all('meta')

people_to_tweet = []
clean_url = None
author = None
title = None

for meta in metas:
    meta_name = meta.get("property", None) or meta.get("name", None)
    
    ### Match Author
    if meta_name == "author":
        author = meta.get("content", None)
    if meta_name == "og:author" and author is None:
        author = meta.get("content", None)
    if meta_name == "article:author" and author is None:
        author = meta.get("content", None)

    ### Match Title
    if meta_name == "title":
        title = meta.get("content", None)
    if meta_name == "og:title" and title is None:
        title = meta.get("content", None)
    if meta_name == "article:title" and title is None:
        title = meta.get("content", None)

    if meta_name == "twitter:creator":
        people_to_tweet.append(meta.get("content", None))
    if meta_name == "twitter:site":
        people_to_tweet.append(meta.get("content", None))
    if meta_name == "og:url":
        clean_url = meta.get("content", None)

print(author)
print(people_to_tweet)
print(clean_url)
print(title)