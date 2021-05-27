import csv

##Define the data path
budget_csv ='../Resources/Budget_Date.csv'

##Create function to calculate and display a summary of the Budget
def printbudsummary(budget_data):

    ##Data types
    date = str(budget_data[0])
    pl = int(budget_data[1])

    ##Total number of months (count rows)

    ##Net total of profit/losses for the entire period(sum of profit/loss)

    ##Calculate the change from start to end of profit/loss(profit[end]-profit[0])

    ##Greated increase (max profit/loss)

    ##Greatest decrease (min profit/loss)



##Open budget data file
with open(budget_csv) as csvfile:

    csvreader=csv.reader(csvfile, delimiter=",")

    header = next(csvreader)