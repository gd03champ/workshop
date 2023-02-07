from bs4 import BeautifulSoup
import requests
import lxml
import csv

url = "https://webscraper.io/test-sites/tables"
response = requests.get(url).text

soup = BeautifulSoup(response,"lxml")

#print(soup)

tables = soup.find_all(("table"))

table_1 = tables[0]

table_1_heading = []

for _ in (table_1.find("thead").find("tr").find_all("th")): table_1_heading.append(_.get_text())

with open("table.csv","w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(table_1_heading)
    csv_file.close()

print(table_1_heading,"-> Heading written to csv")

table_1_body = table_1.find("tbody").find_all("tr")

for i in table_1_body:
    content = []
    for _ in (i.find_all("td")): content.append(_.get_text())
    with open("table.csv","a") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(content)
        print(content,"-> row written")
        csv_file.close()
    
