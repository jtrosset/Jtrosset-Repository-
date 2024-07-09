# 911 Calls PA6

## Problem
In this assignment  you will be analyzing the 911 calls made in Baltimore in 2015 and 2017.

## Details
You must create a program that can read in all data from the file, store it in a list, and then answer questions about that data.

### File Info
The file has values semi-colon-delimited. A description of the fields is below.

### Program Abilities
Your program must answer the following questions for the user:
* How did the percentage of calls that were low, medium, or high priority change from 2015 to 2017? Show the percentage for each year and note if it was higher or lower in 2017 when compared to 2015.
* How many 911 calls were made each month in 2015? Create a graph to show this data.
* After the user chooses a type of 911 call (e.g. description), and a time of day, output to a file all calls that are of that type during that time of day. The options for time of day are "morning (6:00-12:00)", "afternoon (12:01-18:00)", "evening (18:01-23:00)", or "night (all other times)".
* A question of your choosing!

You must give a menu with all options for the user. The program should only end when the user chooses the option to end from the menu.

### Fields in your file

The list of fields on each row are below. Note that the numbers here are NOT the same as the index into your list!

1. The date of the call in the format `month/day/year`, for example `8/2/17`. 
2. The time of the call in military time (otherwise known as 24 hour time).
3. Priority for the call (Low as "L", Medium as "M", High as "H")
4. District in which the call was made
5. Description of the type of call (for example, "Auto Accident", "Larceny", "dog bite", etc)
6. Location of the Incident (this is usually in the form of an address)
