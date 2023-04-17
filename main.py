# import json module
import json

# import urllib library
from urllib.request import urlopen

# store the URL in url as parameter for urlopen
url = "https://data.cdc.gov/api/views/25m4-6qqq/rows.json"

# store the response of URL 
response = urlopen(url)

# storing the JSON response from url in data
cdc = json.loads(response.read())

# read local JSON file & load as Python object
# cdc_file = open("cdcData.json", "r")
# cdc = json.load(cdc_file)

# filter out only the data
meta = cdc['meta']
data = cdc['data']

# cdc_file.close()

# iterate over lines to find just outcomes and data

# read through the file line by line
# lines = data.readlines()
# readlines() does not work on list object

# for L in lines:
#     print(lines)


# print the json response
# print(f"lines is a {type(lines)}")


# extract only the meaningful data


# What percentage of adults in the 18–34-year age range saw a doctor
# for a “Wellness Visit” in 2019 and 2020?
def wellnessVisit ():
    percentage2019 = 0
    percentage2020 = 0
    for Row in data:
        if Row[8] == "Wellness visit" and Row[9] == "18-34 years":
            if Row[14] == "2019":
                percentage2019 = Row[10]
            elif Row[14] == "2020":
                percentage2020 = Row[10]
            else:
                percentage = 0
    print(f"For the 18-34 year-old age group, the percentage of Wellness visits in 2019 was {percentage2019}%")
    print(f"For the 18-34 year-old age group, the percentage of Wellness visits in 2020 was {percentage2020}%")

# Which group of adults had the highest percentage of “Obesity” in 2020?
def obesity():
    highest = 0
    group = "None"

    for Row in data:
        if Row[14] == "2020" and Row[8] == "Obesity":
            if float(Row[10]) > highest and float(Row[10])< 101:
                highest = float(Row[10])
                group = Row[9]
                percentage = Row[10]
    print(f"The group with the highest percentage of Obesity in 2020 was {group} at {percentage}%.")

# which groups of adults had an increased percentage of
# “Difficulty communicating” from 2019 to 2020?
def difficultyComms():
    diff = 0.0
    groupList = [["Group", "Difference"]]
    for Row in data:
        if Row[8] == "Difficulty communicating" and Row[14] == "2020":
            pct_diff_2020 = float(Row[10])
            group = Row[9]
            for NextRow in data:
                if NextRow[9] == group and NextRow[14] == "2019":
                    pct_diff_2019 = float(NextRow[10])
                    diff = pct_diff_2020 - pct_diff_2019
                    if diff > 0.0:
                        groupList.append([group, diff])
    print("The groups who had increased difficulty communicating from 2019 to 2020 were:")
    for i in groupList:
        print(f"    {i[0]}, ({i[1]})")



if __name__ == '__main__':
    wellnessVisit()
    obesity()
    difficultyComms()