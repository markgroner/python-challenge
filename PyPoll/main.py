## A Python script that analyzes the votes and calculates each of the following:

## * The total number of votes cast

## * A complete list of candidates who received votes

## * The percentage of votes each candidate won

## * The total number of votes each candidate won

## * The winner of the election based on popular vote.


import os
import csv
import glob


## create a lists to store candidate values and total votes for each candidate
candidates_list = []
votes_list = []

## change directories to raw files
os.chdir('raw_data')

for csvpath in glob.glob('*.csv'):
    with open(csvpath, newline='') as csvfile:
        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # skip the headers
        #  Each row is read as a row
        for row in csvreader:
            voter_id = row[0]
            country = row[1]
            candidate = row[2]
            ## if candidate is in list, add one vote for that candidate
            if candidate in candidates_list:
                candidate_position = candidates_list.index(candidate)
                votes_list[candidate_position] += 1
            ## if candidate is not in list, add candidate to list and give them one vote
            else:
                candidates_list.append(candidate)
                votes_list.append(1)


## sum up total votes
total_votes = sum(votes_list)
## find winner
max_votes = max(votes_list)
winner_position = votes_list.index(max_votes)
winner = candidates_list[winner_position]
## print results
print('Election Results')
print('-------------------------')
print('Total Votes: %i' % (total_votes))
print('-------------------------')
for candidate in candidates_list:
    candidate_position = candidates_list.index(candidate)
    candidate_votes = votes_list[candidate_position]
    candidate_vote_perc = candidate_votes/total_votes * 100
    print('%s: %.1f%s (%i)' % (candidate, candidate_vote_perc, '%', candidate_votes))
print('-------------------------')
print('Winner: %s' % (winner))
print('-------------------------')
