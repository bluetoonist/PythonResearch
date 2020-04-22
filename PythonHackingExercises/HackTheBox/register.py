import requests

url = "https://www.hackthebox.eu/api/invite/generate"

r = requests.post(url)

print(r.text)