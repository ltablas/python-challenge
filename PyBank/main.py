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
    months = []

    #create variable for Profit/Loss
    profits_losses = []

    #create variable for net
    net = (float(row[1]) for row in csvreader)
    net_sum = sum(net)

    for row in csvreader:
        month = row[0]
        profit_loss = row[1]
        
        months.append(month)
        profits_losses.append(profit_loss)

# once the analysis is complete
# print Summary header
print("Financial Analysis")
print("--------------------------")
# print total months
print("Total Months: ", len(months))

# print net total amount of "Profit/Losses" over the entire period
print("Total: $", net_sum)

#print(f'Average Change: {avg_change}')
#print(f'Greatest Increase in Profits: {month} ({change})')
#print(f'Greatest Decrease in Profits: {month} ({change})')