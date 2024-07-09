# Programmers:  John & Bryan
# Course:  CS151, Dr. Kenyon 
# Due Date: 4/29/2024
# Lab Assignment:  PA5
# Problem Statement: Children's Health Outcomes in Baltimore
# Data In: Health.csv file and user's decision
# Data Out: Graph of fast food in Baltimore, Category of IMR with highest number of neighborhoods in it, change in teen birth rate
# Credits: PA5 description 

#imports 
import os 
import matplotlib.pyplot as plt

#Function name: filename_checker()
#Purpose: check existence of file from user input
#Parameters: none
#Return: returns filename
#define filename_checker()
def filename_checker():
  #ask user for file name
  filename = input("Enter the name of the file: ")
  while not os.path.exists(filename):
    filename = input("Invalid file, enter name of file: ")
  return filename 


#Function name: read_in_file()
#Purpose: read file entered by user and put in list
#Parameters: filename
#Return: returns a list of the file
#define read_in_file()
def read_in_file(filename):
  file_list = []
  try:
    file = open(filename, 'r')
    for line in file: 
      line = line.strip()
      words = line.split(',')
      file_list.append(words)
    file.close()
    return file_list
  except FileNotFoundError:
    print("File not found")
    return []

#Function name: get_output_filename()
#Purpose: get output file name
#Parameters: none
#Return: returns output file name
#define get_output_filename()
def get_output_filename():
  output_filename = input("Enter the name of the output file: ")
  return output_filename

#Function name: calculate_and_output_tbr_change(file_list, output_filename)
#Purpose: calculate change in teen birth rate
#Parameters: file_list, output_filename
#Return: nothing
#define calculate_and_output_tbr_change(file_list, output_filename)
def calculate_and_output_tbr_change(file_list, output_filename):
  with open(output_filename, 'w') as output_file:
    output_file.write("Neighborhood,2010 TBR,2014 TBR,Change,Classification\n")
    significant_change_threshold = 25
    no_change_threshold = 5

    for row in file_list[0:]:
      neighborhood_name = row[0]
      tbr_2010 = float(row[1])
      tbr_2014 = float(row[6])
      change = tbr_2014 - tbr_2010
      classification = classify_change(change, significant_change_threshold, no_change_threshold)
      output_file.write(f"{neighborhood_name},{tbr_2010:.2f},{tbr_2014:.2f},{change:.2f},{classification}\n")



#Function name: classify_change(change, significant_change_threshold, no_change_threshold)
#Purpose: classify change in teen birth rate
#Parameters: change, significant_change_threshold, no_change_threshold
#Return: returns classification
#define classify_change(change, significant_change_threshold, no_change_threshold)
def classify_change(change, significant_change_threshold, no_change_threshold):
  if change < -significant_change_threshold:
    return "significantly down"
  elif change < -no_change_threshold:
    return "down"
  elif change <= no_change_threshold:
    return "flat"
  elif change < significant_change_threshold:
    return "up"
  else:
    return "significantly up"

#Function name: create_density_graph(file_list)
#Purpose: create graph of fast food density distribution
#Parameters: file_list
#Return: nothing
#define create_density_graph(file_list)
def create_density_graph(file_list):
    #initialize variables 
    low_count = 0
    moderate_count = 0
    high_count = 0
    #for loop to iterate through each row of list and check density
    for row in file_list[0:]:
        density = float(row[68])  # 2013 density is at index 68
        if density < 1:
            low_count += 1
        elif density >= 1 and density <= 4:
            moderate_count += 1
        elif density > 4:
            high_count += 1
    # Create bar plot
    plt.bar(["Low", "Moderate", "High"], [low_count, moderate_count, high_count])
    # Style and customize
    plt.xlabel("Density Category")
    plt.ylabel("Number of Neighborhoods")
    plt.title("Distribution of Fast Food Outlet Density in 2013")
    plt.xticks(rotation=30, ha="right")
    plt.grid(True)
    # Save figure
    plt.savefig("density_distribution.png")
    plt.show()




  #Function name: categorize_neighborhoods(file_list)
  #Purpose: categorize neighborhoods based on IMR
  #Parameters: file_list
  #Return: nothing
  #define categorize_neighborhoods(file_list)
def categorize_neighborhoods(file_list):
  #create dictionary for each pair 
  categories = {
    'Low IMR, High Prenatal Care': 0,
    'Low IMR, Moderate Prenatal Care': 0,
    'Low IMR, Low Prenatal Care': 0,
    'High IMR, High Prenatal Care': 0,
    'High IMR, Moderate Prenatal Care': 0,
    'High IMR, Low Prenatal Care': 0,
    'Moderate IMR, High Prenatal Care': 0,
    'Moderate IMR, Moderate Prenatal Care': 0,
    'Moderate IMR, Low Prenatal Care': 0
}
  #for loop to iterate through each row of list and check IMR
  for row in file_list[0:]: 
      
      imr = (row[73])
      #many if statements to check IMR/Prenatal and count each 
      if imr == 'High-Prenatal:Low-IMR':
          categories['Low IMR, High Prenatal Care'] += 1
      elif imr == 'Moderate-Prenatal:Low-IMR':
          categories['Low IMR, Moderate Prenatal Care'] += 1
      elif imr == 'Low-Prenatal:Low-IMR':
          categories['Low IMR, Low Prenatal Care'] += 1
      elif imr == 'High-Prenatal:High-IMR':
          categories['High IMR, High Prenatal Care'] += 1
      elif imr == 'Moderate-Prenatal:High-IMR':
          categories['High IMR, Moderate Prenatal Care'] += 1
      elif imr == 'Low-Prenatal:High-IMR':
          categories['High IMR, Low Prenatal Care'] += 1
      elif imr == 'High-Prenatal:Moderate-IMR':
          categories['Moderate IMR, High Prenatal Care'] += 1
      elif imr == 'Moderate-Prenatal:Moderate-IMR':
          categories['Moderate IMR, Moderate Prenatal Care'] += 1
      elif imr == 'Low-Prenatal:Moderate-IMR':
          categories['Moderate IMR, Low Prenatal Care'] += 1
      
  #this finds the max value in dictionary 
  max_category = max(categories, key=categories.get)
  #output value
  print(f"The category with the most neighborhoods is: {max_category}")

  #Function name: identify_top_neighborhoods(file_list)
  #Purpose: identify top 10 neighborhoods with highest blood lead levels
  #Parameters: file_list
  #Return: nothing
  #define cidentify_top_neighborhoods(file_list)
def identify_top_neighborhoods(file_list):
  neighborhoods_data = {}  # Dictionary to store neighborhood data
  #for loop to iterate through each neighborhood and check blood lead level 
  for row in file_list[0:]:  
      neighborhood = row[0]
      lead_level_percentage = float(row[30])  
      neighborhoods_data[neighborhood] = lead_level_percentage

  # Sort neighborhoods by lead level percentages in descending order
  sorted_neighborhoods = sorted(neighborhoods_data.items(), key=lambda x: x[1])

  # Get the top 10 neighborhoods in reverse order to have highest percentages first
  top_10_neighborhoods = sorted_neighborhoods[-10:][::-1]
  print("Top 10 Neighborhoods with Highest Lead Level Percentages (2014):\n")
  for neighborhood, percentage in top_10_neighborhoods:
      print(f"{neighborhood}: {percentage}%\n")
      #simple for loop to print each of the 10 neighborhoods





#Function name: input_int(msg)
#Purpose: ensure menu input is a number
# Parameters: msg 
# Returns: int typed in by the user
#define input_int(msg)
def input_int(msg):

  # Ask user for an integer using parameter as prompt
  candidate = input(msg)

  # while the user hasn't provided an integer, ask again
  while not candidate.isdigit():
    print("Sorry, please enter an integer")
    candidate = input(msg)

  # Return user's input, typecast to an int
  return int(candidate)

  #Function name: menu()
  #Purpose: create menu for program 
  #Parameters: none
  #Return: menu choice
  #define menu()
def menu():
  print()
  # Create list of menu options to output to user
  menuoptions = "\t1. Change in Teen Birth Rate\n" +\
                "\t2. Fast Food by Neighborhood\n" +\
                "\t3. Infant Mortality & Prenatal\n" +\
                "\t4. Elevated Blood Lead Levels in Children\n" +\
                "\t0. Exit"

  # Output options with nice formatting
  print("-" * 40)
  print("Please select what you would like to do:")
  print(menuoptions)
  print("-" * 40)
  # Ask user for choice using int input function, until they provide a valid value
  choice = input_int("Your selection: ")
  while choice > 4:
    print("That is not an option. As a reminder, your options are: ")
    print(menuoptions)
    choice = input_int("Your selection: ")

  return choice  # Return user's choice as an int 





#Function name: main()
#Purpose: call functions and run program
#Parameters: none
#Return: nothing
#define main()
def main():
  print(
    "Welcome! This program will allow you to learn more about Children's Health Outcomes in Baltimore.\n")
  filename = filename_checker()
  file_list = read_in_file(filename)
  # Get user's choices
  choice = menu()

  # while the user hasn't chosen to quit, do their choice and ask again for a choice
  while choice != 0:

    if choice == 1: 
      output_filename = get_output_filename()
      calculate_and_output_tbr_change(file_list, output_filename)
      #call function
    elif choice == 2:  
      create_density_graph(file_list) #call function
    
    elif choice == 3:  
      categorize_neighborhoods(file_list) #call function
    
    elif choice == 4:  
      identify_top_neighborhoods(file_list) #call function 
    
    choice = menu()  # Ask user to choose again

  print("Thank you for using this program!") #thank user 


#call main 
main()