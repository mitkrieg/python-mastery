import sys
sys.path.append('/Users/mitchellkrieger/Documents/GitHub/python-mastery')
import tracemalloc

filename = '/Users/mitchellkrieger/Documents/GitHub/python-mastery/Data/ctabus.csv'

tracemalloc.start()
from Exercises.exer2_1 import readrides
print('List of dictionaries read:')
rows = readrides.read_rides_as_dict(filename)
route22 = [row for row in rows if row['route'] == '22']
print(f'Max ridership: {max(route22, key=lambda x: int(x["rides"]))}')
print(f'Memory: {tracemalloc.get_traced_memory()}')

tracemalloc.clear_traces()

tracemalloc.start()
import csv
print('Using generators:')
f = open(filename)
fcsv  = csv.reader(f)
headers = next(fcsv)
rows = (dict(zip(headers,row)) for row in fcsv)
route22 = (row for row in rows if row['route'] == '22')
print(f'Max ridership: {max(route22, key=lambda x: int(x["rides"]))}')
print(f'Memory: {tracemalloc.get_traced_memory()}')



