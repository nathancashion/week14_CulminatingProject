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

# filter out only the data
cdc_data = json.load(cdc_file)
just_data = cdc_data['data']

# read through the file line by line
lines = just_data.readlines()

# print the json response
print(lines)
print(f"cdc_file is a {type(cdc_file)}")
print(f"lines is a {type(lines)}")


# extract only the meaningful data


# What percentage of adults in the 18–34-year age range saw a doctor
# for a “Wellness Visit” in 2019 and 2020?
# def wellnessVisit ():
#     if meaningfulData[14] == "2019" or "2020":

# Which group of adults had the highest percentage of “Obesity” in 2020?
# def obesity():

# which groups of adults had an increased percentage of
# “Difficulty communicating” from 2019 to 2020?


cdc_file.close()