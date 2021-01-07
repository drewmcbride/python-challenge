import os
import csv
election = os.path.join('Resources', 'election_data.csv')

# Need help building the function
# def vote_count(row):
# khan_total = 0
# #     voter_id = int(row[0])
# #     county = str(row[1])
# #     candidate = str(row[2])
# if candidate == "Khan":
#             khan_total += 1
# khan_total += 1
#     return voter_id,country,candidate

#We can let the function return the candidiate name

total_votes = 0
khan_total = 0
correy_total = 0
li_total = 0
otooley_total = 0
candidate_count = {}
#candidate_count.keys()
#candidate[row[2]] = 0
winner = str()
with open(election, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)
    for row in csv_reader:
        voter_id = int(row[0])
        county = str(row[1])
        candidate = str(row[2])
        total_votes += 1
        # <Check with if condition whether the row[2] is NOT present inside the KEYS of dictionary">
        #     Append that key to the dictionary and we initalise the value of that key to zero
        # <if name is present>>
        #     Just add 1 to the value of the key

        if candidate not in candidate_count.keys():
            candidate_count[candidate] = 1
        elif candidate in candidate_count.keys():
            candidate_count[candidate] += 1
    print("Election Results")
    print("--------------------")
    print(f"Total Votes: {total_votes}")
    print("--------------------")
    
    for candidate in candidate_count.keys():
        winner = max(candidate_count, key=candidate_count.get)
        print(f"{candidate} {round(candidate_count[candidate]/total_votes * 100, 4)}% ({candidate_count[candidate]}) ")
    print("--------------------")
    print(f"Winner: {winner}")
        # if candidate == "Khan":
        #     khan_total += 1
        # elif candidate == "Correy":
        #     correy_total += 1
        # elif candidate == "Li":
        #     li_total += 1
        # elif candidate == "O'Tooley":
        #     otooley_total += 1
    #     khan_percent = round((khan_total / total_votes) * 100, 3)
    #     correy_percent = round((correy_total / total_votes) * 100, 3)
    #     li_percent = round((li_total / total_votes) * 100, 3)
    #     otooley_percent = round((otooley_total / total_votes) * 100, 3)
    
    # print("Election Results")
    # print("--------------------")
    # print(f"Total Votes: {total_votes}")
    # print("--------------------")
    # print(f"Khan: {khan_percent}% ({khan_total})")
    # print(f"Correy: {correy_percent}% ({correy_total})")
    # print(f"Li: {li_percent}% ({li_total})")
    # print(f"O'Tooley: {otooley_percent}% ({otooley_total})")
    # print("--------------------")
    # print(f"Winner : ")
    # print("--------------------")