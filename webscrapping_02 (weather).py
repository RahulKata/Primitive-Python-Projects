import requests
from bs4 import BeautifulSoup
from datetime import date
import csv

# =============================================================================
# make sure to 
# * pip install bs4 *
# before you proceeeeeeeed
# =============================================================================

source = requests.get('https://weather.com/en-IN/weather/5day/l/95a2e56497334f82741c004c34cbcb998bfd844467774100fff97db31ceef064').text
soup = BeautifulSoup(source,'lxml')

# =============================================================================
# all the commented code below is just a part of my experimentation
# you too can uncomment part by part and experiment yourselves
# =============================================================================

# print(soup.prettify())

# temp_range = soup.find_all(class_="temp")
# del(temp_range[0])
# for i in temp_range:
#     print(i.text)
#
# date = soup.find_all(class_="day-detail")
# for i in date:
#     print(i.text)
#
# humidity = soup.find_all(class_="humidity")
# del(humidity[0])
# for i in humidity:
#     print(i.text)

# csv_file = open('weather_scrape.csv','w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['Day','Date','Description','Temp. Range','Precipitation','Wind','Humidity'])

l=[]
table=soup.find_all("table",class_="twc-table")
for items in table:
	for i in range(len(items.find_all("tr"))-1):
		d = {}
		try:
			d["day"]=items.find_all("span",class_="date-time")[i].text
			d["date"]=items.find_all("span",class_="day-detail")[i].text
			d["desc"]=items.find_all("td",class_="description")[i].text
			d["temp"]=items.find_all("td",class_="temp")[i].text
			d["precip"]=items.find_all("td",class_="precip")[i].text
			d["wind"]=items.find_all("td",class_="wind")[i].text
			d["humidity"]=items.find_all("td",class_="humidity")[i].text
		except:
			d["day"]="None"
			d["date"]="None"
			d["desc"]="None"
			d["temp"]="None"
			d["precip"]="None"
			d["wind"]="None"
			d["humidity"]="None"
		print(d)
		l.append(d)


import pandas
df = pandas.DataFrame(l)
print(df)
df.to_csv("weather_scrape.csv")

# =============================================================================
# this csv file will be created and saved in the cwd (current working directory)
# =============================================================================
