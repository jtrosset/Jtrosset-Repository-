# Pokemon PA6

## Problem
In this assignment you will create a program that organizes Pokemon for the user.

## Details
You must create a program that can read in all data from the file, store it in a list, and then answer questions about that data.

### File Info
The file has values comma-delimited. A description of the fields is below.

### Program Abilities
Your program must answer the following questions for the user:
* Allow the user to choose a type of Pokemon (includes Type 1 and Type 2) and output to a file all pokemon that meet that criteria. For instance, if the user chooses grass and poison, it should output all Pokemon that have both types; if the user only wants all grass pokemon, it should including all pokemon that have the grass type even if they also have another type as well.
* What percentage of Pokemon have a low, medium, or high HP? Create a graph to show the percentages. Low HP is considered below 50, medium is between 50 and 125, and high is over 125.
* Which pokemon(s) have the highest increase in attack from their basic attack to their special attack level?
* A question of your choosing!

You must give a menu with all options for the user. The program should only end when the user chooses the option to end from the menu.

### Fields in your file

The list of fields on each row are below. Note that the numbers here are NOT the same as the index into your list!

1. Pokemon ID, which is unique for each Pokemon
2. Name of the Pokemon
3. Height of the pokemon
4. Weight of the pokemon
5. Type 1: the main type of the pokemon. Every pokemon has at least one type.
6. Type 2: The secondary type of the pokemon. Not all pokemon have a second type.
7. HP (hit points) the Pokemon has; this is essentially their health in battle
8. Attack level
9. Defense level
10. Special Attack level
11. Special Defense level