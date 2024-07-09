# Working Adults PA5

## Problem
In order to better understand the working situation of adults in the US, you will analyze data from a large survey.

## Details
You must create a program that can read in all data from the file, store it in a list, and then answer questions about that data.

### File Info
The file has values comma-delimited. The file is 1.3MB in size, so it may take a little while to read in the data from the file into your program; that's normal.

The fields appear in your file in this order on each row:

* 'age': numerical value
* 'education_num': The highest level of education attained. See the education_num file in replit for what each number represents.
* 'marital_status': If the person is married or not. "Married-civ-spouse" means married to a civilian; "Married-AF-spouse" means married to someone in the armed forces. The rest of the values should be self explanatory.
* 'occupation'
* 'sex'
* 'hr_worked_per_week': Because this is a dataset of working people, everyone has worked at least 1 hour per week.
* 'income_greater_50K': Values are "Yes" or "No" based on whether income crosses the 50K range.

### Program Abilities
Your program must answer the following questions for the user:
* How many people work more hours, significantly more hours, fewer hours, or significantly fewer hours than the average number of hours worked for the people in the dataset? You should consider a change of at least +/- 5 to be more/less, and a change of at least +/- 20 to be significantly more/less.
* Create a graph to show how many people with each education level make at least `$50K` per year.
* What is the average number of hours worked per week for each occupation?
* A question of your choosing!

You must give a menu with all options for the user. The program should only end when the user chooses the option to end from the menu.


