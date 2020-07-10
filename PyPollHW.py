import os
import csv

election_data = os.path.join("election_data.csv")

# Candidates List
candidates = []

# Number of Votes
num_votes = []

# Percentage of Votes
percent_votes = []

# total number of votes 
total_votes = 0

with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader: 
        total_votes += 1 

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1
    
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percent_votes.append(percentage)
    
    # Find the Winner
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

# Print the results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")

Election Results
--------------------------
Total Votes: 3521001
--------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
--------------------------
Winner: Khan
