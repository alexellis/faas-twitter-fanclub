import requests
import json
import base64
import redis
import os

def handle(st):
    # parse Github event
    req = json.loads(st)

    minutes = 1
    minutes_val = os.getenv("cache-minutes")
    if minutes_val != None:
        minutes = int(minutes_val)

    loginName = req["sender"]["login"]

    try:
        redis_client = redis.StrictRedis("redis")
        redis_key = "tweet-" + loginName

        cached = redis_client.get(redis_key)

        if cached != None:
            print(loginName + " attempted to trigger event again before cache expired. Extending cache timeout.")
            redis_client.setex(redis_key, 60 * minutes, "1")
            return

        redis_client.setex(redis_key, 60 * minutes, "1")
    except Exception:
        print("Redis may be down or errored")

    # download the avatar binary using getavatar function
    r = requests.post("http://gateway:8080/function/get-avatar", json=req)

    res = r.json()

    # Figure out the correct extension for the avatar.
    ext = ".jpg"
    if res["contentType"] == "image/png":
        ext = ".png"

    # Take the encoded image and turn into binary bytes
    imageData = base64.standard_b64decode(res["content"])
    put_url = "http://minio-shim:8080/put/" + loginName + ext
    # Store in the fan-club photo gallery
    r1 = requests.post(put_url, data= imageData)

    gazer = {}
    gazer["login"] = loginName
    gazer["filename"] = loginName + ext

    r2 = requests.post("http://gateway:8080/function/tweetstargazer", json.dumps(gazer))

    club_res = {}
    club_res["put_url"] = put_url
    club_res["tweet_result"] = r2.text
    club_res["status"] = "success"
    club_res["username"] = req["sender"]["login"]
    club_res["bytes"] = len(imageData)

    # Useful for logging, GitHub's invoker will receive this string
    print(json.dumps(club_res))
