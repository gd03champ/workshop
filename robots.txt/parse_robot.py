from urllib.robotparser import RobotFileParser

def check_robots(url):
    parser = RobotFileParser()
    parser.set_url(url + '/robots.txt')
    parser.read()
    return parser

# Example usage
website_url = "https://amazon.in"
parser = check_robots(website_url)

if parser.can_fetch("*", website_url+"/some-page"):
    print("This page can be scraped.")
else:
    print("This page cannot be scraped.")