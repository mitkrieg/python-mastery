from abc import ABC, abstractclassmethod

class TableFormatter(ABC):
    
    @abstractclassmethod
    def headings(self, headers):
        pass
    
    @abstractclassmethod
    def row(self, rowdata):
        pass
    

def print_table(records, fields, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError('formatter must be of type TableFormatter')
    
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

class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)

class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])

class PortfolioColFormatter(ColumnFormatMixin, TextTableFormatter):
    formats = ['%s', '%d', '%0.2f']

class PortfolioHeadFormatter(UpperHeadersMixin, TextTableFormatter):
    pass




def create_formatter(type, upper_headers=None, col_format=None):
    match type:
        case 'html':
            form = HTMLTableFormatter
        case 'csv':
            form = CSVTableFormatter
        case 'text':
            form = TextTableFormatter
        case _:
            raise ValueError(f'Unknown formation {type}')
        
    if col_format:
        class form(ColumnFormatMixin, form):
            formats = col_format

    if upper_headers:
        class form(UpperHeadersMixin, form):
            pass 

    return form()

    
        

if __name__ == '__main__':
    import stock, reader
    portfolio = reader.read_csv_as_instances('../../Data/portfolio.csv',stock.Stock)
    
    print_table(portfolio, ['name','shares','price'], PortfolioColFormatter())
    print('\n\n')
    print_table(portfolio, ['name','shares','price'], PortfolioHeadFormatter())
    print('\n\n')
    print_table(portfolio, ['name','shares','price'], create_formatter('text', upper_headers=True, col_format=['%s', '%d', '%0.2f']))
