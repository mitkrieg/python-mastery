import csv
import tracemalloc

def read_rides_as_columns(filename):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)


if __name__ == '__main__':
    tracemalloc.start()
    columns = read_rides_as_columns('/Users/mitchellkrieger/Documents/GitHub/python-mastery/Data/ctabus.csv')
    print(tracemalloc.get_traced_memory())
