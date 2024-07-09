# Covid Symptoms PA6

## Problem
In order to better understand Covid symptoms from the original variant of COVID-19, we can analyze data published by Israel on citizens who were tests for covid.

## Details
You must create a program that can read in all data from the file, store it in a list, and then answer questions about that data.

### File Info
The file has values comma-delimited. A description of the fields is below.

### Program Abilities 
Your program must answer the following questions for the user:
* How likely was each demographic group to test positive: young males, young females, older males, older females, males with unknown age, and females with unknown age? Note that young/old is defined by whether or not they are under 60. Output in a well organized table format each group's positivity rate (e.g. percentage that tested positive).
* What percentage of negative patients had all 5 symptoms? What percentage of positive patients had all 5 symptoms?
* Create a graph that shows the number of positive test results over time.
* A question of your choosing!

You must give a menu with all options for the user. The program should only end when the user chooses the option to end from the menu.

### Fields in your file

The list of fields on each row are below. Note that the numbers here are NOT the same as the index into your list!

1. test_date: This column gives the date the person was tested for covid of the format YYYY-MM-DD
2. cough: 0 if the patient did not have a cough, 1 if they did
3. fever: 0 if the patient did not have a fever, 1 if they did
4. shortness_of_breath: 0 if the patient did not have shortness of breath, 1 if they did
5. corona_result: the result of their COVID test (negative/positive)
6. age_60_and_above: None if we don't know age, Yes if they are 60 or older, No if they younger than 60
7. sex: female, male, None 
8. test_indication: This field represents why they were tested. It can be "Other", "Abroad" (e.g. the patient traveled), or "Contact with confirmed".

