

from selenium import webdriver
from bs4 import BeautifulSoup

from time import sleep


driver =webdriver.Chrome("./chromedriver.exe")

# SSO POTAL
driver.get("https://mnuwb.mokpo.ac.kr/uat/uia/loginForm.do?site_preference=normal")
sleep(0.3)
driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div/ul[1]/li[2]/a").click()
sleep(0.4)
driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div/div[1]/div/form/fieldset/p[1]/input").send_keys("bluetoon")
sleep(0.5)
driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div/div[1]/div/form/fieldset/p[2]/input").send_keys("kojian132!mokpo")
sleep(0.6)
driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div/div[1]/div/form/fieldset/button").click()
sleep(0.7)
driver.implicitly_wait(2)
driver.get("https://lms.mokpo.ac.kr/sso/index.php")
driver.implicitly_wait(2)
driver.get("https://lms.mokpo.ac.kr/local/ubmessage/")
driver.implicitly_wait(2)
sleep(2)
top_message = driver.page_source
print(top_message)



sleep(2)
driver.close()