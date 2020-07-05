# report.py
#
# Exercise 2.4
import csv
import sys
from pprint import pprint

def read_portfolio(filename):
    portfolio = []

    with open(filename,'rt') as f:
        for line in f:
            lineItem = line.split(",")
            portfolio_tuple = (lineItem[0],lineItem[1],lineItem[2])
            portfolio.append(portfolio_tuple)
    return portfolio

def read_portfolio_with_csv(filename):
    portfolio = []

    with open(filename,'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for lineItem in rows:
            portfolio_tuple = (lineItem[0],int(lineItem[1]),float(lineItem[2]))
            portfolio.append(portfolio_tuple)
    return portfolio

def read_portfolio_with_csv_And_dict(filename):
    
    portfolio_list = []
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for lineItem in rows:
            portfolio_dict = {}
            portfolio_dict["name"] = lineItem[0]
            portfolio_dict["shares"] = int(lineItem[1])
            portfolio_dict["price"] = float(lineItem[2]) 
            portfolio_list.append(portfolio_dict)
    return portfolio_list

def read_prices(filename2):
    prices_dict = {}
    with open(filename2) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices_dict[row[0]] = float(row[1])
            except  IndexError:
                pass
    return prices_dict

filename2 = 'Data/prices.csv'
if(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

print('Using List split() and Iteration :')
pprint(read_portfolio(filename))

tupleList = read_portfolio_with_csv(filename)
print(tupleList[0])
print(tupleList[0][1])
total = 0.0
for name, shares, price in tupleList:
    total += shares * price
print("Total ::",total)
print('Using csv reader :')
pprint(tupleList)

portfolio_list = read_portfolio_with_csv_And_dict(filename)
print('Using dictionary :')
pprint(portfolio_list)
print(portfolio_list[0])
print(portfolio_list[0]['shares'])
costValueTotal = 0.0
for s in portfolio_list:
    costValueTotal += s['shares'] * s['price']
print("Total Cost value::",costValueTotal)

priceList = read_prices('Data/prices.csv')
print("Prices csv as dict:",priceList)
total_value = 0.0

for s in portfolio_list:
    total_value += s['shares'] * priceList[s['name']]

print("Total Current Value :",total_value)
print("Total gain/loss :",total_value - costValueTotal)
