import os
import csv

csvpath = os.path.join("election_data.csv")
#votes are a number and we can store candidate names in a list
total_votes = 0
unique_candidates = []
votes_for_candidates = []

with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    header = next(csvreader)

    for row in csvreader:
        total_votes += 1

        candidate_column = row[2]

        if candidate_column not in unique_candidates:
            unique_candidates.append(candidate_column)
            votes_for_candidates.append(1)
        else:
            candidate_spot = unique_candidates.index(candidate_column)
            votes_for_candidates[candidate_spot] = votes_for_candidates[candidate_spot] + 1

percentage_list = []
votes_max = votes_for_candidates[0]
spot_max = 0

for i in range(len(unique_candidates)):
    percentage_votes = round(votes_for_candidates[i] / total_votes * 100, 2)
    percentage_list.append(percentage_votes)

    if votes_for_candidates[i] > votes_max:
        votes_max = votes_for_candidates[i]
        spot_max = i

poll_winner = unique_candidates[spot_max]

print("Election Results")
print("-----------------")
print("Total Votes: " + str(total_votes))
print("-----------------")
print(f'{unique_candidates[i]} : {percentage_list[i]}% ({votes_for_candidates[i]})')
print("-----------------")
print(f'Election Winner: {poll_winner.upper()}')
print("-----------------")
