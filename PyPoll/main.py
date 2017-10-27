## A Python script that analyzes the votes and calculates each of the following:

## * The total number of votes cast

## * A complete list of candidates who received votes

## * The percentage of votes each candidate won

## * The total number of votes each candidate won

## * The winner of the election based on popular vote.


import os
import csv
import glob


##
candidates_list = []
votes_list = []
candidate_dict= {'candidates': candidates_list, 'votes': votes_list}

## change directories to
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
            if candidate in candidates_list:
                candidate_position = candidates_list.index(candidate)
                votes_list[candidate_position] += 1
            else:
                candidates_list.append(candidate)
                votes_list.append(1)

##       print(candidates_list)
##       print(votes_list)
##       print(sum(votes_list))

for candidate in candidates_list:
