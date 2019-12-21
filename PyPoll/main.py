import os
import csv

csvpath = os.path.join("election_data.csv")
#votes need to be a number so we can operate on it to get a percentage later
#we can store candidate names in a list
total_votes = 0
unique_candidates = []
votes_for_candidates = []

with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    header = next(csvreader)
    #count the number of votes (rows)
    for row in csvreader:
        total_votes += 1
        #identify the column that has all the candidates
        candidate_column = row[2]
        #we want to store the candidate names in a list but only once. If the name isn't in the list, add it. If it's already in the list, skip it.
        if candidate_column not in unique_candidates:
            unique_candidates.append(candidate_column)
            votes_for_candidates.append(1)
        #after we make the list of candidates, we want to point to a specific candidate and add one to votes list every time the name is mentioned/repeated
        else:
            candidate_spot = unique_candidates.index(candidate_column)
            votes_for_candidates[candidate_spot] = votes_for_candidates[candidate_spot] + 1
#calculate the percentage of votes each candidate has and pick which one has the most. Can use max command here.
percentage_list = []
votes_max = votes_for_candidates[0]
spot_max = 0
#loop through our list of candidates and turn their vote count into a percentage
for i in range(len(unique_candidates)):
    percentage_votes = round(votes_for_candidates[i] / total_votes * 100, 2)
    percentage_list.append(percentage_votes)

    if votes_for_candidates[i] > votes_max:
        votes_max = votes_for_candidates[i]
        spot_max = i

#we need to pick the winner from the list we have created (the candidate that has the highest number value associated with it)
poll_winner = unique_candidates[spot_max]

#print("Election Results")
#print("-----------------")
#print("Total Votes: " + str(total_votes))
#print("-----------------")
#print(f'{unique_candidates[i]} : {percentage_list[i]}% ({votes_for_candidates[i]})')
#print("-----------------")
#print(f'Election Winner: {poll_winner}')
#print("-----------------")
#This works but will only print the last candidate in the list, therefore needs a for loop to execute print for each candidate stored in the list

print("Election Results")
print("-----------------")
print("Total Votes: " + str(total_votes))
print("-----------------")
for i in range(len(unique_candidates)):
    print(f'{unique_candidates[i]} : {percentage_list[i]}% ({votes_for_candidates[i]})')
print("-----------------")
print(f'Election Winner: {poll_winner}')
print("-----------------")

#write the output to a csv file
output_path = os.path.join("PyPoll_output.csv")

with open(output_path, 'w', newline='') as new_csvfile:

    csvwriter = csv.writer(new_csvfile, delimiter=',')

    csvwriter.writerow(["Election Results"])

    csvwriter.writerow(["Total Votes: ", str(total_votes)])
    for i in range(len(unique_candidates)):
        csvwriter.writerow([f'{unique_candidates[i]} :', f'{percentage_list[i]}% ({votes_for_candidates[i]})'])

    csvwriter.writerow(["Election Winner: ", str(poll_winner)])