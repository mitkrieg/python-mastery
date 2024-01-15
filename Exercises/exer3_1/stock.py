import csv 

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price
    
    def sell(self, amt):
        self.shares -= amt

def read_portfolio(filename):
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            yield Stock(row[0], int(row[1]),float(row[2]))


# 3.1 version
# def print_portfolio(portfolio):
#     print('%10s %10s %10s' % ('name', 'shares', 'price'))
#     print('---------- ---------- ----------')
#     for s in portfolio:
#         print('%10s %10d %10.2f' % (s.name, s.shares, s.price))
            
# 3.2 version
def print_table(data, cols):
    print(' '.join(['%10s' % (col) for col in cols]))
    print(' '.join('----------' for col in cols))
    for d in data:
        print(' '.join('%10s' % (getattr(d,col)) for col in cols))

if __name__ == '__main__':
    portfolio = read_portfolio('Data/portfolio.csv')
    for s in portfolio:
        print(s)

    portfolio = read_portfolio('Data/portfolio.csv')
    print_table(portfolio, ['shares','shares','price'])

