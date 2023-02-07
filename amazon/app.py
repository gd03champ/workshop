from flask import Flask, request, render_template
from time import sleep
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_product_details(url):
    
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"} 

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")


    with open("templates/scrapped.html","w") as html_file:
        html_file.write(str(soup))
        html_file.close()


    #extract the product details from the page
    title = soup.find("span", id="productTitle").text.strip()
    price = soup.find("span", id="priceblock_ourprice").text.strip()
    image_url = soup.find("img", id="landingImage")["data-old-hires"]
    
    # return the product details as a dictionary
    return {
        "title": title,
        "price": price,
        "image_url": image_url
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']

        try:
            
            product_details = get_product_details(url)

        except Exception as e:
            return render_template("scrapped.html")

        return render_template('index.html', product_details=product_details)

    return render_template('index.html')
if __name__ == '__main__':
    app.run()