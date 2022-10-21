# The data we need to retrieve

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. the winner of the election based on popular vote


import csv
import os
# Assign  a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a file name variable to a direct or indirect path to the file
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# 1. Initiazlize a total vote counter
total_votes = 0
# Initialize candidate options
candidate_options = []

# Declare empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    # To do: Read and analyze Data:
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)
    
    # Print each row in the csv file
    for row in file_reader:
        #2 . Add to the total vote count
        total_votes += 1

        # Print candidate name from each row
        candidate_name = row[2]

        # add candidate name to the candidate list
           # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # begin tracking that candidates vote count
            candidate_votes[candidate_name] = 0
    
        # add a vote to candidates names
        candidate_votes[candidate_name] += 1 

        # Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name

         
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)


        



    
    
