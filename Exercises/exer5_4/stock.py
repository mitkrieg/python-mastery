from typed_property import String, Integer, Float

class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price) -> None:
        self.name = name
        self. shares = shares
        self.price = price