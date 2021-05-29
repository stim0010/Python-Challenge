
import csv

##Define the data path
budget_csv=('Resources/budget_data.csv')

##Open budget data file
with open(budget_csv, 'r') as csvfile:
    
    ##Read the csv file
    csvreader = csv.reader(csvfile, delimiter=",")

    ##Skip the headers
    header = next(csvreader)
    
    ##Set count values
    total_months = 0
    nptotal = 0
    avgchange = 0

    for row in csvreader:
        
        ##Find number of months by counting each row
        total_months = total_months + 1
        
        ##Find the total profit/loss by adding each row
        nptotal = nptotal + int(row[1])
        
        ##Find the average change in profit/loss between each month
        ##Need to use 'while' to subtract current row from previous row 
        #avgchange = 
        
      
    
    print(f'Financial Analysis')
    print(f'---------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: $ {nptotal}')
    #print(f'Average Change: {avgchange}')
    #print(f'Greatest increase in profits: {maxpl}')
    #print(f'Greatest decrease in profits:{minpl}')