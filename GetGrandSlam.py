import requests
from bs4 import BeautifulSoup

dateConversionDict = {"Mon":"Monday", "Tue":"Tuesday", "Wed":"Wednesday", "Thu":"Thursday","Fri":"Friday"}
monthConversionDict = {"Jan" : "January", "Feb": "February", "Mar": "March", "Apr": "April", "May":"May", \
"Jun":"June", "Jul":"July", "Aug":"August", "Sep":"September", "Aug":"August", "Sep":"September", "Oct":"October", "Nov":"November"}

def string_reverse(date):
	space = date.find(" ")
	returnString = date[space+1:] + date[:space]
	return returnString





#urls for us, aus, and english open
usopen_URL = "https://www.grandslamtennistours.com/us-open/schedule-of-play"
wimbledon_URL ="https://www.grandslamtennistours.com/wimbledon/schedule-of-play"
ausopen_URL ="https://www.grandslamtennistours.com/australian-open/schedule-of-play"

#GET request for US Open schedule of play
try:
	pageUSOpen = requests.get(usopen_URL)
except:
	print("Couldn't check schedules for US Open")

#GET request for Wimbledon schedule of play
try:
	pageWimbledon = requests.get(wimbledon_URL)
except:
	print("Couldn't check schedules for Wimbledon")

#GET request for Australian Open schedule of play
try:
	pageausOpen = requests.get(ausopen_URL)
except:
	print("Couldn't check schedules for Australian Open")

#use Beautiful Soup to parse through content by tag
soup = BeautifulSoup(pageUSOpen.content, "html.parser")
results = soup.find("tbody")
newFile = open("/Users/oishikachaudhury/Downloads/schedule-of-play.txt", "w")

#Write to file in order to convert byte to string
#While this line is not essential, it does make some elementary file processing easier
for line in results:
	newFile.write(str(line))
newFile.close()

schedules = []
readfile = open("/Users/oishikachaudhury/Downloads/schedule-of-play.txt", "r")
readfile.readline()

for line in readfile:
	if line[:3] == "<th":
		#process for date and day
		start = line.find(">")
		day = line[start+1:start+4]
		end =  line.find(" ",start + 10)
		date = line[start+5:end].strip(" ")
		for i in range(2):
			readfile.readline()
		
		#process for time
		line = readfile.readline()
		start = line.find(">")
		end =  line.find("<",start + 1)
		time = line[start+1:end].strip(" ")
		readfile.readline()
		
		#process for what match it is
		line = readfile.readline()
		start = line.find(">")
		end =  line.find("<",start + 1)
		featuredPlay = line[start+1:end].strip(" ")
		#add to list
		schedules.append([day, date, time, featuredPlay])


#now add this stuff to reminders

command = "tell application \"Reminders\" to make new reminder at end \
with properties {due date:date \"Thursday, July 10, 2014 at 3:00:00 PM\", \
body:\"This is a note for the reminder\"}"

#----------------------------------------- for Wimbledon ----------------------------------------------------------------------------------------
#use Beautiful Soup to parse through content by tag
soup = BeautifulSoup(pageWimbledon.content, "html.parser")
results = soup.find("tbody")
newFile = open("/Users/oishikachaudhury/Downloads/schedule-of-play.txt", "w")

#Write to file in order to convert byte to string
for line in results:
	newFile.write(str(line))
newFile.close()

schedules = []
readfile = open("/Users/oishikachaudhury/Downloads/schedule-of-play.txt", "r")
readfile.readline()


for line in readfile:
	if line[:3] == "<th":
		#process for date and date
		start = line.find(">")
		day = line[start+1:start+4]
		end =  line.find(" ",start + 10)
		date = line[start+5:end].strip(" ")
		for i in range(3):
			readfile.readline()
		
		#process for time
		line = readfile.readline()
		start = line.find(">")
		end =  line.find("<",start + 1)
		time = line[start+1:end].strip(" ")
		
		#process for what match it is
		line = readfile.readline()
		start = line.find(">")
		end =  line.find("<",start + 1)
		featuredPlay = line[start+1:end].strip(" ")
		#add to list
		schedules.append([day, date, time, featuredPlay])


print(schedules)
'''
Additional file processing is required for Australian Open matches 
'''
#add Wimbledon to reminders

