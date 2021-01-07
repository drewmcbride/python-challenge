import os
import csv
import sys
election = os.path.join('Resources', 'election_data.csv')



total_votes = 0
khan_total = 0
correy_total = 0
li_total = 0
otooley_total = 0
candidate_count = {}
#candidate_count.keys()
#candidate[row[2]] = 0
winner = str()

#import file
with open(election, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)

#for loop and define variables
    for row in csv_reader:
        voter_id = int(row[0])
        county = str(row[1])
        candidate = str(row[2])
        total_votes += 1

#loop for candidate dictionary
        if candidate not in candidate_count.keys():
            candidate_count[candidate] = 1
        elif candidate in candidate_count.keys():
            candidate_count[candidate] += 1
#print for election results
    sys.stdout = open('analysis.txt','a')
    print("Election Results")
    print("--------------------")
    print(f"Total Votes: {total_votes}")
    print("--------------------")

#for loop to print dictionary results of winner
    for candidate in candidate_count.keys():
        winner = max(candidate_count, key=candidate_count.get)
        print(f"{candidate} {round(candidate_count[candidate]/total_votes * 100, 4)}% ({candidate_count[candidate]}) ")
    print("--------------------")
    print(f"Winner: {winner}")
  