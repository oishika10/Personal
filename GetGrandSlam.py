import requests
from bs4 import BeautifulSoup

URL = "https://www.grandslamtennistours.com/us-open/schedule-of-play"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("th", class_="main-content wysiwyg-content")
print(results)




