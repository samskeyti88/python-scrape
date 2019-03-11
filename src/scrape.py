# #coding: utf-8
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)

url = 'https://www.tv-asahi.co.jp/ametalk/backnumber/'

driver.get(url)
html = driver.page_source.encode('utf-8')
soup = BeautifulSoup(html, "html.parser")
print(soup.select_one("#backnumber > ul.column-3-box.clearfix > li.row1141.rowall > a > p"))
