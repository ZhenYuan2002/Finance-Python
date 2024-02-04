Life_Insurance_Relief = print('''\n\n\n Life Insurance Relief is given to individuals who paid annual insurance premium on their own life insurance policies.

Qualifying Conditions:
1) Total CPF Contribution for the following was less than $5000 in the year preceding Year Assessment, which includes
    a) Compulsory employee CPF contribution
    b) Compulsory Medisave/Voluntary CPF contribution as an self-employed individual
2) You paid insurance premium on your own Life Insurance Policy
   (If you are a married man, and have paid for your wife's life insurance policy,you may also claim the premiums paid)
3) Insurance company must have an office or branch in Singapore
4) The following insurance policies/riders do not qualify for the Life Insurance Relied:
   - Accident Insurance Policy
   - Hospitalisation Policy
   - Health Insurance Policy such as Medishield, Integrated Shield Plans etc
   - Disability Insurance Policy such as ElderShield, CareShield Life etc
   - Riders under Life Insurance Policy such as total and permanent disability riders, critical illness rider etc
   - Critical Illness Policy
   - Endowment Policy
5) 3) Employee compulsory CPF contribution MUST be less than $5000

Rules:
1) The voluntary cash contribution to your Medisave Account is not considered for the $5,000 limit for the total CPF contribution.

Payout:

Types of contributions         Total amount of contributions                 Amount of Life Insurance Relief allowed

Compulsory Employee CPF             >= 5,000                                              nil
contribution

Self-employed Medisave/             <5,000                                         MAY CLAIM THE LOWER OF:
Voluntary CPF contribution                                                    a) Difference between $5,000 and your CPF Contributions
                                                                              b) Up to 7% of the insured value of your own/ wife's life
                                                                              c) Amount of annual insurance premium paid

''')

print('\n\n\n This is the Life Insurance Relief Calculator for the Year of Assessment 2024')
cpf_contribution_ceiling = 5000
life_insurance_value = int(input('Enter your Life Insurance value minus all unqualified plans($):\n'))
annual_insurance_premium = int(input('Enter your annual insurance premium paid($):\n'))
employee_cpf = int(input('Enter your compulsory employee cpf contribution($):\n[Must be less than $5000]\n'))

difference = 5000 - employee_cpf
difference = round(difference, 2)
percentage = life_insurance_value * (7 / 100)
percentage = round(percentage, 2)
premium_paid = annual_insurance_premium
premium_paid = round(premium_paid, 2)
if difference < percentage and difference < premium_paid:
    print(f'You are eligible for ${difference} of Life Insurance Relief')
elif percentage < difference and percentage < premium_paid:
    print(f'You are eligible for ${percentage} of Life Insurance Relief')
elif premium_paid < difference and premium_paid < percentage:
    print(f'You are eligible for ${premium_paid} of Life Insurance Relief')