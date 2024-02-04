print('''Earned Income Relief is for individuals who are gainfully employed or carrying on a trade, business, profession or vocation.

Qualifying Conditions:
- You must have taxable earned income from any of the following sources:
   1) Employment
   2) Pension
   3) Trade, Business, Profession or Vocation

Rules:
- If amount of taxable earned income is lower than maximum amount claimable,
  relief will be capped at the amount of taxable earned income
- Do not need to claim Earned Income Relief in your Income Tax Return as it will be
  automatically granted to you based on your eligibility
- Personal income tax relief capped at $80,000

Relief Eligible:
                                    Non-Handicapped Individual
        Age as of 31 Dec the previous year                      Maximum amount claimable
                   Below 55                                             $1,000
                   55 to 59                                             $6,000
                   60 and above                                         $8,000



                                    Handicapped Individual
        Age as of 31 Dec the previous year                       Maximum amount claimable
                   Below 55                                             $4,000
                   55 to 59                                             $10,000
                   60 and above                                         $12,000
''')

print(
    "The following questions are to test your eligibility for the taxable earned income relief.\n Enter 'y' for Yes, and 'n' for No")

q1 = input('''Do you have taxable earned income from any of the following sources:
- Employment
- Pension
- Trade, Business, Profession, Vocation''')
if q1.capitalize() == 'Y':
    q2 = input('Are you handicapped physically or mentally?')
    if q2.capitalize() == 'Y':
        q3 = int(input('Enter you age as of 31 Dec the previous year:\n'))
        if q3 < 55:
            print('You are eligible for a MAXIMUM of $4,000 of Taxable Earned Income Relief!')
            income_earned = int(input('Enter your total taxable earned income in the previous year:\n'))
            if income_earned >= 4000:
                print('You can claim $4,000 of Taxable Earned Income Relief!')
            elif income_earned < 4000:
                print(f'You can claim ${income_earned} of Taxable Earned Income Relief!')
        elif 55 <= q3 <= 59:
            print('You are eligible for a MAXIMUM of $10,000 of Taxable Earned Income Relief!')
            income_earned = int(input('Enter your total taxable earned income in the previous year:\n'))
            if income_earned >= 10000:
                print('You can claim $10,000 of Taxable Earned Income Relief!')
            elif income_earned < 10000:
                print(f'You can claim ${income_earned} of Taxable Earned Income Relief!')
        elif q3 >= 60:
            print('You are eligible for a MAXIMUM of $12,000 of Taxable Earned Income Relief!')
            income_earned = int(input('Enter your total taxable earned income in the previous year:\n'))
            if income_earned >= 12000:
                print('You can claim $12,000 of Taxable Earned Income Relief!')
            elif income_earned < 12000:
                print(f'You can claim ${income_earned} of Taxable Earned Income Relief!')
    elif q2.capitalize() == 'N':
        q3 = int(input('Enter you age as of 31 Dec the previous year:\n'))
        if q3 < 55:
            print('You are eligible for a MAXIMUM of $1,000 of Taxable Earned Income Relief!')
            income_earned = int(input('Enter your total taxable earned income in the previous year:\n'))
            if income_earned >= 1000:
                print('You are eligible for $1,000 of Taxable Earned Income Relief!')
            elif income_earned < 1000:
                print(f'You are eligible for ${income_earned} of Taxable Earned Income Relief!')
        elif 55 <= q3 <= 59:
            print('You are eligible for a MAXIMUM of $6,000 of Taxable Earned Income Relief!')
            income_earned = int(input('Enter your total taxable earned income in the previous year:\n'))
            if income_earned >= 6000:
                print('You can claim $6,000 of Taxable Earned Income Relief!')
            elif income_earned < 6000:
                print(f'You can claim ${income_earned} of Taxable Earned Income Relief!')
        elif q3 >= 60:
            print('You are eligible for a MAXIMUM of $8,000 of Taxable Earned Income Relief!')
            income_earned = int(input('Enter your total taxable earned income in the previous year:\n'))
            if income_earned >= 8000:
                print('You can claim $8,000 of Taxable Earned Income Relief!')
            elif income_earned < 8000:
                print(f'You can claim ${income_earned} of Taxable Earned Income Relief!')


elif q1.capitalize() == 'N':
    print('You are not eligible for any Earned Income Tax Relief.')