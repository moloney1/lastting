import os
import json
import pprint
import requests
from collections import namedtuple
from creds.creds import apikey, user

method = "user.getrecenttracks"
format_ = "json"
BASE_URL = "http://ws.audioscrobbler.com/2.0/"

pp = pprint.PrettyPrinter(indent=4)
TrackInfo = namedtuple("TrackInfo", "artist, name, url")

def base_request():
	payload = {
		"user": user,
		"api_key": apikey,
		"format": format_
	}
	return payload

# return list of (artist, title, url)
def get_recent(limit):

	tracklist = []

	payload = {
		"method": "user.getrecenttracks",
		"limit": limit
	}
	payload.update(base_request())
#	print(payload)
	
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

		tracklist.append(TrackInfo._make((artist, name, url)))

	#	print(f"Track: {name}")
	#	print(f"Artist: {artist}")
	#	print(f"URL: {url}")
	
	return tracklist

# return list of (artist, title, url)
def get_top(limit):
	
	tracklist = []	

	period = "7day"

	payload = {
		"method": "user.gettoptracks",
		"limit": limit,
		"period": period
	}
	payload.update(base_request())
	
	if not os.path.exists('data_top.json'):
		r = requests.get(BASE_URL, params=payload)
		data = r.json()
		with open("data_top.json", "w") as f:
			json.dump(data, f)
	else:
		print("loading from file..")
		data = json.load(open("data_top.json", "r"))
#	pp.pprint(data)
	
	top_tracks = data["toptracks"]["track"]
	for track in top_tracks:
		artist = track["artist"]["name"]
		name = track["name"]
		url = track["url"]
		tracklist.append(TrackInfo._make((artist, name, url)))

	return tracklist

if __name__ == "__main__":
	recent = get_recent(5)
	top = get_top(5)
	
	print("Recent Tracks:")
	for track in recent:
		print(f"{track.artist} - {track.name}")
	print("Top Tracks:")
	for track in top:
		print(f"{track.artist} - {track.name}")

