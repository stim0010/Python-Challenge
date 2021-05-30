##Import csv library
import csv

##Define the data path
budget_csv = ('Resources/budget_data.csv')

###FUNCTIONS

#def counters(budget_data):

#def 

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
    current_row = 0.00
    prev_row = 0.0
    avgchange = 0
    month_change = 0
    maxpl = 0.0
    minpl = 0.0
   
  
###For loop to move through the rows in the csv file
    for row in csvreader:
        
    ###TOTAL MONTHS
        ##Find number of months by counting each row
        total_months += 1
        
    ###TOTAL PROFIT/LOSS
        ##Find the total profit/loss by adding each row
        nptotal += int(row[1])
        
    ###AVERAGE CHANGE (MONTH to MONTH)
        ##Find the average change in profit/loss between each month
        current_row = float(row[1])
        
       
    ##Find max for row[1] and determine date 
        if current_row > prev_row:
            maxpl = current_row
            max_date = row[0]
        
    ##Find min for row[1] and determine date
        if current_row < prev_row:
            minpl = current_row
            min_date = row[0]
        
        ##if statement stops the change in profit/loss from using 0 on the first month
        if prev_row == 0:
            prev_row = 0
        else:
            month_change = (current_row - prev_row)   
    
    ## Determine total change for average change calc
        prev_row = current_row
        total_change = total_change + month_change
        
    ## Calc average change in profit/loss (month to month)
    avgchange = total_change / (total_months - 1)
    
    ## Format the avgchange output to 2 decimal places with +/-
    format_avgchange = "{:+.2f}".format(avgchange)
      
    ###PRINT OUTPUT SUMMARY
    
    print(f'Financial Analysis')
    print(f'---------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: $ {nptotal}')
    ##format number to 2 decimal places
    print(f'Average Change: $ {format_avgchange}')
    print(f'Greatest increase in profits: {max_date} ({maxpl})')
    print(f'Greatest decrease in profits: {min_date} ({minpl})')
    
#######Write summary output to a csv file
# Specify the file to write to
#output_path = "PyBank_summary.txt"

# Open the file using "write" mode. Specify the variable to hold the contents
#with open(output_path, 'w', newline='') as csvfile:

    #Initialize csv.writer
    #csvwriter = csv.writer(csvfile, delimiter=',')

    ##OUTPUT TEXT
    #csvwriter.writerow([f'Financial Analysis'])
    #csvwriter.writerow([f'---------------------'])
    #csvwriter.writerow([f'Total Months: {total_months}'])
    #csvwriter.writerow([f'Total Months: {total_months}'])
    #csvwriter.writerow([f'Average Change: {avgchange}'])
    #csvwriter.writerow([f'Greatest increase in profits: {max_date} ({maxpl})'])
    #csvwriter.writerow([f'Greatest decrease in profits: {min_date} ({minpl})'])