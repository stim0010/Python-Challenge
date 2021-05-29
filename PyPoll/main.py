import csv

poll_csv = "Resources/election_data.csv"


with open(poll_csv) as csvfile:
    
    csvreader=csv.reader(csvfile, delimiter=',')

    header=next(csvreader)
    
    total_votes = 0
    
    # dictionaries
    cans_summary = {}
    
    #lists
    cans = []
    can_votes = []
    pct_votes = []
        
    
    for row in csvreader:
        
        ##Calc total number of votes by counting the rows
        total_votes = total_votes + 1
        
        ##Use 'while' to determine the candidates and store them in a list
        ##if currentrow != previous row:
            ##store
        
        while: 
           cur_line = csvreader.next()
                
           if pre_row != cur_row:
               
                    pass append.candidate(str(row[1]))
                    
            pre_row = cur_row
            
            except:
                ##candidate is in the list
                break     
                   ##All candidates are in list
            
            ##Count candidates # of votes
            can_votes [] = can_votes [] + 1 
            
            ##Calc percentage of votes for each candidate
            calc_pct_votes [] = can_votes[] / total_votes
            
            
            
    print('Election Results')
    print('---------------------')
    print(f'Total Votes: {total_votes}')
    print('---------------------')
    for can in can_list:     
        #print(f'{cans[]}: {vote_pct[]} ({can_votes[]})')
    print(f'---------------------')
    #find max(can_votes)
    #print(f'Winner: {winner}')
    print(f'---------------------')
    
    
    
    ###Save results in text file (write csv)
    