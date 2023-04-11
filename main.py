# import urllib library 
from urllib.request import urlopen

# import json 
import json

# store the URL in url as parameter for urlopen 
url = "https://data.cdc.gov/api/views/25m4-6qqq/rows.json"

# store the response of URL 
response = urlopen(url)

# storing the JSON response from url in data
data_json = json.loads(response.read())

# print the json response 
print(data_json)


# convert numerical strings


# What percentage of adults in the 18–34-year age range saw a doctor
# for a “Wellness Visit” in 2019 and 2020?


# Which group of adults had the highest percentage of “Obesity” in 2020?


# which groups of adults had an increased percentage of
# “Difficulty communicating” from 2019 to 2020?
