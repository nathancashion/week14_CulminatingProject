# [[Culminating Project]] Notes

I'm really struggling with this final project. We've lightly touched on many concepts but haven't learned how to combine them together for a more complex project.

### JSON
In week 12, we watched a demonstration on how to import the JSON module and read a JSON file. It was just a small file with a single entry and a few variables and then a method to create a separate small file with one more entry. But there was no assignment or exercise on that subject. I rewatched the video to [recreate the project](https://github.com/nathancashion/week12) and tried manipulating it in a few ways. With some effort, I learned how to include more than one entry/object in a single file and iterate over them with a for loop to print each line.

### Strategy
I've approached this from two directions. Based on the suggestion from Logan, I've tried to read the JSON file line-by-line as strings. I get stuck because the data is then unstructured. I'm not sure how to reliably strip the unnecessary information from the lists or how to filter through the data by outcome, group, percentage, etc.

I've also tried to import the file as a data object/lists. I try to slice the lists by using indexes, but I can't figure out how to find the right index. I was able to separate the *meta* from the *data* sections of the JSON file. As Logan indicated, the information we need (outcome, group, percentage, etc.) starts at index 8 through index 14(?). But this is of the internal or lowest level list. I've tried a number of ways to target the higher-level lists without any success. 

### Work-around
While I couldn't find a solution for the project in Python, I imported the data set into Tableau (which I've been learning for the Info Data Viz course). I was able to create charts and filter the data to find the following answers:
1. The percentage of adults in the 18-34-year age range who saw a doctor for a "Wellness Visit" in 2019 was 69.1% and in 2020 was 67.9%.
2. The group of adults that had the highest percentage of “Obesity” in 2020 was "Other Coverage" at 72.30%.Week Fifteen Discussion: Reflections
22 unread replies.22 replies.
You all are now officially Python programmers! Share your thoughts this week about what you learned. Here are some things you may wish to discuss:

Has learning how to write programs changed how you think?
What was the most challenging part of the class?
Do you plan to write any Python scripts in the future? What for?
How might your new skills help you in everyday life or in your career?
3. The following groups of adults had an increased percentage of “Difficulty communicating” from 2019 to 2020:
		- 45-64 years
		- 50-64 years
		- 200% and greater FPL
		- Asian, single race
		- Foreign-born
		- High school diploma or GED
		- Low social vulnerability
		- Medium social vulnerability
		- Male
		- Medicaid or other public
		- Mexican or Mexican American
		- Midwest
		- Never married
		- Nonmetropolitan
		- Not in MSA
		- Other, non-Hispanic
		- Part-time
		- Some college
		- Veteran
		- West
		- Widowed
		- With disability

### Understanding the data
Using Tableau highlighted another challenge. We haven't discussed how to look at a data set and assess whether it is complete or if certain fields need to be modified. As mentioned in the instructions, some percentages were outside of the expected range of 1-100. But why? Is this because they were calculated incorrectly, or do they represent something else about the data? For instance, the group with the highest percentage of obesity in 2020 was actually "Uninsured", but the result was 1,037%. Simply discarding it because it doesn't fit ignores a potential error in the data. Just because a result is outside of the expected range does not mean it should be discarded. Similarly, just because a result is within the expected range does not mean it is accurate. Perhaps all of the percentages should have been divided by 100?

### Summary
This project was indeed challenging. I recognized concepts we discussed previously – lists, functions, reading JSON file, etc. – but feel that we have not discussed the more complex aspects of these skills, nor have we sufficiently practiced them to be able to tackle a project of this size.