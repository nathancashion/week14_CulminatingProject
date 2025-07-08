# CDC Website Data Analysis Project
## MSHI HTLI06200 Culminating Project

This project was the final assignment for the Data Analytics course as part of the MS Health Informatics at Logan University.
All code was created by me in Visual Studio Code. 

### Assignment Instructions
https://logan.instructure.com/courses/12005/assignments/200616?module_item_id=491610
Due Apr 16 by 9:59pm CT

For the culminating project, you will be coupling your new knowledge of JSON with your existing knowledge of dictionaries, lists, variables, conditional statements, and writing scripts to answer real-world questions based on data collected and provided by the CDC.

A description of this CDC data set is available at: https://data.cdc.gov/NCHS/NHIS-Adult-Summary-Health-Statistics/25m4-6qqq

A copy of the data is [available here for download.](https://logan.instructure.com/courses/12005/files/2806311?wrap=1)

## Want a Challenge? 

If you're up for a challenge, your script can get the same data directly from the [CDC website](https://data.cdc.gov/api/views/25m4-6qqq/rows.json?accessType=DOWNLOAD).  Try it out! 

Your script should answer the following questions using the data:
1. What percentage of adults in the 18–34-year age range saw a doctor for a “Wellness Visit” in 2019 and 2020?
2. According to the data, which group of adults had the highest percentage of “Obesity” in 2020?
3. According to the data, which groups of adults had an increased percentage of “Difficulty communicating” from 2019 to 2020? Note that classifications of adults may differ from year to year, so you should include in the comparison only those groups that appeared in both the 2019 and 2020 data.

A few notes:
- You'll need to spend some time with the JSON data before you start coding to understand how it is structured.
- The first block of data, entitled “meta,” describes information included in the data and how to interpret it.
- The second portion, entitled “data,” is the raw information from 2019 and 2020.
- You will likely need to spend time reviewing the “meta” information, and your script will consume data elements from the “data” section.
- Real-world data often has problems. Your script will need to account for these problems and work around them. For example, most measurements in this dataset contain a percentage and a confidence range. All percentages should be more than 0 and less than 100 and should fall within the confidence range, or they should be excluded. If a measurement does not have a confidence range, then it should also be excluded.
- This dataset has numbers expressed as strings instead of their native type. You should convert them to float or int as appropriate if you want to perform numerical comparisons on them.

### Grading Considerations

The script should print answers to each of the three questions.

The script should use only the data contained in the JSON file to make its determination. No other data sources or “hard-coding” is permitted.

See the culminating project rubric for grading details.
