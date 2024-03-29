from prettytable import PrettyTable

x = PrettyTable()
x.field_names = ['Chargeable Income', 'Income tax rate(%)', 'Gross tax payable($)']
x.add_row(['First $20,000', 0, 0])
x.add_row(['Next $10,000', 2, 200])
x.add_row(['', '', ''])
x.add_row(['First $30,000', '-', 200])
x.add_row(['Next $10,000', 3.50, 350])
x.add_row(['', '', ''])
x.add_row(['First $40,000', '-', 550])
x.add_row(['Next $40,000', 7, 2800])
x.add_row(['', '', ''])
x.add_row(['First $80,000', '-', 3350])
x.add_row(['Next $40,000', 11.5, 4600])
x.add_row(['', '', ''])
x.add_row(['First $120,000', '-', 7950])
x.add_row(['Next $40,000', 15, 6000])
x.add_row(['', '', ''])
x.add_row(['First $160,000', '-', 13950])
x.add_row(['Next $40,000', 18, 7200])
x.add_row(['', '', ''])
x.add_row(['First $200,000', '-', 21150])
x.add_row(['Next $40,000', 19, 7600])
x.add_row(['', '', ''])
x.add_row(['First $240,000', '-', 28750])
x.add_row(['Next $40,000', 19.5, 7800])
x.add_row(['', '', ''])
x.add_row(['First $280,000', '-', 36550])
x.add_row(['Next $40,000', 20, 8000])
x.add_row(['', '', ''])
x.add_row(['First $320,000', '-', 44550])
x.add_row(['Next $180,000', 22, 39600])
x.add_row(['', '', ''])
x.add_row(['First $500,000', '-', 84150])
x.add_row(['Next $500,000', 23, 115000])
x.add_row(['', '', ''])
x.add_row(['First $1,000,000', '-', 199150])
x.add_row(['In excess of $1,000,000', 24, ''])

print('This is the Progressive Income Tax Bracket for Singapore Tax Residents for the Year of Assessment 2024')
print(x)


