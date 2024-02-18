import csv 

class Stock:
    _types = (str,int,float)
    __slots__ = ('name','_shares','_price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
        

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)

    @property
    def cost(self):
        return self.shares * self.price
    
    @property
    def shares(self):
        return self._shares
    
    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        elif value < 0:
            raise ValueError('share must be >= 0')
        self._shares = value

    @property
    def price(self):
        return self._price 
    
    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError('Expected float')
        elif value < 0:
            raise ValueError('price must be >= 0')
        self._price = value
    
    def sell(self, amt):
        self.shares -= amt

def read_portfolio(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(Stock.from_row(row))
            # 3.1 version
            # yield Stock(row[0], int(row[1]),float(row[2]))
    return records


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
    print(portfolio)
    for s in portfolio:
        print(s)

    portfolio = read_portfolio('Data/portfolio.csv')
    print_table(portfolio, ['shares','shares','price'])

