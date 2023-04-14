# import urllib library 
from urllib.request import urlopen

# import json 
import json

# store the URL in url as parameter for urlopen 
# url = "https://data.cdc.gov/api/views/25m4-6qqq/rows.json"

# store the response of URL 
# response = urlopen(url)

# storing the JSON response from url in data
# data_json = json.loads(response.read())

# import local JSON file
cdc_file = open("cdcData.json", "r")

# read through the file line by line
lines = cdc_file.readlines()

# print the json response
print(f"cdc_file is a {type(cdc_file)}")
print(f"lines is a {type(lines)}")

# create a list of only the data
cdc_data = lines[1:]

print(type(cdc_data))

# extract only the meaningful data
meaningfulData = cdc_data[8:]

print(meaningfulData)


# What percentage of adults in the 18–34-year age range saw a doctor
# for a “Wellness Visit” in 2019 and 2020?
def wellnessVisit ():
    if meaningfulData[14] == "2019" or "2020":



# Which group of adults had the highest percentage of “Obesity” in 2020?
# def obesity():

# which groups of adults had an increased percentage of
# “Difficulty communicating” from 2019 to 2020?
