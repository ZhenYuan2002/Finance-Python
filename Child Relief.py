print('''The Qualifying Child Relief(QCR) and the Handicapped Child Relief(HCR) are given to
parents to recognise their efforts in supporing their children.

Qualifying Conditions for QCR:
1) You are a parent maintaining an unmarried child
2) Your child was either:
   - born to you and your spouse/ex-spouse
   - a step-child
   - legally adopted
3) Your child was either:
   - below 16 years old
   - studying full time at any educational institution at any time of the year
4) Your child did not have an annual income exceeding $4,000

Qualifying Conditions for HCR:
1) You are a parent maintaining an unmarried child
2) Your child was either:
   - Born to you and your spouse/ex-spouse
   - a step-child
   - legally adopted
3) Your child is mentally or physically handicapped

Rules:
1) If you are a working mother and have met all the conditions for Working Mother's Child Relief(WMCR),
  you may claim QCR/HCR and WMCR on the same child
  - QCR/HCR will be claimed first
  - QCR/HCR + WMCR will be capped at $50,000
2) You can claim QCR/HCR multiple times for multiple children
3) You can split the amount of tax relief with your spouse/ex-spouse
4) Total Personal Tax Relief is capped at $80,000

Relief Eligible:

           Qualifying Child Relief(QCR)                          Handicapped Child Relief(HCR)
                $4,000 per child                                        $7,500 per child
                
''')
print('''\n\n\n The following questions will determine whether your child is eligible for the tax relief.
Enter "y" for yes or "n" for no.''')
number_of_children = int(input('How many children do you have?'))
total_child_relief = 0
total_children = 0
while number_of_children > 0:
    q1 = input('''Are you a parent maintaining an unmarried child who was either:
    - born to you and your spouse/ex-spouse
    - your step-child
    - a legally adopted child''')
    if q1.lower() == 'y':
        q2 = input('Is your child physically or mentally handicapped?')
        if q2.lower() == 'y':
            child_relief = 7500
            total_child_relief += child_relief
            print('You can claim $7,500 of Handicapped Child Relief!')
        elif q2.lower() == 'n':
            q3 = input('''Was your child either below 16 years old or studying full time at any educational 
            institution\n at any time of the year prior to the Year of Assessment?''')
            if q3.lower() == 'y':
                q4 = input('Did your child have an annual income NOT exceeding $4,000?')
                if q4.lower() == 'y':
                    child_relief = 4000
                    total_child_relief += child_relief
                    print('You can claim $4,000 of Qualifying Child Relief!')
                elif q4.lower() == 'n':
                    print('Sorry! You are not eligible for any Child Relief.')
            elif q3.lower() == 'n':
                print('Sorry! You are not eligible for any Child Relief')
    elif q1.lower() == 'n':
        print('Sorry! You are not eligible for any Child Relief')

    number_of_children -= 1
    total_children += 1

else:
    if total_child_relief < 50000:
        print(f'You can claim s total of ${total_child_relief} of Child Reliefs for your {total_children} eligible children!')
    elif total_child_relief >= 50000:
        print(f'You can claim a total of $50000 of Child Reliefs for your {total_children} eligible children!')