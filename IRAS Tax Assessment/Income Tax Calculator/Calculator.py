
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
        chargeable_income = total_income - total_taxreliefs
        chargeable_income = int(chargeable_income)
        print(f'\n\nYour total chargeable income for the Year of Assessment 2024 is {chargeable_income}!\n\n')
        #totaltaxpayable





        parenthood_rebate = float(input('Enter the Parenthood rebate you are eligible for in the Year 2023. \nIf not applicable, please enter "0"\n'))







