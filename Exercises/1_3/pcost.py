
with open('/Users/mitchellkrieger/Documents/GitHub/python-mastery/Data/portfolio.dat', 'r') as f:
    data = []
    for line in f:
        data.append(line.split())

    cost = 0
    for stock in data:
        cost += float(stock[1]) * float(stock[2])

    print(cost)
