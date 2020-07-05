# pcost.py
#
# Exercise 1.27

import sys

def portfolio_cost(filename):
    with open(filename,'rt') as file:
        next(file)
        totalCost = 0.0
        for line2 in file:
            line2Details = line2.split(',')
            totalCost = totalCost + (int(line2Details[1])*float(line2Details[2]))
        return totalCost 

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
finalCost = portfolio_cost(filename)
print('Final Cost: ',finalCost)


        