x = '''Working Mother's Child Relief (WMCR) is given to 
1) Encourage married women to remain in the workforce after having children
2) Encourage parents to take up Singapore Citizenship for their children
3) Reward families with children who are Singaporean Citizens


Qualifying Conditions(For the year prior to the Year of Assessment)
1) You are a working mother who is married, divorced or widowed
2) You have taxable earned income from employment or through pensions, trade or business, or through a profession
   or vocation (taxable earned income = total earned income - allowable expenses)
3) You have maintained a child who is a Singaporean Citizen as at 31 Dec of the year prior
   and has satisfied all the conditions under Qualifying Child Relief as well as the Handicapped Child Relief


Rules
1) You may claim WMCR in your tax filing for Year of Assessment even if your child has passed away the year prior
2) The amount of relief varies for each child based on the child order of the family unit,
    which is determined via the date of marriage, birth certificate or date of legal adoption
3) A deceased or stillborn child is counted in determining order of the children
4) You may claim WMCR even if you and/or your husband or ex-husband has already claimed Qualifying Child Relief/ Handicapped Child Relief
   on the same child
    - QCR/HCR Claims will be allowed first
    - Total cap of QCR/HCR + WMCR is $50,000 per child
    - WMCR is limited to remaining balance after the QCR/HCR claim is allowed
5) WMCR percentages are added together for multiple children and the total is capped at 100% of mother's earned income
6) Personal income tax relief cap of $80,000 applies to total amount of all tax reliefs allowed

Relief Eligible

             Child Order                               WMCR Amount
               1st                                     15% of mother's earned income
               2nd                                     20% of mother's earned income
               3rd and beyond                          25% of mother's earned income
 '''

print(''' __       __            __                                              __  __  __ 
|  \\  _  |  \\          |  \\                                            |  \\|  \\|  \\
| $$ / \\ | $$  ______  | $$  _______   ______   ______ ____    ______  | $$| $$| $$
| $$/  $\\| $$ /      \\ | $$ /       \\ /      \\ |      \\    \\  /      \\ | $$| $$| $$
| $$  $$$\\ $$|  $$$$$$\\| $$|  $$$$$$$|  $$$$$$\\| $$$$$$\\$$$$\\|  $$$$$$\\| $$| $$| $$
| $$ $$\\$$\\$$| $$    $$| $$| $$      | $$  | $$| $$ | $$ | $$| $$    $$ \\$$ \\$$ \\$$
| $$$$  \\$$$$| $$$$$$$$| $$| $$_____ | $$__/ $$| $$ | $$ | $$| $$$$$$$$ __  __  __ 
| $$$    \\$$$ \\$$     \\| $$ \\$$     \\ \\$$    $$| $$ | $$ | $$ \\$$     \\|  \\|  \\|  \\
 \\$$      \\$$  \\$$$$$$$ \\$$  \\$$$$$$$  \\$$$$$$  \\$$  \\$$  \\$$  \\$$$$$$$ \\$$ \\$$ \\$$

                                                                             ''')




#Start of questions


print('''Welcome to the Working Mother's Child Relief Eligibility Test!
The following questions will determine whether you child is eligible for the tax relief, 
as well as the sum of the tax relief he/she can claim.
(IMPORTANT: You may claim WMCR for the current Year Of Assessment even if your child has passed away the year prior)
For the following questions, if not stated otherwise, please enter 'y' for Yes, and enter 'n' for No.\n''')

decision1 = input('''Do you want to see the summarized description of the Working Mother's Child Relief?\n''')
if decision1.lower == 'y':
    print('x')
while True:
    try:
        q1 = input("Were you a working mother who was married, divorced or widowed in the year prior?\n")
        if q1.lower() == 'y':
            q2 = input('''Did you have a taxable earned income from employment or through pensions, trade or business, 
or through a vocation?\n''')
            if q2.lower() == 'y':
                annual_taxable_income = int(input('How much taxable income did you earn for the whole year prior?\n'))
                print('Please enter valid numbers!')
                q3 = input('''Did you maintain a child who is a Singaporean Citizens as at the year prior and has satisfied ALL the following conditions:
EITHER (For Non-Handicapped Children)
- Your child was either born to you and your spouse/ex-spouse, or a step-child, or your child was legally adopted
- Your child was either below 16 year old or studying full time at any educational institution at any time of the year
- Your child did not have an annual allowance exceeding $4,000
- Your child is unmarried
        
OR (For Handicapped Children)
- Your child was either born to you and your ex-spouse, or your child is a step-child, or your child was legally adopted
- Your child was physically or mentally handicapped?\n''')
                if q3.lower() == 'y':
                    q4 = int(input('Please enter the number of children that is eligible for this child relief\n(ENTER A WHOLE NUMBER)'))
                    total_relief = 0

                    while q4 > 0:
                        if q4 >= 3:
                            q5 = input(
                                'Is your child physically or mentally handicapped, and qualify for the Handicapped Child Relief?\n')
                            if q5.lower() == 'y':
                                print('You are eligible for $7,500 of Handicapped Child Relief!')
                                WMCR = (25 / 100) * annual_taxable_income
                                HCR_WMCR = 7500 + WMCR
                                HCR_WMCR = round(HCR_WMCR, 2)
                                if HCR_WMCR < 50000:
                                    total_relief += HCR_WMCR
                                    print(f'You can claim {HCR_WMCR} for your Child number {q4}!')
                                    q4 -= 1
                                elif HCR_WMCR >= 50000:
                                    total_relief += 50000
                                    print(f'You can claim $50,000 for your Child number {q4}!')
                                    q4 -= 1

                            elif q5.lower() == 'n':
                                q6 = input('Is your child non-handicapped and qualify for the Qualifying Child Relief?\n')
                                if q6.lower() == 'y':
                                    print('Your child is eligible for $4,000 of Qualifying Child Relief!')
                                    WMCR = (25 / 100) * annual_taxable_income
                                    QCR_WMCR = 4000 + WMCR
                                    QCR_WMCR = round(QCR_WMCR, 2)
                                    if QCR_WMCR < 50000:
                                        total_relief += QCR_WMCR
                                        print(f'You can claim {QCR_WMCR} for your Child number {q4}!')
                                        q4 -= 1
                                    elif QCR_WMCR >= 50000:
                                        total_relief += 50000
                                        print(f'You can claim $50,000 for your Child number {q4}!')
                                        q4 -= 1
                                elif q6.lower() == 'n':
                                    print('Sorry! Your child is not eligible for any of the Child Reliefs.')
                                else:
                                    print('Please Enter Y/N to indicate your choice')
                                    continue
                            else:
                                print('Please Enter Y/N to indicate your choice')
                                continue

                        elif q4 == 2:
                            q5 = input('Is your child physically or mentally handicapped, and qualify for the Handicapped Child Relief?\n')
                            if q5.lower() == 'y':
                                print('You are eligible for $7,500 of Handicapped Child Relief!')
                                WMCR = (20 / 100) * annual_taxable_income
                                HCR_WMCR = 7500 + WMCR
                                HCR_WMCR = round(HCR_WMCR, 2)
                                if HCR_WMCR < 50000:
                                    total_relief += HCR_WMCR
                                    print(f'You can claim {HCR_WMCR} for your Child number {q4}!')
                                    q4 -= 1
                                elif HCR_WMCR >= 50000:
                                    total_relief += 50000
                                    print(f'You can claim $50,000 for your Child number {q4}!')
                                    q4 -= 1
                            elif q5.lower() == 'n':
                                q6 = input('Is your child non-handicapped and qualify for the Qualifying Child Relief?\n')
                                if q6.lower() == 'y':
                                    print('Your child is eligible for $4,000 of Qualifying Child Relief!')
                                    WMCR = (20 / 100) * annual_taxable_income
                                    QCR_WMCR = 4000 + WMCR
                                    QCR_WMCR = round(QCR_WMCR, 2)
                                    if QCR_WMCR < 50000:
                                        total_relief += QCR_WMCR
                                        print(f'You can claim {QCR_WMCR} for your Child number {q4}!')
                                        q4 -= 1
                                    elif QCR_WMCR >= 50000:
                                        total_relief += 50000
                                        print(f'You can claim $50,000 for your Child number {q4}!')
                                        q4 -= 1
                                elif q6.lower() == 'n':
                                    print('Sorry! Your child is not eligible for any of the Child Reliefs.')
                                else:
                                    print('Please enter Y/N to indicate your choice.')
                                    continue
                            else:
                                print('Please enter Y/N to indicate your choice.')
                                continue

                        elif q4 == 1:
                            q5 = input('Is your child physically or mentally handicapped, and qualify for the Handicapped Child Relief?\n')
                            if q5.lower() == 'y':
                                print('You are eligible for $7,500 of Handicapped Child Relief!')
                                WMCR = (15/100) * annual_taxable_income
                                HCR_WMCR = 7500 + WMCR
                                HCR_WMCR = round(HCR_WMCR,2)
                                if HCR_WMCR < 50000:
                                    total_relief += HCR_WMCR
                                    print(f'You can claim {HCR_WMCR} for your Child number {q4}!')
                                    q4 -= 1
                                elif HCR_WMCR >= 50000:
                                    total_relief += 50000
                                    print(f'You can claim $50,000 for your Child number {q4}!')
                                    q4 -= 1

                            elif q5.lower() == 'n':
                                q6 = input('Is your child non-handicapped and qualify for the Qualifying Child Relief?\n')
                                if q6.lower()== 'y':
                                    print('Your child is eligible for $4,000 of Qualifying Child Relief!')
                                    WMCR = (15 / 100) * annual_taxable_income
                                    QCR_WMCR = 4000 + WMCR
                                    QCR_WMCR = round(QCR_WMCR, 2)
                                    if QCR_WMCR < 50000:
                                        total_relief += QCR_WMCR
                                        print(f'You can claim {QCR_WMCR} for your Child number {q4}!')
                                        q4 -= 1
                                    elif QCR_WMCR >= 50000:
                                        total_relief += 50000
                                        print(f'You can claim $50,000 for your Child number {q4}!')
                                        q4 -= 1
                                elif q6.lower() == 'n':
                                    print('Sorry! Your child is not eligible for any of the Child Reliefs.')
                                else:
                                    print('Please enter Y/N to indicate your choice.')
                                    continue
                            else:
                                print('Please enter Y/N to indicate your choice')
                                continue

                    else:
                        if total_relief < 80000:
                            print(f'You can claim a total of ${total_relief} of Child Reliefs!')
                        elif total_relief >= 80000:
                            print(f'You can claim a total of $80000 of Child Reliefs! (Maximum Personal Tax Relief allowed)')

                elif q3.lower() == 'n':
                    print('Sorry! Your child is not eligible for any of the Child Reliefs.')
                else:
                    print('Please enter Y/N to indicate your choice.')
                    continue

            elif q2.lower() == 'n':
                print('Sorry! Your child is not eligible for any of the Child Reliefs.')
            else:
                print('Please enter Y/N to indicate your choice.')
                continue

        elif q1.lower() == 'n':
            print('Sorry! Your child is not eligible for any of the Child Reliefs.')
        else:
            print('Please enter Y/N to indicate your choice.')
            continue

    except ValueError:
        print('Please enter valid number(s).')
        continue
    else:
        break