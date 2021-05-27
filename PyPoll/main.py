import csv

poll_csv = "../Resources/election_data.csv"

def vote_anal(poll_data):

    voter_ID=int(poll_data[0])
    country=str(poll_data[1])
    candidate=str(poll_data[2])



    ##Total votes cast (count row)

    ##Complete list of candidates who recieved votes 

    ##The percentage of votes each candidate won (candidate votes/total votes)

    ##The total number of votes each canidate won (count candidate votes)

    ##The winner of the election based on popular vote 



with open(poll_data) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

