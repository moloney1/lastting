import os
import json
import pprint
import requests
from creds.creds import apikey

method = "user.getrecenttracks"
user = "recoilmoney"
format_ = "json"
limit = "10"
BASE_URL = "http://ws.audioscrobbler.com/2.0/"

pp = pprint.PrettyPrinter(indent=4)

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
	
	if not os.path.exists('data.json'):
		r = requests.get(BASE_URL, params=payload)
		data = r.json()
		with open("data.json", "w") as f:
			json.dump(data, f)
	else:
		print("loading from file..")
		data = json.load(open("data.json", "r"))
	
	tracks = data["recenttracks"]["track"]
	for track in tracks:
		artist = track["artist"]["#text"]
		name = track["name"]
		url = track["url"]

		recent_tracks.append((artist, name, url))

		print(f"Track: {name}")
		print(f"Artist: {artist}")
		print(f"URL: {url}")

def get_top(limit):
	period = "7day"
	
	payload = {
		"method": "user.gettoptracks",
		"user": user,
		"limit": limit,
		"period": period,
		"api_key": apikey,
		"format": format_
	}
	if not os.path.exists('data_top.json'):
		r = requests.get(BASE_URL, params=payload)
		data = r.json()
		with open("data_top.json", "w") as f:
			json.dump(data, f)
	else:
		print("loading from file..")
		data = json.load(open("data_top.json", "r"))
	pp.pprint(data)
	
	top_tracks = data["toptracks"]["track"]
	for track in top_tracks:
		artist = track["artist"]["name"]
		name = track["name"]
		url = track["url"]

		print(f"Track: {name}")
		print(f"Artist: {artist}")
		print(f"URL: {url}")
	

if __name__ == "__main__":
#	get_recent(1)
	get_top(1)
