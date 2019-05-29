import os
import json
import pprint
import requests
from creds.creds import apikey
# http://ws.audioscrobbler.com/2.0/?method=user.getinfo&user=rj&api_key=YOUR_API_KEY&format=json

BASE_URL = "http://ws.audioscrobbler.com/2.0/"

method = "user.getinfo"
user = "recoilmoney"
format_ = "json"

req = f"{BASE_URL}?method={method}&user={user}&api_key={apikey}&format={format_}"
if not os.path.exists("data.json"):
	r = requests.get(req)
	if r.status_code == 200:
		data = r.json()
		with open('data.json', 'w') as f:
			json.dump(data, f)
else:
	data = json.load(open('data.json','r'))
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(data)
