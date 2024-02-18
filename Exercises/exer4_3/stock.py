import csv
from typing import Any 
from validate import PositiveInteger, PositiveFloat, NonEmptyString

class Stock:
    _types = (str,int,float)
    name = NonEmptyString()
    shares = PositiveInteger()
    price = PositiveFloat()
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __setattr__(self, name: str, value: Any) -> None:
        if name not in {'name', '_shares', '_price','shares','price'}:
            raise AttributeError('No attribute %s' % name)
        super().__setattr__(name,value)

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
        self._shares = PositiveInteger.check(value)

    @property
    def price(self):
        return self._price 
    
    @price.setter
    def price(self, value):
        self._price = PositiveFloat.check(value)

    # @name.setter 
    # def name(self, value):
    #     self._name = NonEmptyString.check(value)
    
    def sell(self, amt):
        self.shares -= amt

    def __repr__(self) -> str:
        return 'Stock(' + ', '.join(["'" + self.name + "'", str(self.shares), str(self.price)])  + ')'
    
    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) == (other.name, other.shares, other.price))

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
    print(repr(Stock('GOOG', 100, 490.10)))

