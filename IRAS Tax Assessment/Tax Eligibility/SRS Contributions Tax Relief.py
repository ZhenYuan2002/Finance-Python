print('''Welcome to the  Supplementary Retirement Scheme(SRS) Contributions and Tax Relief Calculator!
SRS is a voluntary scheme to encourage individuals to save for retirement, over and above their CPF Savings.
Contributions to SRS are eligible for tax relief. Investment returns are tax-free before withdrawal, and only
50% of the withdrawals from SRS are taxable at retirement.


Conditions for SRS account:
- At least 18 years old
- No undischarged bankruptcy
- No current mental disorders
- Capable of managing yourself and your affairs

Rules for SRS account:
1) Can only have 1 SRS account per person
2) No refunds for SRS contributions made
3) SRS Contribution cannot be made at or after prevailing statutory retirement age when you
   first made your SRS Contribution, or on medical grounds
4) Contributions can be made by your employer on your behalf, though it is subject to taxes and 
   must be declared by your employer on your Form IR8A for relevant Year of Assessment
5) You do not need to make a claim of the Tax Relief, it will be allowed automatically based on information provided by SRS Operator
6) There are NO REFUNDS for any SRS Contributions made
7) Personal Income Tax Relief Cap of $80,000 applies

Payout:
Amount of tax relief = Amount of contributions made by you or your employer(on your behalf), 
Citizens/Permanent Residents can contribute up to $15,300
Foreigners can contribute up to $35,700
''')


contributions_made = int(input('Enter the total contribution to your SRS Account for the year prior to YOA($):\n'))
amount_withdrawn = int(input('Enter the amount withdrawn from your SRS Account for the year prior to YOA($):\n'))
tax_relief = contributions_made - amount_withdrawn
citizenship_status = int(input('''
Enter '1' if you are a Singaporean Citizen
Enter '2' if you are a Permanent Resident of Singapore
Enter '3' if you are a Foreigner\n'''))
if citizenship_status == 1 or citizenship_status == 2:
    if tax_relief < 15300:
        tax_relief = tax_relief
        print(f'You are eligible for ${tax_relief} of SRS Tax Relief!')
    elif tax_relief >= 15300:
        print(f'You are eligible for $15,300 of SRS Tax Relief!')
elif citizenship_status == 3:
    if tax_relief < 35700:
        tax_relief = tax_relief
        print(f'You are eligible for ${tax_relief} of SRS Tax Relief!')
    elif tax_relief >= 35700:
        print(f'You are eligible for $35700 of SRS Tax Relief!')
