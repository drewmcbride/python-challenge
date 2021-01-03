import os
import csv
election = os.path.join('Resources', 'election_data.csv')
total_votes = 0
khan_total = 0
correy_total = 0
li_total = 0
otooley_total = 0
with open(election, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)
    for row in csv_reader:
        voter_id = int(row[0])
        county = str(row[1])
        candidate = str(row[2])
        total_votes += 1
        if candidate == "Khan":
            khan_total += 1
        elif candidate == "Correy":
            correy_total += 1
        elif candidate == "Li":
            li_total += 1
        elif candidate == "O'Tooley":
            otooley_total += 1
        khan_percent = round((khan_total / total_votes) * 100, 3)
        correy_percent = round((correy_total / total_votes) * 100, 3)
        li_percent = round((li_total / total_votes) * 100, 3)
        otooley_percent = round((otooley_total / total_votes) * 100, 3)
    
    print("Election Results")
    print("--------------------")
    print(f"Total Votes: {total_votes}")
    print("--------------------")
    print(f"Khan: {khan_percent}% ({khan_total})")
    print(f"Correy: {correy_percent}% ({correy_total})")
    print(f"Li: {li_percent}% ({li_total})")
    print(f"O'Tooley: {otooley_percent}% ({otooley_total})")
    print("--------------------")
    print(f"Winner : {winner}")
    print("--------------------")