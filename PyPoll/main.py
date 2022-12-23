# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 11:19:14 2022

@author: LTabl
"""
import os
import csv

#import csv
election_data_csv = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

# read in the csv file
with open(election_data_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ',')

    #read the header row first
    csv_header = next(csvreader)

    #create variable to count total number of votes
    total_votes = 0
   
    #create a dictionary that will store candidate:votes. this will be used to retrieve count of votes per candidate
    candidate_votes = {}

    #loop through csv data
    for row in csvreader:

        #get total number of votes
        total_votes += 1
        
        #create a counter to tally total number of votes per candidate
        if row[2] not in candidate_votes:
            candidate_votes[row[2]] = 1

        else:
            candidate_votes[row[2]] += 1

#check results for total number of votes
print(total_votes)

#using the dictionary, retrieve total votes per candidate
for candidate, votes in candidate_votes.items():
    #calculate percentage of votes for each candidate
    percent_votes = votes/total_votes * 100
    #format percent to 3 decimal points
    formatted_percent = '{:.3f}'.format(percent_votes)
    #check results
    print(candidate, formatted_percent, votes)

#find winner using max of candidate votes, using get dictionary method and key
winner = max(candidate_votes, key = candidate_votes.get)
#check results
print(winner)

print("Election Analysis")
print("--------------------------")
# print total months
print(f'Total Votes: {total_votes}')
print("--------------------------")
# print each candidate name, percent of votes, and overall count of votes
for candidate, votes in candidate_votes.items():
     print(f'{candidate} : {formatted_percent}% ({str(votes)})')
print("--------------------------")     
#print winner
print(f'Winner: {winner}')


#export results to txt file
#specify the file to write to
election_results = os.path.join("Analysis", "election_results.txt")
with open(election_results, 'w') as txtfile:
    txtfile.write("Election Analysis\n")
    txtfile.write("--------------------------\n")
    txtfile.write(f'Total Votes: {total_votes}\n')
    txtfile.write("--------------------------\n")
    for candidate, votes in candidate_votes.items():
        txtfile.write(f'{candidate} : {formatted_percent}% ({str(votes)})\n')
    txtfile.write("--------------------------\n")
    txtfile.write(f'Winner: {winner}\n')


