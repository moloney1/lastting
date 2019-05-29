import os
import json
import pprint
import requests
from creds.creds import apikey

BASE_URL = "http://ws.audioscrobbler.com/2.0/"

method = "user.getrecenttracks"
user = "recoilmoney"
format_ = "json"
limit = "10"

# return list of (artist, title, url)
def get_recent(limit):

	recent_tracks = []

	payload = {
		"method": "user.getrecenttracks",
		"user": user,
		"limit": limit,
		"api_key": apikey,
		"format": format_
	}

	pp = pprint.PrettyPrinter(indent=4)
	
	if not os.path.exists('data.json'):
		r = requests.get(BASE_URL, params=payload)
		data = r.json()
		with open("data.json", "w") as f:
			json.dump(data, f)
	else:
		print("loading from file..")
		data = json.load(open("data.json", "r"))
	#pp.pprint(data)	
	tracks = data["recenttracks"]["track"]
	for track in tracks:
		artist = track["artist"]["#text"]
		name = track["name"]
		url = track["url"]

		recent_tracks.append((artist, name, url))

		print(f"Track: {name}")
		print(f"Artist: {artist}")
		print(f"URL: {url}")

if __name__ == "__main__":
	get_recent(1)
