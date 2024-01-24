
#CPF Relief calculator without Functions
print('This is the CPF Relief Calculator for YOA 2025')
CPF_RELIEF = 0
ordinary_wage_ceiling = int(6800)
age = int(input('Enter your age: '))
monthly_salary = int(input('Please enter your monthly_salary as a whole number'))
medisave_contribution = int(input('Please enter any voluntary cash contribution you made to your Medisave Account.\n If no contributions are made, enter "0"'))



#If the user's monthly salary exceeds the monthly salary cap, use the monthly salary cap as the input for total wage
if monthly_salary > ordinary_wage_ceiling :
    ordinary_wage = 6800 * 12
    additional_wage_ceiling = 102000 - ordinary_wage
    extra_wages = float(input('Please enter any additional wages you received in the year 2024. (E.G. Annual Bonus)'))
    if extra_wages > additional_wage_ceiling:
        additional_wage = additional_wage_ceiling
        total_wage = ordinary_wage + additional_wage
        print(f'Your Ordinary Wage is {ordinary_wage}')
        print(f'Your Additional Wage is {additional_wage}')
        print(f'Your total wage is ${total_wage}')

        #age bracket 1
        if age <= 55:
            employer_cpf = total_wage * (17/100)
            employee_cpf = total_wage * (20/100)
            total_cpf = total_wage * (37/100)
            print(f'Your CPF contribution is ${employee_cpf}, your employer contributed ${employer_cpf}.\n Total CPF contribution is ${total_cpf}')

            #Check whichever is lower, max tax relief or voluntary cash contribution to Medisave and calculate total CPF relief available
            max_taxrelief = 37740 - total_cpf
            if max_taxrelief < medisave_contribution:
                total_cpf_relief = employee_cpf + max_taxrelief
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')
            else:
                total_cpf_relief = employee_cpf + medisave_contribution
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')




        elif 55 < age <= 60:
            employer_cpf = total_wage * (15/100)
            employee_cpf = total_wage * (16/100)
            total_cpf = total_wage * (31/100)
            print(f'Your CPF contribution is ${employee_cpf}, your employer contributed ${employer_cpf}.\n Total CPF contribution is ${total_cpf}')
            #Check whichever is lower, max tax relief or voluntary cash contribution to Medisave and calculate total CPF relief available
            max_taxrelief = 37740 - total_cpf
            if max_taxrelief < medisave_contribution:
                total_cpf_relief = employee_cpf + max_taxrelief
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')
            else:
                total_cpf_relief = employee_cpf + medisave_contribution
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')

        elif 60 < age <= 65:
            employer_cpf = total_wage * (11.5/100)
            employee_cpf = total_wage * (10.5/100)
            total_cpf = total_wage * (22/100)
            print(f'your CPF contribution is ${employee_cpf}, your employer contributed ${employer_cpf}.\n Total CPF contribution is ${total_cpf}')
            #Check whichever is lower, max tax relief or voluntary cash contribution to Medisave and calculate total CPF relief available
            max_taxrelief = 37740 - total_cpf
            if max_taxrelief < medisave_contribution:
                total_cpf_relief = employee_cpf + max_taxrelief
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')
            else:
                total_cpf_relief = employee_cpf + medisave_contribution
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')

        elif 65 < age <= 70:
            employer_cpf = total_wage * (9/100)
            employee_cpf = total_wage * (7.5/100)
            total_cpf = total_wage * (16.5/100)
            print(f'Your CPF contribution is ${employee_cpf}, your employer contributed ${employer_cpf}.\n Total CPF contribution is ${total_cpf}')
            #Check whichever is lower, max tax relief or voluntary cash contribution to Medisave and calculate total CPF relief available
            max_taxrelief = 37740 - total_cpf
            if max_taxrelief < medisave_contribution:
                total_cpf_relief = employee_cpf + max_taxrelief
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')
            else:
                total_cpf_relief = employee_cpf + medisave_contribution
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')

        elif age > 70:
            employer_cpf = total_wage * (7.5/100)
            employee_cpf = total_wage * (5/100)
            total_cpf = total_wage * (12.5/100)
            print(f'Your CPF contribution is ${employee_cpf}, your employer contributed ${employer_cpf}.\n Total CPF contribution is ${total_cpf}')
            #Check whichever is lower, max tax relief or voluntary cash contribution to Medisave and calculate total CPF relief available
            max_taxrelief = 37740 - total_cpf
            if max_taxrelief < medisave_contribution:
                total_cpf_relief = employee_cpf + max_taxrelief
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')
            else:
                total_cpf_relief = employee_cpf + medisave_contribution
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')



#if additional wages is below the additional wage ceiling
    else:
        additional_wage = extra_wages
        total_wage = ordinary_wage + additional_wage
        print(f'Your Ordinary Wage is {ordinary_wage}')
        print(f'Your Additional Wage is {additional_wage}')
        print(f'Your total wage is ${total_wage}')
        if age <= 55:
            employer_cpf = total_wage * (17/100)
            employee_cpf = total_wage * (20/100)
            total_cpf = total_wage * (37/100)
            print(f'Your CPF contribution is ${employee_cpf}, your employer contributed ${employer_cpf}.\n Total CPF contribution is ${total_cpf}')
            #Check whichever is lower, max tax relief or voluntary cash contribution to Medisave and calculate total CPF relief available
            max_taxrelief = 37740 - total_cpf
            if max_taxrelief < medisave_contribution:
                total_cpf_relief = employee_cpf + max_taxrelief
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')
            else:
                total_cpf_relief = employee_cpf + medisave_contribution
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')

        elif 55 < age <= 60:
            employer_cpf = total_wage * (15 / 100)
            employee_cpf = total_wage * (16 / 100)
            total_cpf = total_wage * (31 / 100)
            print(f'Your CPF contribution is ${employee_cpf}, your employer contributed ${employer_cpf}.\n Total CPF contribution is ${total_cpf}')
            #Check whichever is lower, max tax relief or voluntary cash contribution to Medisave and calculate total CPF relief available
            max_taxrelief = 37740 - total_cpf
            if max_taxrelief < medisave_contribution:
                total_cpf_relief = employee_cpf + max_taxrelief
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')
            else:
                total_cpf_relief = employee_cpf + medisave_contribution
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')

        elif 60 < age <= 65:
            employer_cpf = total_wage * (11.5 / 100)
            employee_cpf = total_wage * (10.5 / 100)
            total_cpf = total_wage * (22 / 100)
            print(f'your CPF contribution is ${employee_cpf}, your employer contributed ${employer_cpf}.\n Total CPF contribution is ${total_cpf}')
            #Check whichever is lower, max tax relief or voluntary cash contribution to Medisave and calculate total CPF relief available
            max_taxrelief = 37740 - total_cpf
            if max_taxrelief < medisave_contribution:
                total_cpf_relief = employee_cpf + max_taxrelief
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')
            else:
                total_cpf_relief = employee_cpf + medisave_contribution
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')
        elif 65 < age <= 70:
            employer_cpf = total_wage * (9 / 100)
            employee_cpf = total_wage * (7.5 / 100)
            total_cpf = total_wage * (16.5 / 100)
            print(f'Your CPF contribution is ${employee_cpf}, your employer contributed ${employer_cpf}.\n Total CPF contribution is ${total_cpf}')
            #Check whichever is lower, max tax relief or voluntary cash contribution to Medisave and calculate total CPF relief available
            max_taxrelief = 37740 - total_cpf
            if max_taxrelief < medisave_contribution:
                total_cpf_relief = employee_cpf + max_taxrelief
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')
            else:
                total_cpf_relief = employee_cpf + medisave_contribution
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')
        elif age > 70:
            employer_cpf = total_wage * (7.5 / 100)
            employee_cpf = total_wage * (5 / 100)
            total_cpf = total_wage * (12.5 / 100)
            print(f'Your CPF contribution is ${employee_cpf}, your employer contributed ${employer_cpf}.\n Total CPF contribution is ${total_cpf}')
            #Check whichever is lower, max tax relief or voluntary cash contribution to Medisave and calculate total CPF relief available
            max_taxrelief = 37740 - total_cpf
            if max_taxrelief < medisave_contribution:
                total_cpf_relief = employee_cpf + max_taxrelief
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')
            else:
                total_cpf_relief = employee_cpf + medisave_contribution
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')


#Use user's monthly salary as the input for total wage
elif monthly_salary < ordinary_wage_ceiling:
    ordinary_wage = float(monthly_salary * 12)
    additional_wage_ceiling = 102000 - ordinary_wage
    extra_wages = float(input('Please enter any additional wages you received in the year 2024. (E.G. Annual Bonus)'))

    #if additional wages is above additional wage ceiling
    if extra_wages > additional_wage_ceiling:
        additional_wage = additional_wage_ceiling
        total_wage = ordinary_wage + additional_wage
        print(f'Your Ordinary Wage is {ordinary_wage}')
        print(f'Your Additional Wage is {additional_wage}')
        print(f'Your total wage is ${total_wage}')

        if age <= 55:
            employer_cpf = total_wage * (17/100)
            employee_cpf = total_wage * (20/100)
            total_cpf = total_wage * (37/100)
            print(f'Your CPF contribution is ${employee_cpf}, your employer contributed ${employer_cpf}.\n Total CPF contribution is ${total_cpf}')
            #Check whichever is lower, max tax relief or voluntary cash contribution to Medisave and calculate total CPF relief available
            max_taxrelief = 37740 - total_cpf
            if max_taxrelief < medisave_contribution:
                total_cpf_relief = employee_cpf + max_taxrelief
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')
            else:
                total_cpf_relief = employee_cpf + medisave_contribution
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')

        elif 55 < age <= 60:
            employer_cpf = total_wage * (15 / 100)
            employee_cpf = total_wage * (16 / 100)
            total_cpf = total_wage * (31 / 100)
            print(f'Your CPF contribution is ${employee_cpf}, your employer contributed ${employer_cpf}.\n Total CPF contribution is ${total_cpf}')
            #Check whichever is lower, max tax relief or voluntary cash contribution to Medisave and calculate total CPF relief available
            max_taxrelief = 37740 - total_cpf
            if max_taxrelief < medisave_contribution:
                total_cpf_relief = employee_cpf + max_taxrelief
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')
            else:
                total_cpf_relief = employee_cpf + medisave_contribution
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')
        elif 60 < age <= 65:
            employer_cpf = total_wage * (11.5 / 100)
            employee_cpf = total_wage * (10.5 / 100)
            total_cpf = total_wage * (22 / 100)
            print(f'your CPF contribution is ${employee_cpf}, your employer contributed ${employer_cpf}.\n Total CPF contribution is ${total_cpf}')
            #Check whichever is lower, max tax relief or voluntary cash contribution to Medisave and calculate total CPF relief available
            max_taxrelief = 37740 - total_cpf
            if max_taxrelief < medisave_contribution:
                total_cpf_relief = employee_cpf + max_taxrelief
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')
            else:
                total_cpf_relief = employee_cpf + medisave_contribution
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')
        elif 65 < age <= 70:
            employer_cpf = total_wage * (9 / 100)
            employee_cpf = total_wage * (7.5 / 100)
            total_cpf = total_wage * (16.5 / 100)
            print(f'Your CPF contribution is ${employee_cpf}, your employer contributed ${employer_cpf}.\n Total CPF contribution is ${total_cpf}')
            #Check whichever is lower, max tax relief or voluntary cash contribution to Medisave and calculate total CPF relief available
            max_taxrelief = 37740 - total_cpf
            if max_taxrelief < medisave_contribution:
                total_cpf_relief = employee_cpf + max_taxrelief
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')
            else:
                total_cpf_relief = employee_cpf + medisave_contribution
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')
        elif age > 70:
            employer_cpf = total_wage * (7.5 / 100)
            employee_cpf = total_wage * (5 / 100)
            total_cpf = total_wage * (12.5 / 100)
            print(f'Your CPF contribution is ${employee_cpf}, your employer contributed ${employer_cpf}.\n Total CPF contribution is ${total_cpf}')
            #Check whichever is lower, max tax relief or voluntary cash contribution to Medisave and calculate total CPF relief available
            max_taxrelief = 37740 - total_cpf
            if max_taxrelief < medisave_contribution:
                total_cpf_relief = employee_cpf + max_taxrelief
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')
            else:
                total_cpf_relief = employee_cpf + medisave_contribution
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')

    #if additional wages is below additional wage ceiling
    else:
        additional_wage = extra_wages
        total_wage = ordinary_wage + additional_wage
        print(f'Your Ordinary Wage is {ordinary_wage}')
        print(f'Your Additional Wage is {additional_wage}')
        print(f'Your total wage is ${total_wage}')

        #age bracket
        if age <= 55:
            employer_cpf = total_wage * (17/100)
            employee_cpf = total_wage * (20/100)
            total_cpf = total_wage * (37/100)
            print(f'Your CPF contribution is ${employee_cpf}, your employer contributed ${employer_cpf}.\n Total CPF contribution is ${total_cpf}')
            #Check whichever is lower, max tax relief or voluntary cash contribution to Medisave and calculate total CPF relief available
            max_taxrelief = 37740 - total_cpf
            if max_taxrelief < medisave_contribution:
                total_cpf_relief = employee_cpf + max_taxrelief
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')
            else:
                total_cpf_relief = employee_cpf + medisave_contribution
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')
        #age bracket 2
        elif 55 < age <= 60:
            employer_cpf = total_wage * (15 / 100)
            employee_cpf = total_wage * (16 / 100)
            total_cpf = total_wage * (31 / 100)
            print(f'Your CPF contribution is ${employee_cpf}, your employer contributed ${employer_cpf}.\n Total CPF contribution is ${total_cpf}')
            #Check whichever is lower, max tax relief or voluntary cash contribution to Medisave and calculate total CPF relief available
            max_taxrelief = 37740 - total_cpf
            if max_taxrelief < medisave_contribution:
                total_cpf_relief = employee_cpf + max_taxrelief
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')
            else:
                total_cpf_relief = employee_cpf + medisave_contribution
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')
        #age bracket 3
        elif 60 < age <= 65:
            employer_cpf = total_wage * (11.5 / 100)
            employee_cpf = total_wage * (10.5 / 100)
            total_cpf = total_wage * (22 / 100)
            print(f'your CPF contribution is ${employee_cpf}, your employer contributed ${employer_cpf}.\n Total CPF contribution is ${total_cpf}')
            #Check whichever is lower, max tax relief or voluntary cash contribution to Medisave and calculate total CPF relief available
            max_taxrelief = 37740 - total_cpf
            if max_taxrelief < medisave_contribution:
                total_cpf_relief = employee_cpf + max_taxrelief
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')
            else:
                total_cpf_relief = employee_cpf + medisave_contribution
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')
        #age bracket 4
        elif 65 < age <= 70:
            employer_cpf = total_wage * (9 / 100)
            employee_cpf = total_wage * (7.5 / 100)
            total_cpf = total_wage * (16.5 / 100)
            print(f'Your CPF contribution is ${employee_cpf}, your employer contributed ${employer_cpf}.\n Total CPF contribution is ${total_cpf}')
            #Check whichever is lower, max tax relief or voluntary cash contribution to Medisave and calculate total CPF relief available
            max_taxrelief = 37740 - total_cpf
            if max_taxrelief < medisave_contribution:
                total_cpf_relief = employee_cpf + max_taxrelief
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')
            else:
                total_cpf_relief = employee_cpf + medisave_contribution
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')
        #age bracket 5
        elif age > 70:
            employer_cpf = total_wage * (7.5 / 100)
            employee_cpf = total_wage * (5 / 100)
            total_cpf = total_wage * (12.5 / 100)
            print(f'Your CPF contribution is ${employee_cpf}, your employer contributed ${employer_cpf}.\n Total CPF contribution is ${total_cpf}')
            #Check whichever is lower, max tax relief or voluntary cash contribution to Medisave and calculate total CPF relief available
            max_taxrelief = 37740 - total_cpf
            if max_taxrelief < medisave_contribution:
                total_cpf_relief = employee_cpf + max_taxrelief
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')
            else:
                total_cpf_relief = employee_cpf + medisave_contribution
                print(f'Your maximum CPF Relief is ${total_cpf_relief}')

