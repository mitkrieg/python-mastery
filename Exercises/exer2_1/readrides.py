import csv
from collections import namedtuple


def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            records.append((row[0], row[1], row[2], int(row[3])))
    return records


def read_rides_as_dict(filename):
    '''
    Read the bus ride data as a list of dicts
    '''
    records = []
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


class RowClass:
    def __init__(self, route, date, daytype, rides) -> None:
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


def read_rides_as_class(filename):
    '''
    Read the bus ride data as a list of objects
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            records.append(RowClass(row[0], row[1], row[2], int(row[3])))
    return records


RowNamedTuple = namedtuple('Row', ['route', 'date', 'daytype', 'rides'])


def read_rides_as_named_tuple(filename):
    '''
    Read the bus ride data as a list of named tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            records.append(RowNamedTuple(row[0], row[1], row[2], int(row[3])))
    return records


class RowClassSlots:
    __slots__ = ['route', 'date', 'daytype', 'rides']

    def __init__(self, route, date, daytype, rides) -> None:
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


def read_rides_as_class_slots(filename):
    '''
    Read the bus ride data as a list of objects
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            records.append(RowClassSlots(row[0], row[1], row[2], int(row[3])))
    return records


if __name__ == '__main__':
    import tracemalloc

    readers = [
        read_rides_as_tuples,
        read_rides_as_dict,
        read_rides_as_class,
        read_rides_as_named_tuple,
        read_rides_as_class_slots
    ]

    for reader in readers:
        tracemalloc.start()
        rows = reader(
            '/Users/mitchellkrieger/Documents/GitHub/python-mastery/Data/ctabus.csv')
        print(reader.__name__)
        print('Memory Use: Current %d, Peak %d \n' %
              tracemalloc.get_traced_memory())
        tracemalloc.clear_traces()
