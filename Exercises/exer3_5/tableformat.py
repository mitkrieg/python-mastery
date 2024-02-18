class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()
    
    def row(self, rowdata):
        raise NotImplementedError()
    

def print_table(records, fields, formatter):
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ') * len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(str(d) for d in rowdata))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print("<tr> <th>" + "</th> <th>".join(headers) + "</th> </tr>")

    def row(self, rowdata):
        print("<tr> <td>" + "</td> <td>".join(str(d) for d in rowdata) + "</td> </tr>")

def create_formatter(type):
    match type:
        case 'html':
            return HTMLTableFormatter()
        case 'csv':
            return CSVTableFormatter()
        case 'text':
            return TextTableFormatter()
        case _:
            return TableFormatter()
        

if __name__ == '__main__':
    import stock, reader
    portfolio = reader.read_csv_as_instances('Data/portfolio.csv',stock.Stock)
    formatter = create_formatter('html')
    print_table(portfolio, ['name','shares','price'], formatter)
