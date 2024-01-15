from collections.abc import Sequence
import csv
from collections import Counter

class RideData(Sequence):
    def __init__(self,data = None):
        if data:
            self.routes = data['routes']
            self.dates = data['dates']
            self.daytypes = data['daytypes']
            self.numrides = data['numrides']
        else:
            self.routes = []
            self.dates = []
            self.daytypes = []
            self.numrides = []

    def __len__(self):
        # assume all lists have the same length
        return len(self.routes)
    
    def __getitem__(self, index):
        if isinstance(index,slice):
            return RideData({
            'routes': self.routes[index],
            'dates': self.dates[index],
            'daytypes': self.daytypes[index],
            'numrides': self.numrides[index]
        })
        return {
            'route': self.routes[index],
            'date': self.dates[index],
            'daytype': self.daytypes[index],
            'rides': self.numrides[index]
        }
    
    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])

    def read(self, filename):
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                self.append({
                    'route': row[0], 
                    'date': row[1], 
                    'daytype': row[2], 
                    'rides' : int(row[3])                    
                })

def read_rides_as_collector_class(filename):
    '''
    Read the bus ride data as collector class
    '''
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            records.append({
                'route': row[0],
                'date': row[1],
                'daytype': row[2],
                'rides': int(row[3])
            })
    return records

if __name__ == '__main__':

    print('XXXXXXXX OUTPUT FROM 2-2 XXXXXXXXXXX')
    rows = RideData()
    rows.read('/Users/mitchellkrieger/Documents/Github/python-mastery/Data/ctabus.csv')
    print('How many bus routes exist in Chicago?')
    print(len({row['route'] for row in rows}))
    print('How many people rode the number 22 bus on February 2, 2011? What about any route on any date of your choosing?')
    ppl = Counter()
    route22 = [row for row in rows if row['route'] == '22']
    for row in route22:
        ppl[row['date']] += row['rides']
    print(ppl['02/02/2011'])
    print('What is the total number of rides taken on each bus route?')
    routes = Counter()
    for row in rows:
        routes[row['route']] += row['rides']
    for route, rides in routes.items():
        print(f'Route: {route}\tRides: {rides}')

    print('What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?')
    routes_2001 = Counter()
    routes_2011 = Counter()
    for row in [x for x in rows if x['date'].split('/')[-1] == '2001']:
        routes_2001[row['route']] += row['rides']
    for row in [x for x in rows if x['date'].split('/')[-1] == '2011']:
        routes_2011[row['route']] += row['rides']
    diff = routes_2011 - routes_2001
    top = diff.most_common(5)
    for route, rides in top:
        print(f'Route: {route}\tRides: {rides}')

    print('XXXXXXXXXX TESTING CLASS XXXXXXXXXXXXX')
    print(f'Length: {len(rows)}')
    r = rows[0:10]
    print('Slicing:')
    print(f'Slice length: {len(r)}')
    for i in range(5):
        print(f'Index {i}: {r[i]}')