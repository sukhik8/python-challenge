import os
import csv

# Set file path
fname = os.path.join('/Users/sukhikaur/Desktop/UCI Class Analysis/PyPoll/election_data.csv', 'Resources', 'election_data.csv')
output = os.path.join('Analysis', 'election_analysis.txt')

# Set important variables
total_votes = 0

# Set Candidate variables
candidate_options = []
candidate_votes = {}

# Set Winning Candidate variables
winning_candidate = ""
winning_count = 0
lastCount = 0
Winner = ""

# Convert the list into dictionaries
with open('election_data.csv', 'r') as election_data:
    reader = csv.reader(election_data)
    # Read the header row
    header = next(reader)
    for row in reader:
        print(".", end="")
        candidate_name = row[2]
        total_votes = total_votes +1

# Assign candidates to indexes
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
    

            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1



# Generate results and export to text file
with open('election_analysis', "w") as txt_file:
    
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    txt_file.write(election_results)

# Set candidate on vote_list for loop
for candidate in candidate_options:

    lastCount = candidate_votes.get(candidate)
    winning_candidate = float(lastCount) / float(total_votes)

    voter_output = f"{candidate}: {winning_candidate:.3%} ({lastCount})\n"
    print(voter_output, end="")


    if (lastCount > winning_count):
        Winner = candidate 
        winning_count = lastCount



# Generate the winner
winning_candidate_summary = (
    f"------------------------------\n"
    f"Winner: {Winner}\n"
    f"------------------------------\n")
print(winning_candidate_summary)
