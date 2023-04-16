# import urllib library 
# from urllib.request import urlopen

# import json module
import json

# store the URL in url as parameter for urlopen 
# url = "https://data.cdc.gov/api/views/25m4-6qqq/rows.json"

# store the response of URL 
# response = urlopen(url)

# storing the JSON response from url in data
# data_json = json.loads(response.read())

# read local JSON file & load as Python object
cdc_file = open("cdcData.json", "r")
cdc = json.load(cdc_file)

# filter out only the data
meta = cdc['meta']
data = cdc['data']

print(data[8:14])

# iterate over lines to find just outcomes and data
# I'm trying to slice the lists by index, but I don't know how to find the index of such a long list
for Row in data:
    outcome = data[7194][8]
    group = data[7194][9]
    # if outcome == "Wellness visit":
    print(f"outcome: {outcome}\n group: {group}")

# read through the file line by line
# lines = data.readlines()
# readlines() does not work on list object

# for L in lines:
#     print(lines)

# just_data = cdc_data['data']


# print the json response
# print(f"lines is a {type(lines)}")


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
