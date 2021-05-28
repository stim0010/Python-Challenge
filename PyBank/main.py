
import csv

##Define the data path
budget_csv=('Resources/budget_data.csv')

##Create function to calculate and display a summary of the Budget
#def budsummary(budget):

    ##Data types
    
    ###what data type is the date & do I even need these variables?
    #date = str(budget[0])
    #pl = int(budget[1])

    ##Total number of months (count rows)
    #total_months = len(list(budget[0]))

    ##Net total of profit/losses for the entire period(sum of profit/loss)
    ##need to determine the proper way to sum +/- integers
    ##Do I loop or is there a python lib
    #nptotal=sum(budget[1])
    
    ##Calculate the change from start to end of profit/loss(profit[end]-profit[0])
    ##Use total_months to determine the final row in the data set
    #plchange=(budget_date[months]-budgetdata[0])

    ##Greated increase (max profit/loss)
    #maxpl=max(budget[1])

    ##Greatest decrease (min profit/loss)
    #minpl=min(budget[1])
    
    ####################################################################
    
    #print(f'Financial Analysis')
    #print(f'-----------------------------')
    #print(f'Total Months: {total_months}')
    #print(f'Total: {nptotal}')
    #print(f'Average Change: {plchange}')
    #print(f'Greatest increase in profits: {date[row]} + '('+{maxpl}+')'')
    #print(f'Greatest decrease in profits: {date[row]} + '('+{minpl}+')'')
    
####Financial Analysis
####--------------------------
####Total Months: '{total_months}'
####Total: '{nptotal}'
####Average Change: '{plchange}'
####Greatest increase in profits: {date[0]} + '('{maxpl}')
####Greatest decrease in profits: {date[0]} + '('{minpl}')

#############################################################################

##Open budget data file
with open(budget_csv, 'r') as csvfile:

    csvreader=csv.reader(csvfile, delimiter=",")

    header = next(csvreader)
    print(len(list(csvreader)))
