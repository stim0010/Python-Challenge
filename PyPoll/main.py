#import csv library
import csv

##Determine the csv file path
poll_csv = "Resources/election_data.csv"

##Open poll data file
with open(poll_csv) as csvfile:
    
    ##Read Poll data csv file
    csvreader=csv.reader(csvfile, delimiter=',')
    
    ##skip header
    header=next(csvreader)
    
    #define variables
    total_votes = 0
    curr_row = 0
    prev_row = 0
    
    # tuple
    name, pct_vote, can_votes = ('','','')
    
    ##For loop throught the rows in the csv file
    for row in csvreader:
        
        ##Calc total number of votes by counting the rows
        total_votes = total_votes + 1
        
        curr_row = int(row[0])
        
        if curr_row != prev_row:
            append.name(str(row[1]))
        else:
            pre_row = cur_row
        
                ##candidate is in the list
               # break     
                   ##All candidates are in list
            
            ##Count candidates # of votes
            #can_votes [] = can_votes [] + 1 
            
            ##Calc percentage of votes for each candidate
            #calc_pct_votes [] = can_votes[] / total_votes
            
            
###Output the results from the csv file          
    print('Election Results')
    print('---------------------')
    print(f'Total Votes: {total_votes}')
    print('---------------------')
    #for can in can_list:     
        #print(f'{cans[]}: {vote_pct[]} ({can_votes[]})')
    print(f'---------------------')
    #find max(can_votes)
    #print(f'Winner: {winner}')
    print(f'---------------------')
    
#######Write summary output to a csv file
# Specify the file to write to
#output_path = "PyPoll_summary.txt"

# Open the file using "write" mode. Specify the variable to hold the contents
#with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    #csvwriter = csv.writer(csvfile, delimiter=',')
    
    #csvwriter.writerow([f'---------------------'])