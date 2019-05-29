import requests
#from creds/creds import apikey
from creds.creds import apikey
print(apikey)
# http://ws.audioscrobbler.com/2.0/?method=user.getinfo&user=rj&api_key=YOUR_API_KEY&format=json

BASE_URL = "http://ws.audioscrobbler.com/2.0/"

method = "user.getinfo"
user = "recoilmoney"
format_ = "json"

req = f"{BASE_URL}?method={method}&user={user}&api_key={apikey}&format={format_}"
r = requests.get(req)
print(r.status_code)
