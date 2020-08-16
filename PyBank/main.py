# Modules
import os
import csv

print("__________________________________________________________")

csvpath = os.path.join("Resources", "budget_data.csv")

# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #setting variables
    months = []
    net_rev = 0
    maxRev = 0
    minRev = 0

    #loop data for months and net rev
    for row in csvreader:
        months.append(row[0])
        net_rev +=int(row[1])

        #find max revenue
        if(maxRev<int(row[1])):
            maxRev = int(row[1])
            maxRev_month = row[0]

        #find min revenue
        if(minRev>int(row[1])):
            minRev=int(row[1])
            minRev_month = row[0]

    #print the statements
    print(f'Financial Analysis')
    print(f'----------------------------')
    print(f'Total Months: {len(months)}')
    print(f'Net Revenue: ${net_rev}')
    print(f'Average Change: ${net_rev / len(months), 2}')
    print(f'Greatest increase in Profits: {maxRev_month} ({maxRev})')
    print(f'Greatest decrease in Profits: {minRev} ({minRev_month})')

print('________________________________________________________________')
#The net total amount of "Profit/Losses" over the entire period


#The average of the changes in "Profit/Losses" over the entire period


#The greatest increase in profits (date and amount) over the entire period


#The greatest decrease in losses (date and amount) over the entire period


#As an example, your analysis should look similar to the one below:
    
    #Financial Analysis
    #----------------------------
    #Total Months: 86
    #Total: $38382578
    #Average  Change: $-2315.12
    #Greatest Increase in Profits: Feb-2012 ($1926159)
    #Greatest Decrease in Profits: Sep-2013 ($-2196167)