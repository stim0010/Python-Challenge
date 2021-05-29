
import csv

##Define the data path
budget_csv=('Resources/budget_data.csv')

###FUNCTIONS

##Open budget data file
with open(budget_csv, 'r') as csvfile:
    
    ##Read the csv file
    csvreader = csv.reader(csvfile, delimiter=",")

    ##Skip the headers
    header = next(csvreader)
    
    ##Define variables
    total_months = 0
    nptotal = 0
    total_change = 0
    current_row = 0
    prev_row = 0
    avgchange = 0
    month_change = 0
    maxpl = 0
    minpl = 0

    for row in csvreader:
        
        ###TOTAL MONTHS
        ##Find number of months by counting each row
        total_months = total_months + 1
        
        ###TOTAL PROFIT/LOSS
        ##Find the total profit/loss by adding each row
        nptotal = nptotal + int(row[1])
        
        ###AVERAGE CHANGE (MONTH to MONTH)
        ##Find the average change in profit/loss between each month
        current_row = int(row[1])
        
        ##if statement stops the change in profit/loss from using 0 on the first month
        if prev_row == 0:
            prev_row = 0
        else:
            month_change = (current_row - prev_row)   
        
        prev_row = current_row
        total_change = total_change + month_change
        
    
    ## Calc average change in profit/loss (month to month)
    avgchange = total_change / (total_months - 1)
    format_avgchange = "{:+.2f}".format(avgchange)
      
    ###PRINT OUTPUT SUMMARY
    
    print(f'Financial Analysis')
    print(f'---------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: $ {nptotal}')
    ##format number to 2 decimal places
    print(f'Average Change: {format_avgchange}')
    #print(f'Greatest increase in profits: {row[0] -- max} ({maxpl})'
    #print(f'Greatest decrease in profits: {row[0] -- min} ({minpl})'
    
#######Write summary output to a csv file
# Specify the file to write to
#output_path = "PyBank_summary.txt"

# Open the file using "write" mode. Specify the variable to hold the contents
#with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    #csvwriter = csv.writer(csvfile, delimiter=',')

    ##OUTPUT TEXT
   # csvwriter.writerow([f'Financial Analysis'])
   # csvwriter.writerow([f'---------------------'])
   # csvwriter.writerow([f'Total Months: {total_months}'])
   # csvwriter.writerow([f'Total Months: {total_months}'])
    #csvwriter.writerow([f'Average Change: {avgchange}'])
    #csvwriter.writerow([f'Greatest increase in profits: {row[0] -- max} ({maxpl})'])
    #csvwriter.writerow([f'Greatest decrease in profits: {row[0] -- min} ({minpl})'])