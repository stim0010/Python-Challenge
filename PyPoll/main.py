import csv

poll_csv = "Resources/election_data.csv"

##CREATE FUNCTION 

#def vote_analysis(poll_data):

    #voter_ID=int(poll_data[0])
    #county=str(poll_data[1])
    #candidate=str(poll_data[2])

    ##Total votes cast (count row)
    #total_votes=len(list(poll_data[0]))

    ##Complete list of candidates who recieved votes (list name and remove duplicates)
    
    ##The percentage of votes each candidate won (candidate votes/total votes)
    ## p_won=(# of candidate)/total_votes
    
    ##The total number of votes each canidate won (count candidate votes)

    ##The winner of the election based on popular vote 
    
    ###########################################################################
    
    #print('Election Results')
    #print('---------------------')
    #print(f'Total Votes: {total_votes}')
    #print('---------------------')
    #print(f'{candidate_list}')
    #print(f'{})

####FORMAT
####Election Results
####----------------
####Total Votes: {total_votes}
####----------------
####candidate(x): {p_won} + '(' + {can_votes} + ')'
####----------------
####Winner: max({can_votes})


###############################################################################


with open(poll_csv) as csvfile:
    
    csvreader=csv.reader(csvfile, delimiter=',')

    header=next(csvreader)
    
    print(len(list(csvreader)))
    