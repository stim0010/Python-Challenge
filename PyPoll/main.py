import csv

poll_csv = "Resources/election_data.csv"


with open(poll_csv) as csvfile:
    
    csvreader=csv.reader(csvfile, delimiter=',')

    header=next(csvreader)
    
    total_votes = 0
    
    for row in csvreader:
        
        ##Calc total number of votes by counting the rows
        total_votes = total_votes + 1
        
        ##Use 'while' to determine the candidates and store them in a list
        ##if currentrow != previous row:
            ##store
        
    
    print('Election Results')
    print('---------------------')
    print(f'Total Votes: {total_votes}')
    print('---------------------')
    ##For loop to display the candidate stored in list
    #print(f'{candidate[]}: {vote_pct} ({can_votes})')
    print(f'---------------------')
    #find max(can_votes)
    #print(f'Winner: {winner}')
    print(f'---------------------')
    #print(f'{})
    