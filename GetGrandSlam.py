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

#use Beautiful Soup to parse through content by tag
soup = BeautifulSoup(pageUSOpen.content, "html.parser")
results = soup.find("tbody")
newFile = open("/Users/oishikachaudhury/Downloads/schedule-of-play.txt", "w")

#While this part is not entirely essential, it does make some elementary file processing easier
for line in results:
	newFile.write(str(line))
newFile.close()

schedules = []
readfile = open("/Users/oishikachaudhury/Downloads/schedule-of-play.txt", "r")

readfile.readline()

for line in readfile:
	if line[:3] == "<th":
		#process for date
		start = line.find(">")
		end =  line.find(" ",start + 10)
		date = line[start+5:end].strip(" ")
		for i in range(3):
			print(readfile.readline())
		#process for time
		line = readfile.readline()
		start = line.find(">")
		end =  line.find("<",start + 1)
		time = line[start+1:end].strip(" ")
		


