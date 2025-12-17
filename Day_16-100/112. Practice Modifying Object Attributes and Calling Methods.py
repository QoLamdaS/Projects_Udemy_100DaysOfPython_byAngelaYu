
from prettytable import PrettyTable
table = PrettyTable()
table.add_column('Name', ['Jade', 'John', 'Jane'])
table.add_column('Age', [20, 30, 40])
table.add_column('Results', [9.651, 3, 245.7])
print(table)