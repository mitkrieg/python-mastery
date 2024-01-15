import csv

def read_csv_as_dicts(filename, dtypes):
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            yield {name:func(val) for name,func,val in zip(headers,dtypes,row)}

if __name__ == '__main__':   
    import tracemalloc
    from sys import intern  
    print('TEST portfolio.csv')
    portfolio = read_csv_as_dicts('/Users/mitchellkrieger/Documents/GitHub/python-mastery/Data/portfolio.csv',[str,int,float])
    for s in portfolio:
        print(s)

    print('TEST ctabus.csv')
    tracemalloc.start()
    rides = list(read_csv_as_dicts('/Users/mitchellkrieger/Documents/GitHub/python-mastery/Data/ctabus.csv',[str,str,str,int]))
    print(len(rides))
    print(rides[0])
    routeids = {id(row['route']) for row in rides} #need to reuse the same route id strings in mem rather than create new strings for each row
    print(len(routeids))
    print(tracemalloc.get_traced_memory())
    tracemalloc.clear_traces()

    tracemalloc.start()
    rides = list(read_csv_as_dicts('/Users/mitchellkrieger/Documents/GitHub/python-mastery/Data/ctabus.csv',[intern,str,str,int]))
    print(len(rides))
    print(rides[0])
    routeids = {id(row['route']) for row in rides} #reuse the same route id strings in mem rather than create new ones
    print(len(routeids))
    print(tracemalloc.get_traced_memory())
    tracemalloc.clear_traces()

    tracemalloc.start()
    rides = list(read_csv_as_dicts('/Users/mitchellkrieger/Documents/GitHub/python-mastery/Data/ctabus.csv',[intern,intern,str,int]))
    print(len(rides))
    print(rides[0])
    routeids = {id(row['route']) for row in rides} #reuse the same route id strings in mem rather than create new ones
    print(len(routeids))
    print(tracemalloc.get_traced_memory())
    tracemalloc.clear_traces()
