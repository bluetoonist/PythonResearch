import wget
import requests

import ssl
import urllib.request
import urllib3
from bs4 import BeautifulSoup

from bs4 import BeautifulSoup
# Setting SSL Certificate Error
ssl._create_default_https_context = ssl._create_unverified_context
urllib3.disable_warnings()
context = ssl._create_unverified_context()

web1 = requests.get("https://velog.io")
soup = BeautifulSoup(web1.content, "html.parser")

find_content = soup.find("div",{"class":"sc-eqIVtm gLLJLX"})
find_img_content = find_content.find_all("img")

reg_url="https://cdn.hasselblad.com/samples/x1d-II-50c/x1d-II-35-75-sample-05.jpg"

print(reg_url)
# urllib.request.urlretrieve(reg_url, "C:\\Users\\Jan\\Downloads\\test.jpg")
wget.download(reg_url)
exit()
for x in find_img_content:
    try:
        url = x.attrs['src']
        print(url)
        wget.download(url)
    except:
        pass