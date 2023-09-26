# reading cv files
import os
import csv

# Set path for files
csvpath = 'Resources/budget_data.csv'
#Declare variables
with open (csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next (csvreader)
    rowcount = 0
    netcount = 0


    for row in csvreader:
        rowcount += 1
        netcount = netcount + int(row[1])
        avg_change = row [1]

print("Financial Analysis")
print("--------------")
print(f'Total Months:{rowcount}')
print(f'Total: ${netcount}')
print(f'Average Change: ${avg_change}')

# Print the results to "PyPoll.txt" file
print("Financial Analysis", file=open("PyBank.txt", "a"))
print("----------------------------", file=open("PyBank.txt", "a"))
print(f"Total Months: {rowcount:,}", file=open("PyBank.txt", "a"))
print(f"Total : {netcount:,}", file=open("PyBank.txt", "a"))
print(f'Average Change: ${avg_change}', file=open("PyBank.txt", "a"))



