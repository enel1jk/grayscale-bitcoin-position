#%%
import json
import requests
import datetime

with open('responses.txt') as f:
    for line in f:
        tweets = json.loads(line)["globalObjects"]["tweets"]
        for _, value in tweets.items():
            date = value["full_text"][0:8].split()[0]   # 11/12/20
            date_s = date.split('/')
            date = datetime.datetime(int("20"+date_s[2]), int(date_s[0]), int(date_s[1])).strftime("%Y%m%d") # 20201112
            img_url = value["entities"]["media"][0]["media_url"]
            ext = img_url.rsplit('.', 1)[1]
            filename = f"{date}.{ext}"

            print(f"{date} - {img_url}")
            print(filename)
            
            with open(filename, 'wb') as handle:    # download image
                    response = requests.get(img_url, stream=True)
                    if not response.ok:
                        print(response)
                    for block in response.iter_content(1024):
                        if not block:
                            break
                        handle.write(block)