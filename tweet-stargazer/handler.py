import tweepy
import os
import requests
import json

def handle(st):
    req = json.loads(st)

    auth = tweepy.OAuthHandler(os.environ["consumer_key"], os.environ["consumer_secret"])
    auth.set_access_token(os.environ["access_token"], os.environ["access_token_secret"])

    api = tweepy.API(auth)

    file_name = req["filename"]
    
    r = requests.get("http://minio-shim:8080/get/"+file_name)
    f = open("/tmp/"+file_name, 'wb')
    f.write(r.content)
    f.close()

    api.update_with_media("/tmp/"+file_name, req["login"] + " is a star-gazer for OpenFaaS")

    # Log the results
    print("Tweet sent")

    os.remove("/tmp/"+file_name)
