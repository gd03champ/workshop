from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_product_details(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find('span', {'id': 'productTitle'}).get_text().strip()
    price = soup.find('span', {'id': 'priceblock_ourprice'}).get_text().strip()
    availability = soup.find('div', {'id': 'availability'}).get_text().strip()
    rating = soup.find('span', {'class': 'rating-star-rating'}).get_text().strip()
    return {'Title': title, 'Price': price, 'Availability': availability, 'Rating': rating}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        product_details = get_product_details(url)
        return render_template('index.html', product_details=product_details)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
