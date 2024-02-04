
import prettytable



print('''
.___                                          ___________                 _________          .__                  .__            __                 
|   |  ____    ____   ____    _____    ____   \\__    ___/_____   ___  ___ \\_   ___ \\ _____   |  |    ____   __ __ |  |  _____  _/  |_  ____ _______ 
|   | /    \\ _/ ___\\ /  _ \\  /     \\ _/ __ \\    |    |   \\__  \\  \\  \\/  / /    \\  \\/ \\__  \\  |  |  _/ ___\\ |  |  \\|  |  \\__  \\ \\   __\\/  _ \\\\_  __ \\
|   ||   |  \\\\  \\___(  <_> )|  Y Y  \\  ___/    |    |    / __ \\_ >    <  \\     \\____ / __ \\_|  |__\\  \\___ |  |  /|  |__ / __ \\_|  | (  <_> )|  | \\/
|___||___|  / \\___  >\\____/ |__|_|  / \\___  >   |____|   (____  //__/\\_ \\  \\______  /(____  /|____/ \\___  >|____/ |____/(____  /|__|  \\____/ |__|   
          \\/      \\/              \\/      \\/                  \\/       \\/         \\/      \\/            \\/                   \\/                     

''')

print('''Welcome to the Income Tax Calculator!
Please answer the following questions via keying in the appropriate values in order to calculate your tax payable for the Year of Assessment 2024.''')


q1 = input('Are you a Singaporean Citizen? Y/N:\n')
if q1.upper() == 'Y':
    q2 = input('Are you an employee of a company? Y/N:\n')
    if q2.upper() == 'Y':


        net_employment_income = float(input('Key in Your Net Employment Income for the year 2023. (Employment Income - Employment Expenses)\n'))
        dividends = float(input('Key in your total dividends earnings for the year 2023.\nIf not applicable, please enter "0"\n'))
        property = float(input('Key in your total property rent earnings for the year 2023.\nIf not applicable, please enter "0"\n'))
        trust = float(input('Key in your total Royalty/Charge/Estate/Trust Income earnings for the Year 2023. \nIf not applicable, please enter "0"\n'))
        other_income = float(input('Key in your total gains/profit of an income nature for the year 2023. \nIf not applicable, please enter "0"\n'))
        donations = float(input('Key in any approved donations you made for the Year 2023. \nIf not applicable, please enter "0"\n'))
        total_income = (net_employment_income + dividends + property + trust + other_income) - donations
        total_income = int(total_income)
        print(f'\n\nYour total income for the Year of Assessment 2024 is {total_income}!\n\n')
        total_taxreliefs = float(input('Enter the total tax reliefs you are eligible for in the Year 2023. \nIf not applicable, please enter "0"\n'))
        chargeableincome = total_income - total_taxreliefs
        chargeableincome = int(chargeableincome)
        print(f'\n\nYour total chargeable income for the Year of Assessment 2024 is {chargeableincome}!\n\n')


        #total income that is subjected to taxes
        income = chargeableincome


        #Income Tax Bracket
        if income < 20000:  # Below 20k
            tax = 0
            print(f'You do not have to pay any Income Tax')
        elif 20000 <= income < 30000:  # 20k - <30k
            tax = (income - 20000) * (2 / 100)
            print(f'You have to pay ${tax:.2f} of Income Tax')
        elif 30000 <= income < 40000:  # 30k - <40k
            tax = (income - 30000) * (3.5 / 100) + 200
            print(f'You have to pay ${tax:2f} of Income Tax')
        elif 40000 <= income < 80000:  # 40k - <80k
            tax = (income - 40000) * (7 / 100) + 550
            print(f'You have to pay ${tax:.2f} of Income Tax')
        elif 80000 <= income < 120000:  # 80k - <120k
            tax = ((income - 80000) * (11.5 / 100)) + 3350
            print(f'You have to pay ${tax:.2f} of Income Tax')
        elif 120000 <= income < 160000:  # 120k - <160k
            tax = ((income - 120000) * (15 / 100)) + 7950
            print(f'You have to pay ${tax:.2f} of Income Tax')
        elif 160000 <= income < 200000:  # 160k - <200k
            tax = ((income - 160000) * (18 / 100)) + 13950
            print(f'you have to pay ${tax:.2f} of Income Tax')
        elif 200000 <= income < 240000:  # 200k - <240k
            tax = ((income - 200000) * (19 / 100)) + 21150
            print(f'You have to pay ${tax:.2f} of Income Tax')
        elif 240000 <= income < 280000:  # 240k - <280k
            tax = ((income - 240000) * (19.5 / 100)) + 28750
            print(f'You have to pay ${tax:.2f} of Income Tax')
        elif 280000 <= income < 320000:  # 280k - <320k
            tax = ((income - 280000) * (20 / 100)) + 36550
            print(f'you have to pay ${tax:.2f} of Income Tax')
        elif 320000 <= income < 500000:  # 320k - <500k
            tax = ((income - 320000) * (22 / 100)) + 44550
            print(f'you have to pay ${tax:.2f} of Income Tax')
        elif 500000 <= income < 1000000:  # 500k - <1mil
            tax = ((income - 500000) * (23 / 100)) + 84150
            print(f'you have to pay ${tax:.2f} of Income Tax')
        elif income >= 1000000:  # >1mil
            no_millions = (income - 1000000) / 1000000
            no_millions = round(no_millions) * 1000000
            tax = 199150 + (no_millions * (24 / 100))
            print(f'you have to pay ${tax:.2f} of Income Tax')

        #parenthood rebate
        parenthood_rebate = float(input('Enter the Parenthood rebate you are eligible for in the Year 2023. \nIf not applicable, please enter "0"\n'))



        #Net Tax Payable AFTER TAX IS DEDUCTED
        nettaxpayable = tax - parenthood_rebate
        nettaxpayable = round(nettaxpayable, 2)
        print(f'\n\nYour net tax payable for the Year of Assessment 2024 is {nettaxpayable:.2f}!')







