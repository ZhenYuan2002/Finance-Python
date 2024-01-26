print('''Parent Relief(PAR) or Handicapped Parent Relief(HPAR) is given to promote filial piety and recognise individuals who are supporting 
their parents, grandparents, parents-in-law or grandparents in Singapore.


Qualifying Conditions for Parent Relief:
1) Supported the following dependants in the previous year:
   - Parents/Parents-in-law
   - Grandparents/Grandparents-in-law
   - Great Grandparents/Great Grandparents-in-law
2) Dependant was living in your household in Singapore, OR
   Dependant lived in a seperate household in Singapore, and you incurred $2,000 or more supporting him/her
3) Dependant was 55 years of age and above
4) Dependant did not have an annual income exceeding $4,000

Qualifying Conditions for Handicapped Parent Relief:
1) Supported the following dependants in the previous year:
   - Parents/Parents-in-law
   - Grandparents/Grandparents-in-law
   - Great Grandparents/Great Grandparents-in-law
2) Dependant is/was physically or mentally disabled


Rules:
1) PAR/HPAR may be shared with other claimants, provided no one else is claiming any other reliefs (except for Grandparent Caregiver Relief)
  on the same dependant
2) If you are claiming for this relief, no other claimant will be able to claim the following:
     - Spouse Relief/Handicapped Spouse Relief
     - Handicapped Brother/Sister Relief
3) You may claim PAR/HPAR for up to 2 dependants
4) You may claim the full amount of relief even though dependant has passed away in the previous year
5) If you are a working mother, you may claim both PAR/HPAR and Grandparent Caregiver Relief on the same dependant
6) Total personal tax relief is capped at $80,000


Relief Eligible:

        Type of Parent Relief                                 Parent Relief                    Handicapped Parent Relief
        Taxpayer stays with dependant                         $9,000 per dependant              $14,000 per dependant
        Taxpayer does not stay with dependant                 $5,500 per dependant              $10,000 per dependant
        
        ''')

print('''The following question will determine you eligibility for the Parent/Handicapped Parent Relie, and how much you can claim.
Enter 'y' for yes and 'n' for no, unless otherwise stated''')
number_dependants = int(input('How many dependants are you looking to claim (MAXIMUM 2)?'))
total_par = 0
total_dependants = 0
while number_dependants > 0 and number_dependants <= 2:
    q1 = input('Was the dependant handicapped in the previous year?')
    if q1.lower() == 'y':
        q2 = input('Was the dependant supported by you in the previous year?')
        if q2.lower() == 'y':
            q3 = input('Did the dependant stay with any of the claimants?')
            if q3.lower() == 'y':
                total_par += 14000
                print('You can claim $14,000 for the dependant')
            elif q3.lower() == 'n':
                total_par += 10000
                print('You can claim $10,000 for the dependant')
        elif q2.lower() == 'n':
            print('Sorry! You are not eligible for the Parent/Handicapped Parent Relief.')

    elif q1.lower() == 'n':
        q2 = input('Was the dependant supported by you in the previous year?')
        if q2.lower() == 'y':
            q3 = input('''Was the dependant living in your household OR living in a seperate household in Singapore and you incurred $2,000 supporting him/her?''')
            if q3.lower() == 'y':
                q4 = input('Was the dependant 55 years of age or above in the previous year?')
                if q4.lower() == 'y':
                    q5 = input('Did the dependant NOT have an annual income exceeding $4,000?')
                    if q5.lower() == 'y':
                        q6 = input('Did the dependant stay with any of the claimants?')
                        if q6.lower() == 'y':
                            total_par += 9000
                            print('You can claim $9,000 for the dependant')
                        elif q6.lower() == 'n':
                            total_par += 5500
                            print('You can claim $5,500 for the dependant')
                    elif q5.lower() == 'n':
                        print('Sorry! You are not eligible for the Parent/Handicapped Parent Relief.')
                elif q4.lower() == 'n':
                    print('Sorry! You are not eligible for the Parent/Handicapped Parent Relief.')
            elif q3.lower() == 'n':
                print('Sorry! You are not eligible for the Parent/Handicapped Parent Relief.')
        elif q2.lower() == 'n':
            print('Sorry! You are not eligible for the Parent/Handicapped Parent Relief.')

    number_dependants -= 1
    total_dependants += 1

else:
    print(f'You can claim ${total_par} for {total_dependants} dependants.')