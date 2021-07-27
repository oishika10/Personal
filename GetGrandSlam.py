import requests
from bs4 import BeautifulSoup

#urls for us, aus, and english open
usopen_URL = "https://www.grandslamtennistours.com/us-open/schedule-of-play"
wimbledon_URL ="https://www.grandslamtennistours.com/wimbledon/schedule-of-play"
ausopen_URL ="https://www.grandslamtennistours.com/australian-open/schedule-of-play"

#GET requests to the URLs
pageUSOpen = requests.get(usopen_URL)
pageWimbledon = requests.get(wimbledon_URL)
pageAusOpen = requests.get(ausopen_URL)

#!TODO --> try and error block for get 

soup = BeautifulSoup(pageUSOpen.content, "html.parser")
results = soup.find(class_="main-content wysiwyg-content")
newFile = open("/Users/oishikachaudhury/Downloads/schedule-of-play.txt", "w")

for line in results:
	newFile.write(str(line))
newFile.close()



