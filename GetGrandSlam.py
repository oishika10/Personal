import requests
from bs4 import BeautifulSoup

#urls for us, aus, and english open
usopen_URL = "https://www.grandslamtennistours.com/us-open/schedule-of-play"
wimbledon_URL ="https://www.grandslamtennistours.com/wimbledon/schedule-of-play"
ausopen_URL ="https://www.grandslamtennistours.com/australian-open/schedule-of-play"

#GET requests to the URLs 
try:
	pageUSOpen = requests.get(usopen_URL)
except:
	print("Couldn't check schedules for US Open")

try:
	pageWimbledon = requests.get(wimbledon_URL)
except:
	print("Couldn't check schedules for Wimbledon")


try:
	pageausOpen = requests.get(ausopen_URL)
except:
	print("Couldn't check schedules for Australian Open")



soup = BeautifulSoup(pageUSOpen.content, "html.parser")
results = soup.find("tbody")
newFile = open("/Users/oishikachaudhury/Downloads/schedule-of-play.txt", "w")

print(results)














