# pcost.py
#
# Exercise 1.27

import sys
import csv

def portfolio_cost(filename):
    with open(filename,'rt') as file:
        next(file)
        totalCost = 0.0
        for line2 in file:
            line2Details = line2.split(',')
            totalCost = totalCost + (int(line2Details[1])*float(line2Details[2]))
        return totalCost 

def portfolio_cost_using_enumeration_and_dict(filename):
    with open(filename,'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        totalCost = 0.0
        for rowno, row in enumerate(rows, start=1):
            rec = dict(zip(headers,row))
            try:
                noOfShares = int(rec['shares'])
                price = float(rec['price'])
                totalCost += noOfShares * price
            except ValueError:
                    print(f'Row{rowno}: Bad row:{row}')
        return totalCost 

def portfolio_cost_using_enumeration_and_dict(filename):
    with open(filename,'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        totalCost = 0.0
        for rowno, row in enumerate(rows, start=1):
            rec = dict(zip(headers,row))
            try:
                noOfShares = int(rec['shares'])
                price = float(rec['price'])
                totalCost += noOfShares * price
            except ValueError:
                    print(f'Row{rowno}: Bad row:{row}')
        return totalCost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

finalCost = portfolio_cost(filename)
print('Final Cost: ',finalCost)

filename = 'Data/missing.csv'
finalCost = portfolio_cost_using_enumeration_and_dict(filename)
print('Final Cost: ',finalCost)

filename = 'Data/portfoliodate.csv'
finalCost = portfolio_cost_using_enumeration_and_dict(filename)
print('Final Cost: ',finalCost)


        