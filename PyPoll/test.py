import csv
import os

data = os.path.join("Resources","election_data.csv")
results = os.path.join("Analysis", "election_results.txt")

# create counter for the total votes
total_votes = 0

# create list and dictionary to store the Candidates and votes for them
cand_opt = []
cand_votes = {}

#create var for winning candidate and votes for them
win_cand = ""
win_votes = 0

#read the csv
with open(data) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)

    for row in reader:      
        total_votes += 1
        cand_name = row[2]

        if cand_name is not cand_opt:
            cand_opt.append(cand_name)
            cand_votes[cand_name] = 0 
        cand_votes[cand_name] += 1

with open(results, "w") as text_file:

   for cand in cand_votes:

    votes = cand_votes.get(cand)
    vote_pct = float(votes) / float(total_votes) * 100


    if (votes > win_votes):
        win_votes = votes
        win_cand = cand

print(win_cand)