# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 11:17:54 2022

@author: LTabl
"""
import os
import csv

# Path to collect data from the Resources folder
budget_data_csv = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

# read in the csv file
with open(budget_data_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ',')

    #read the header row first
    csv_header = next(csvreader)  

    #create variable for months
    months_total = 0

    #create variable for Profit/Loss
    profit_loss = 0

    #create variable for Profit changes
    current_month = 0
    previous_month = 0
    profit_change = 0
    date = []
    profit_changes = []

    #loop through each row in csv to get month count and net sum of profits/losses 
    for row in csvreader:

        #count number of months
        months_total += 1

        #get net sum of profit/loss column
        current_month = int(row[1])
        profit_loss += int(row[1])

        #calculate monthly changes, not counting first row since it doesnt have a net change
        if months_total == 1:
            previous_month = current_month
        
        else:
            profit_change = current_month - previous_month

            #keep track of the date
            date.append(row[0])

            #add to profit changes list
            profit_changes.append(profit_change)

            #reset values
            previous_month = current_month
    
    #calculate changes in "Profit/Losses" over the entire period
    sum_profit_changes = sum(profit_changes)

    #now calculate average of those changes
    average_profit_change = sum_profit_changes/(months_total - 1)

    #get the greatest increase in profits (date and amount) over the entire period
    max_profit_change = max(profit_changes)
    max_profit_date = profit_changes.index(max_profit_change)

    #get the greatest decrease in profits (date and amount) over the entire period
    min_profit_change = min(profit_changes)
    min_profit_date = profit_changes.index(min_profit_change)

# once the analysis is complete
# print Summary header
print("Financial Analysis")
print("--------------------------")
# print total months
print(f'Total Months: {months_total}')
# print net total amount of "Profit/Losses" over the entire period
print(f'Total: ${profit_loss}')
#print average change
print(f'Average Change: ${(round(average_profit_change,2))}')
#print(change_from_previous)
print(f'Greatest Increase in Profits: {date[max_profit_date]} (${(str(max_profit_change))})')
print(f'Greatest Decrease in Profits: {date[min_profit_date]} (${(str(min_profit_change))})')

#export results to txt file
#specify the file to write to
budget_results = os.path.join("Analysis", "budget_results.txt")
with open(budget_results, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("--------------------------\n")
    txtfile.write(f'Total Months: {months_total}\n')
    txtfile.write(f'Total: ${profit_loss}\n')
    txtfile.write(f'Average Change: ${(round(average_profit_change,2))}\n')
    txtfile.write(f'Greatest Increase in Profits: {date[max_profit_date]} (${(str(max_profit_change))})\n')
    txtfile.write(f'Greatest Decrease in Profits: {date[min_profit_date]} (${(str(min_profit_change))})\n')
