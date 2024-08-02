import csv
from typing import List, Dict

def convert_csv(lines, func, *, headers=None):

    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    return map(lambda rows: func(headers, rows), rows)

def make_dict(headers, row):
    return dict(zip(headers,row))

def csv_as_dicts(f, types: List[str], *, headers=None) -> List[Dict]:
    return convert_csv(f, make_dict, headers=headers)

def read_csv_as_dicts(file: str, types: List[str], *, headers=None) -> List[Dict]:
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    with open(file) as f:
        
        return csv_as_dicts(f, types, headers=headers)

def csv_as_instances(f, cls, *, headers=None) -> List[Dict]:
    '''
    Read CSV data into a list of instances
    '''
    return convert_csv(f, lambda headers, row: cls.from_row(row))

def read_csv_as_instances(file: str, cls, *, headers=None) -> List[Dict]:
    with open(file, cls) as f:
        return csv_as_instances(f, cls, headers=headers)
    



