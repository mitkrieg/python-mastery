import sys
sys.path.append('/Users/mitchellkrieger/Documents/GitHub/python-mastery')
from Exercises.exer2_1 import readrides
from collections import Counter

rows = readrides.read_rides_as_dict('/Users/mitchellkrieger/Documents/Github/python-mastery/Data/ctabus.csv')
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