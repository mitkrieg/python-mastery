import csv
from typing import List, Dict

def csv_as_dicts(f, types: List[str], *, headers=None) -> List[Dict]:
    records = []
    lines = csv.reader(f)
    if headers is None:
        headers = next(lines)
    for row in lines:
        record = { name: func(val) 
                    for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

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
    records = []
    lines = csv.reader(f)
    if headers is None:
        headers = next(lines)
    for row in lines:
        record = cls.from_row(row)
        records.append(record)
    return records

def read_csv_as_instances(file: str, cls, *, headers=None) -> List[Dict]:
    with open(file, cls) as f:
        return csv_as_instances(f, cls, headers=headers)
