import requests

def check_robots(url):
    # Send an HTTP request to the robots.txt file
    robots = requests.get(url + "/robots.txt", headers={'User-agent': 'myBot'})
    # Check if the request was successful
    if robots.status_code == 200:
        return robots.text
    else:
        return None

website_url = "https://www.amazon.com"
robots_txt = check_robots(website_url)

if robots_txt:
    print(robots_txt)
else:
    print("No robots.txt file found.")