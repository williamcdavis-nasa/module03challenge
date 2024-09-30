# Challenge 3: PyBank

# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
# The dataset is composed of two columns: Date and Profit/Losses. 

# Your task is to create a Python script that analyzes the records to calculate each of the following:
#   1.	The total number of months included in the dataset
#   2.	The total net amount of "Profit/Losses" over the entire period
#   3.	The average change in "Profit/Losses" between months over the entire period
#   4.	The greatest increase in profits (date and amount) over the entire period
#   5.	The greatest decrease in losses (date and amount) over the entire period
# Your analysis should look similar to the one below:

#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $22564198
#   Average Change: $-8311.11
#   Greatest Increase in Profits: Aug-16 ($1862002)
#   Greatest Decrease in Profits: Feb-14 ($-1825558)
 
# Your final script should both print the analysis to the terminal and export a text file with the results.

# Import dependencies modules os and csv

import os
import csv

# Create variables
 
count = 0
current_pl = 0
previous_pl = 0
monthly_pl_change = 0
total_pl = 0
total_pl_change = 0

# Create lists

month = []
monthly_pl = []
monthly_changes = []

# Read CSV file and option to print path for verification (print command is disabled)
PyBank = os.path.join('Resources', 'budget_data.csv')
# source_file = os.path.abspath(PyBank)
# print(f"Source File: {source_file}")

with open(PyBank, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    csv_header = next(csvreader)

    # Interate through the rows of the CSV file
    for row in csvreader:    

        # Add to indexed list of months
        month.append(row[0])

        # Count the number months in the CSV file
        count = count + 1 

        # Add to indexed list of monthly pl values
        monthly_pl.append(row[1])
    
        # Calculate the running pl total
        current_pl = int(row[1])
        total_pl = total_pl + current_pl

        # Calculate change in pl since previous month, skipping first month in sequence
        if count == 1:
            previous_pl = current_pl
        else:
            monthly_pl_change = current_pl - previous_pl
        
        # Add to indexed list of monthly pl changes
        monthly_changes.append(monthly_pl_change)

        # Calculate the running monthly pl changes total 
        total_pl_change = total_pl_change + monthly_pl_change

        # Reset the previous_pl for the next iteration in this loop
        previous_pl = current_pl

    # Calculate the average change in profits skipping first month since no change is available for that month to be calculated
    average_change_profits = (total_pl_change/(count-1))
      
    #Find the max and min change in profits and the months when they occurred by using indexes
    greatest_increase = max(monthly_changes)
    greatest_decrease = min(monthly_changes)

    greatest_increase_month = month[monthly_changes.index(greatest_increase)]
    greatest_decrease_month = month[monthly_changes.index(greatest_decrease)]

# Display the financial analysis information in terminal
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(count))
print("Total Profits: " + "$" + str(total_pl))
print("Average Change: " + "$" + str(round(average_change_profits,2)))
print("Greatest Increase in Profits: " + str(greatest_increase_month) + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + str(greatest_decrease_month) + " ($" + str(greatest_decrease)+ ")")

# Write financial analysis to text file
with open('financial_analysis.txt', 'w') as text:
    text.write("Financial Analysis"+ "\n")
    text.write("----------------------------\n")
    text.write("Total Months: " + str(count) + "\n")
    text.write("Total Profits: " + "$" + str(total_pl) +"\n")
    text.write("Average Change: " + '$' + str(round(average_change_profits,2)) + "\n")
    text.write("Greatest Increase in Profits: " + str(greatest_increase_month) + " ($" + str(greatest_increase) + ")\n")
    text.write("Greatest Decrease in Profits: " + str(greatest_decrease_month) + " ($" + str(greatest_decrease) + ")\n")