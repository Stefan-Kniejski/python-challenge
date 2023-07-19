import os
import csv
from statistics import mean
# Path to collect data from the Resources folder
budget_data = os.path.join('.','Resources', 'budget_data.csv')
# Read in the CSV file
with open(budget_data, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    first_row=next(csvreader)
    prev_net=int(first_row[1])
    count = 1
    total = int(first_row[1])
    change_list=[]
    # Loop through the data
    for row in csvreader:
        count = count + 1
        total = total + int(row[1])
        change= int(row[1])- prev_net
        prev_net=int(row[1])
        change_list.append(change)
    pmax = max(change_list)
    pmin = min(change_list)
    avg = mean(change_list)
    
    # Print the results
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {count}")
    print("Total: "'${:,.2f}'.format(total))
    print("Average Change: "'${:,.2f}'.format(avg))
    print("Greatest Increase in Profits: "'${:,.2f}'.format(pmax))
    print("Greatest Decrease in Profits: "'${:,.2f}'.format(pmin))