# Challenge 3: PyPoll

# In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process. 
# The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 

# Your task is to create a Python script that analyzes the votes and calculates each of the following values:
#   1. The total number of votes cast
#   2. A complete list of candidates who received votes
#   3. The percentage of votes each candidate won
#   4. The total number of votes each candidate won
#   5. The winner of the election based on popular vote

# Your analysis should align with the following results:

# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------
 
# Your final script should both print the analysis to the terminal and export a text file with the results.

# Import dependencies modules os and csv
import os
import csv

# Create variables
votes = 0
votes_candidate1 = 0
votes_candidate2 = 0
votes_candidate3 = 0
candidate1 = "Charles Casper Stockham"
candidate2 = "Diana DeGette"
candidate3 = "Raymon Anthony Doane"

# Read CSV file and option to print path for verification (print command is disabled)
PyPoll = os.path.join('Resources', 'election_data.csv')
# source_file = os.path.abspath(PyPoll)
# print(f"Source File: {source_file}")

with open(PyPoll, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    csv_header = next(csvreader)

    # Interate through the rows of the CSV file
    for row in csvreader:    

        # Tabulate the running total number of votes
        votes = votes + 1 

        # Use conditional statements to tabluate running vote count for each candidate
        # Candidate 1 = Charles Casper Stockham
        # Candidate 2 = Diana DeGette
        # Candidate 3 = Raymon Anthony Doane
        if row[2] == candidate1:
            votes_candidate1 = votes_candidate1 + 1
        elif row[2] == candidate2:
            votes_candidate2 = votes_candidate2 + 1
        else:
            votes_candidate3 = votes_candidate3 + 1
        
# Calculate the percent of votes recieved by each candidate
percent_candidate1 = votes_candidate1 / votes * 100
percent_candidate2 = votes_candidate2 / votes * 100
percent_candidate3 = votes_candidate3 / votes * 100
    
# Find the highest vote count and the candidate it corresponds to
candidates = [candidate1, candidate2, candidate3]
results = [votes_candidate1, votes_candidate2, votes_candidate3]
winner = candidates[results.index(max(results))]

# Display the election results summary in terminal
print("Election Results")
print("----------------------------")
print("Total Votes: " + str(votes))
print("----------------------------")
print(candidate1 + ": " + str(round(percent_candidate1, 3)) + "% (" + str(votes_candidate1) + ")")
print(candidate2 + ": " + str(round(percent_candidate2, 3)) + "% (" + str(votes_candidate2) + ")")
print(candidate3 + ": " + str(round(percent_candidate3, 3)) + "% (" + str(votes_candidate3) + ")")
print("----------------------------")
print("Winner: " + str(winner))
print("----------------------------")

# Write election results analysis to text file
with open('elections_results.txt', 'w') as text:
    text.write("Election Results"+ "\n")
    text.write("----------------------------\n")
    text.write("Total Votes: " + str(votes) + "\n")
    text.write("----------------------------\n")
    text.write(str(candidate1) + ": " + str(round(percent_candidate1, 3)) + "% (" + str(votes_candidate1) + ")\n")
    text.write(str(candidate2) + ": " + str(round(percent_candidate2, 3)) + "% (" + str(votes_candidate2) + ")\n")
    text.write(str(candidate3) + ": " + str(round(percent_candidate3, 3)) + "% (" + str(votes_candidate3) + ")\n")
    text.write("----------------------------\n")
    text.write("Winner: " + str(winner) + "\n")
    text.write("----------------------------\n")