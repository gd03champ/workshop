import requests
from bs4 import BeautifulSoup
import lxml

url = "https://webscraper.io/test-sites/tables"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

response  = requests.get(url, headers=headers).text

soup = BeautifulSoup(response,"lxml")

#print(str(soup))

#printing header
heading = soup.find("h1").get_text()

print(heading)

#printing all titles
titles = soup.find_all("h2")

for i in titles:
    print(i.get_text())

#retriving sub tags

tables = soup.find_all("table")
table = tables[0]
contents = table.find("thead").find("tr").find_all("th")
for i in contents: print(i.get_text())


#retriving using other than tags

title_image = soup.find(class_="navbar-brand").find("a").find("img")
title_image_link = title_image["src"]
title_image_alt = title_image["alt"]

print(title_image_link+"\n"+title_image_alt)

#socila media division

smedia = soup.find(class_="smedia").find_all("li")

for i in range(len(smedia)): print(smedia[i].find("a")["href"])







