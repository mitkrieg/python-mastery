import csv
from collections.abc import Sequence

class DataCollection(Sequence):
    def __init__(self, data = None, headers=None):
        if data and headers:
            self.headers = headers
            for key, value in data.items():
                if isinstance(value,list):
                    setattr(self,key,value)
                else:
                    setattr(self,key,[value])
        else:
            self.headers = []

    def append(self, data):
        for key, value in data.items():
            try:
                col = getattr(self, key)
                col.append(value)
            except:
                setattr(self, key, [])
                col = getattr(self, key)
                col.append(value)
                self.headers.append(key)
            
    def __getitem__(self, index):
        if isinstance(index,slice):
            return DataCollection({
                header: getattr(self,header)[index] for header in self.headers
            },headers=self.headers)
        else:
            return {
                header: getattr(self,header)[index] for header in self.headers
            }
    
    def __len__(self):
        print(self.headers)
        if len(self.headers) == 0:
            return 0
        else:
            return len(getattr(self,self.headers[0]))

    def read(self, filename, dtypes):
        with open(filename) as f:
            rows = csv.reader(f)
            self.headers = next(rows)
            for row in rows:
                self.append({name: func(val) for name, func, val in zip(self.headers, dtypes, row)})


def read_csv_as_collector_class_dynamic(filename,dtypes):
    records = DataCollection()
    records.read(filename, dtypes)
    return records


if __name__ == '__main__':
    print('TEST portfolio.csv')
    portfolio = read_csv_as_collector_class_dynamic('/Users/mitchellkrieger/Documents/GitHub/python-mastery/Data/portfolio.csv',[str,int,float])
    for s in portfolio:
        print(s)

    print('TEST ctabus.csv')
    rides = list(read_csv_as_collector_class_dynamic('/Users/mitchellkrieger/Documents/GitHub/python-mastery/Data/ctabus.csv',[str,str,str,int]))
    print(len(rides))
    print(rides[0:10])
    print(rides[577560])