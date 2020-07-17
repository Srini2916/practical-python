# report.py
#
# Exercise 2.4
import csv
import sys
from pprint import pprint


filename2 = 'Data/prices.csv'
if(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

################## this one using split##########
def read_portfolio(filename):
    portfolio = []

    with open(filename,'rt') as f:
        for line in f:
            lineItem = line.split(",")
            portfolio_tuple = (lineItem[0],lineItem[1],lineItem[2])
            portfolio.append(portfolio_tuple)
    return portfolio
print('Using List split() and Iteration :')
pprint(read_portfolio('Data/portfolio.csv'))

########### this one using csv and tuple#########
def read_portfolio_with_csv(filename):
    portfolio = []

    with open(filename,'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for lineItem in rows:
            portfolio_tuple = (lineItem[0],int(lineItem[1]),float(lineItem[2]))
            portfolio.append(portfolio_tuple)
    return portfolio

tupleList = read_portfolio_with_csv(filename)
#print(tupleList[0])
#print(tupleList[0][1])
total = 0.0
for name, shares, price in tupleList:
    total += shares * price
print("Total ::",total)
print('Using csv reader :')
pprint(tupleList)

##########this one using csv and dict###########
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

portfolio_list = read_portfolio_with_csv_And_dict(filename)
#print('Using dictionary :')
pprint(portfolio_list)
#print(portfolio_list[0])
#print(portfolio_list[0]['shares'])
costValueTotal = 0.0
for s in portfolio_list:
    costValueTotal += s['shares'] * s['price']
print("Total Cost value::",costValueTotal)

######### this one using csv and dict with try/catch######
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

priceList = read_prices('Data/prices.csv')
print("Prices csv as dict:",priceList)
total_value = 0.0

for s in portfolio_list:
    total_value += s['shares'] * priceList[s['name']]

print("Total Current Value :",total_value)
print("Total gain/loss :",total_value - costValueTotal)

######## this one using list##########
def make_report(portfolio, prices):
    report_tuple_list = []
    for stockitem in portfolio:
        currentprice = prices[stockitem["name"]] 
        profitLoss = currentprice - stockitem["price"]
        listItem = (stockitem["name"],stockitem["shares"], currentprice, profitLoss)
        report_tuple_list.append(listItem)
    return report_tuple_list  

######## Formatting in tabular form by calling above method#######
report = make_report(portfolio_list, priceList)
headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))
for r in report:
    print('%10s %10d %10.2f %10.2f' % r)

print('%10s %10s %10s %10s' %headers)
print(('-' * 10 + ' ') * len(headers))
for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
        
####### this one using csv, enumerate and zip####
def make_report_using_zip(filename):
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        lineItem = []
        portfolio_total = 0.0
        for rowno, row in enumerate(rows, start=1):
            lineItem = dict(zip(headers,row))
            #print(lineItem.items())
            #print(lineItem)
            pricelist = list(zip(lineItem.values(), lineItem.keys()))
            print(pricelist)
            noOfShares = int(lineItem['shares'])
            price = float(lineItem['price'])
            portfolio_total += noOfShares * price
    return portfolio_total

print('Using make_report_using_zip ::', make_report_using_zip('Data/portfoliodate.csv'))

############ using Collections Counter(),defaultdict,deque#######

def make_tabluar_using_Collections():
    portfolio = read_portfolio_with_csv('Data/portfolio.csv')
    from collections import Counter
    holdings = Counter()
    for s in portfolio:
        holdings[s[0]] += s[1]
    
    portfolio2 = read_portfolio_with_csv('Data/portfolio2.csv')
    holdings2 = Counter()
    for s in portfolio2:
        holdings2[s[0]] += s[1]  

    return holdings + holdings2
print("make_tabluar_using_Collections :: Combined holdings::",make_tabluar_using_Collections())
##########################################################













