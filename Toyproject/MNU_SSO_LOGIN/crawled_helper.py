from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
from datetime import datetime

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "./chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)

cmp_data = str(datetime.today().year)+"-"+str(datetime.today().month)+"-"+str(datetime.today().day)

local_year = str(datetime.today().year)
local_month = str(datetime.today().month)
local_day = str(datetime.today().day)

str(datetime.today().year)+"-"+str(datetime.today().month)+"-"+str(datetime.today().day)

message_html = driver.page_source

soup = BeautifulSoup(message_html,"html.parser")

# zoom link find it
find_msg_log = soup.find("div",{"class":"media-body"})
find_zoom_log = find_msg_log.find("div",{"class":"msg"})

print(find_zoom_log.text)






