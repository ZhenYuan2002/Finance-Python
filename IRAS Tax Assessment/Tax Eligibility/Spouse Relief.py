print('''Spouse Relief/Handicapped Spouse Relief recognise both male and female taxpayers who have supported their spouses.

Rules:
1) If legally seperated from wife, you may claim this relief if you have made maintenance payments under 
   Court Order or Deed of Seperation
2) Divorced taxpayers who pay alimony to former spouses are not eligible to claim this relief
3) If you claim Spouse Relief/Handicapped Spouse Relief, no other claimant is allowed to claim the following on your spouse
   - Parent Relief/Handicapped Parent Relief
   - Handicapped Brother/Sister Relief
4) Maximum tax relief is capped at $80,000

Qualifying Conditions for Spouse Relief:
- Spouse was living with/supported by you
- Spouse did not have an annual income exceeding $4,000

Qualifying Conditions for Handicapped Spouse Relief:
- Spouse was living with/supported by you
- Spouse is physically or mentally handicapped

Relief Eligible:

   Spouse Relief           Handicapped Spouse Relief              Legally Seperated Spouses ordered to make maintenance
                                                                  payments under a Court Order or Deed of Seperation

   $2,000                         $5,500                           LOWER OF: 
                                                                   1) Maintenance payments in previous year
                                                                   2) $2,000 for wife
                                                                   3) $5,500 for handicapped wife''')

print('''Please answer the following questions to determine your eligiblity as well as how much you can claim this tax relief
Enter 'y' for yes and 'n' for no for the following questions unless specified''')

q1 = input('''Are you legally seperated from your spouse, and is ordered to make maintenance 
payments under a Court Order or Deed of Seperation in the previous year?''')
if q1.lower() == 'y':
    q2 = input('Is your spouse handicapped?')
    if q2.lower() == 'y':
        main_payment = int(input('Enter the total maintenance payment you made in the previous year($):'))
        if main_payment >= 5500:
            print('You can claim $5,500 of Handicapped Spouse Relief!')
        elif main_payment < 5500:
            print(f'You can claim ${main_payment} of Handicapped Spouse Relief!')
    elif q2.lower() == 'n':
        main_payment = int(input('Enter the total maintenance payment you made in the previous year($):'))
        if main_payment >= 2000:
            print('You can claim $2000 of Spouse Relief!')
        elif main_payment < 2000:
            print(f'You can claim ${main_payment} of Spouse Relief!')

elif q1.lower() == 'n':
    q2 = input('Was your spouse handicapped in the previous year?')
    if q2.lower() == 'y':
        q3 = input('Was your spouse living with or supported by you?')
        if q3.lower() == 'y':
            print('You can claim $5,500 in Handicapped Spouse Relief!')
        elif q3.lower() == 'n':
            print('Sorry, you are not eligible for any Spouse Relief.')
    elif q2.lower() == 'n':
        q3 = input('Was your spouse living with or supported by you?')
        if q3.lower() == 'y':
            q4 = input('Did your spouse have an annual income NOT exceeding $4,000?')
            if q3.lower() == 'y':
                print('You can claim $2,000 in Spouse Relief!')
            elif q3.lower() == 'n':
                print('Sorry, you are not eligible for any Spouse Relief.')
        elif q3.lower() == 'n':
            print('Sorry, you are not eligible for any Spouse Relief.')