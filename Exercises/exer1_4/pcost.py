

def portfolio_cost(filename):
    with open(filename, 'r') as f:
        data = []
        for line in f:
            data.append(line.split())

        cost = 0
        for stock in data:
            try:
                cost += float(stock[1]) * float(stock[2])
            except Exception as e:
                print(f'{e} for {stock}')

        return cost


print(portfolio_cost(
    '/Users/mitchellkrieger/Documents/GitHub/python-mastery/Data/portfolio2.dat'))
