print('''CPF Cash Top-Up Relief allows you to claim tax relief for topping up your own CPF Special/Retirement Account
or those of your family members to meet basic retirement needs

IMPORTANT: You do not need to claim the tax relief personally, it is granted automatically be IRAS based on records by CPF Board


Qualifying Conditions:
1) Be a Singaporean Citizen OR a Singaporean Permanent Resident
2) Have made cash top-ups in the previous year under CPF Retirement Sum Topping-Up Scheme(RSTU)
3) Payment must be in the form of cash top-ups
4) Cash top-ups can be made to the following:
   - Self Special Account for those below 55 years old
   - Self Retirement Account for those 55 years old and above
   - Parent/Parent's-in-law
   - Grandparents/Grandparents-in-law
   - Handicapped Spouse
   - Handicapped Siblings
   - Spouse with annual income of less than or equals to 4000 preceding year of top-up (2 years before current Year of Assessment)
   - Siblings with annual income of less than or equals to 4000 preceding year of top-up (2 years before current Year of Assessment)

Rules:
- Not allowed if recepient is a self-employed person with outstanding Medisave liabilities
- Maximum CPF Cash Top-up Relief per a person can claim Year of Assessment is $16,000 ($8,000 for self, $8,000 for family members)
- Personal income tax relief capped at $80,000 (applies to total amount of ALL tax reliefs made)
- Multiple siblings can claim for the same family member provided that they topped up with their own money

Payout (WILL BE CLAIMED AUTOMATICALLY IF ELIGIBLE):

Amount of cash top-up                       Maximum top-up relief

Below $8,000                                Exact amount of cash top-up
$8,000 or more                              $8000 per individual taxpayer

''')


commentary = print('''Welcome to the CPF Cash Top-Up Relief Calculator!
REMINDER: You can claim up to $16,000 in CPF Cash Top-up Reliefs, $8,000 for you, $8,000 for family members
REMINDER: You do not need to claim the amount yourself, it will be handled by the IRAS via CPF Board
REMINDER: ALL CALCULATIONS ARE TO BE IN THE PREVIOUS YEAR (2023)
''')






person_left = True
total_relief = 0
while person_left == True:

    age = int(input('Enter your age last year:\n '))

    if age < 55:
        # Calculate Medisave Relief user is eligible for and compare it with the amount user topped up
        mas = int(input('Enter the amount in the Medisave Account Savings($) for the previous year before the topup:\n'))
        mas_topup = int(input('Type the total amount you top-up to the Medisave Account Savings($):\n'))
        #BHS = 71500
        mas_topup_allowed = 71500 - mas
        med_actual = 0
        if mas_topup_allowed <= 0:
            med_actual = 0
        elif mas_topup_allowed > 0 and mas_topup >= 8000:
            med_actual = 8000
        elif mas_topup_allowed > 0 and mas_topup < 8000:
            med_actual = mas_topup


        #Calculate Account Relief user is eligible for and compare it with the actual amount user topped up
        sas = int(input('Enter your Special Account Savings($):\n'))
        sas_withdrawn = int(input('Type the total amount that was withdrew from the Special Account for investing($) for the previous year, (type 0 if you have already deducted it yourself):\n'))
        own_topups = int(input('Enter the total amount you topped-up via cash to the Special account($) for the previous year:\n'))
        sas_left = sas - sas_withdrawn
        #RE = 205800
        relief_eligible = 205800 - sas_left
        if relief_eligible <= 0:
            relief_eligible = 0
        else:
            relief_eligible = relief_eligible
        total_cpf_topup_allowed = mas_topup_allowed + relief_eligible
        own_topups = own_topups + med_actual
        own_topup = 0

        #Compare between total amount user topped up and total amount user is eligible for
        if own_topups <= total_cpf_topup_allowed and own_topups < 8000:
            own_topup = own_topups
            print(f'The person can claim ${own_topup} in CPF Cash Top-up Relief!')
        elif own_topups <= total_cpf_topup_allowed and own_topups > 8000:
            own_topup = 8000
            print(f'The person can claim ${own_topup} in CPF Cash Top-up Relief!')
        elif own_topups > total_cpf_topup_allowed and own_topups < 8000:
            own_topup = total_cpf_topup_allowed
            print(f'The person can claim ${own_topup} in CPF Cash Top-up Relief!')
        elif own_topups > total_cpf_topup_allowed and own_topups >= 8000:
            own_topup = 8000
            print(f'The person can claim ${own_topup} in CPF Cash Top-up Relief!')

        total_relief += own_topup
        if total_relief >= 16000:
            total_relief = 16000
            print(f'You have reached the maximum amount of CPF Cash Top-Up Relief you can claim, $16000')
        anymore = input('Do you want to continue? Enter Y for yes, N for no: ')

        if anymore.capitalize() == 'Y':
            person_left = True
        else:
            person_left = False


    elif age >= 55 and age < 65:
        # Calculate Medisave Relief user is eligible for and compare it with the amount user topped up
        mas = int(input('Enter the amount in the Medisave Account Savings($) for the previous year before the topup:\n'))
        mas_topup = int(input('Type the total amount you top-up to the Medisave Account Savings($):\n'))
        mas_topup_allowed = 71500 - mas
        med_actual = 0
        if mas_topup_allowed <= 0:
            med_actual = 0
        elif mas_topup_allowed > 0 and mas_topup >= 8000:
            med_actual = 8000
        elif mas_topup_allowed > 0 and mas_topup < 8000:
            med_actual = mas_topup


        #Calculate the amount of Cash Top-Up allowed to be made in the previous year, as well as amount of CPF Top-Up Relief eligible to the user
        ers = 319500
        frs = 205800
        ras = int(input('Enter the amount in your Retirement Account Savings for the previous year'))
        own_topups= int(input('Enter the amount of Cash top-up you made for the Retirement Account Savings for the previous year'))
        topup_eligible = ers - ras
        if topup_eligible <= 0:
            topup_eligible = 0
        elif topup_eligible > 0:
            topup_eligible = topup_eligible

        if topup_eligible >= own_topups and own_topups >= 8000:
            topup_actual = 8000
            print(f'You can top-up ${own_topups} on the Retirement Account Savings Account')
        elif topup_eligible >= own_topups and own_topups < 8000:
            topup_actual = own_topups
            print(f'You can top-up ${own_topups} on the Retirement Account Savings Account')
        elif topup_eligible < own_topups:
            topup_actual = topup_eligible
            print(f'You can top-up ${own_topups} on the Retirement Account Savings Account this year ')

        own_topup = med_actual + topup_actual


        relief_eligible = frs - ras

        if relief_eligible <= 0:
            relief_eligible = 0
        elif relief_eligible > 0:
            relief_eligible = relief_eligible


        #Compare between amount of Cash Top-Up made to the CPF Relief eligible
        if relief_eligible < 8000:
            if own_topup >= relief_eligible and own_topup >= 8000:
                own_topup = relief_eligible
                print(f'The person is eligible to ${own_topup} of CPF Cash Top-Up Relief!a')
            elif own_topup < relief_eligible and own_topup < 8000:
                print(f'The person is eligible to ${own_topup} of CPF Cash Top-Up Relief!b')

            elif own_topup < relief_eligible and own_topup >= 8000:
                own_topup = 8000
                print(f'The person is eligible for ${own_topup} of CPF Cash Top-Up Relief!c')
            elif own_topup >= relief_eligible and own_topup < 8000:
                own_topup = relief_eligible
                print(f'The person is eligible for ${own_topup} of CPF Cash Top Up Relief!d')

        elif relief_eligible >= 8000:
            if own_topup >= relief_eligible:
                own_topup = 8000
                print(f'The person is eligible to ${own_topup} of CPF Cash Top-Up Relief!e')
            elif own_topup < relief_eligible and own_topup < 8000:
                print(f'The person is eligible to ${own_topup} of CPF Cash Top-Up Relief!f')
            elif own_topup < relief_eligible and own_topup >= 8000:
                own_topup = 8000
                print(f'The person is eligible to ${own_topup} of CPF Cash Top-Up Relief!')


        total_relief += own_topup
        if total_relief >= 16000:
            total_relief = 16000
            print(f'You have reached the maximum amount of CPF Cash Top-Up Relief you can claim, $16000')
        anymore = input('Do you want to continue? Enter Y for yes, N for no: ')

        if anymore.capitalize() == 'Y':
            person_left = True
        else:
            person_left = False









    elif age >= 65:
        # Calculate Medisave Relief user is eligible for and compare it with the amount user topped up
        basic_healthcare_sum = int(input('Enter the Basic Healthcare Sum for the individual\'s age cohort'))
        mas = int(input('Enter the amount in the Medisave Account Savings($) for the previous year before the topup:\n'))
        mas_topup = int(input('Type the total amount you top-up to the Medisave Account Savings($):\n'))
        mas_topup_allowed = basic_healthcare_sum - mas
        med_actual = 0
        if mas_topup_allowed <= 0:
            med_actual = 0
        elif mas_topup_allowed > 0 and mas_topup >= 8000:
            med_actual = 8000
        elif mas_topup_allowed > 0 and mas_topup < 8000:
            med_actual = mas_topup

        # Calculate the amount of Cash Top-Up allowed to be made in the previous year, as well as amount of CPF Top-Up Relief eligible to the user
        ers = 319500
        frs = 205800
        ras = int(input('Enter the amount in your Retirement Account Savings for the previous year'))
        own_topups = int(input('Enter the amount of Cash top-up you made for the Retirement Account Savings for the previous year'))
        topup_eligible = ers - ras
        topup_actual = 0
        if topup_eligible <= 0:
            topup_eligible = 0
        elif topup_eligible > 0:
            topup_eligible = topup_eligible

        if topup_eligible >= own_topups and own_topups >= 8000:
            topup_actual = 8000
            print(f'You can top-up ${own_topups} on the Retirement Account Savings Account')
        elif topup_eligible >= own_topups and own_topups < 8000:
            topup_actual = own_topups
            print(f'You can top-up ${own_topups} on the Retirement Account Savings Account')
        elif topup_eligible < own_topups:
            topup_actual = topup_eligible
            print(f'You can top-up ${own_topups} on the Retirement Account Savings Account this year ')

        own_topup = med_actual + topup_actual

        relief_eligible = frs - ras

        if relief_eligible <= 0:
            relief_eligible = 0
        elif relief_eligible > 0:
            relief_eligible = relief_eligible

        # Compare between amount of Cash Top-Up made to the CPF Relief eligible
        if relief_eligible < 8000:
            if own_topup >= relief_eligible and own_topup >= 8000:
                own_topup = relief_eligible
                print(f'The person is eligible to ${own_topup} of CPF Cash Top-Up Relief!a')
            elif own_topup < relief_eligible and own_topup < 8000:
                print(f'The person is eligible to ${own_topup} of CPF Cash Top-Up Relief!b')

            elif own_topup < relief_eligible and own_topup >= 8000:
                print(f'The person is eligible for ${own_topup} of CPF Cash Top-Up Relief!c')
            elif own_topup >= relief_eligible and own_topup < 8000:
                own_topup = relief_eligible
                print(f'The person is eligible for ${own_topup} of CPF Cash Top Up Relief!d')

        elif relief_eligible >= 8000:
            if own_topup >= relief_eligible:
                own_topup = 8000
                print(f'The person is eligible to ${own_topup} of CPF Cash Top-Up Relief!e')
            elif own_topup < relief_eligible and own_topup < 8000:
                print(f'The person is eligible to ${own_topup} of CPF Cash Top-Up Relief!f')
            elif own_topup < relief_eligible and own_topup >= 8000:
                own_topup = 8000
                print(f'The person is eligible to ${own_topup} of CPF Cash Top-Up Relief!')


        total_relief += own_topup
        if total_relief >= 16000:
            total_relief = 16000
            print(f'You have reached the maximum amount of CPF Cash Top-Up Relief you can claim, $16000')
        anymore = input('Do you want to continue? Enter Y for yes, N for no: ')
        if anymore.capitalize() == 'Y':
            person_left = True
        else:
            person_left = False
















