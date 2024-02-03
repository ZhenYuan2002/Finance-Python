print('''Handicapped Brother/Sister Relief is given to recognise individuals supporting their handicapped siblings and siblings-in-law


Qualifying Conditions (For the year before current Year of Assessment)
1) The dependent was living with you in the same household in Singapore OR
   The dependent lived in a seperate household in Singapore and you incurred $2,000 or more in supporting him/her
2) The dependent is physically and mentally disabled


Rules
1) Each dependant is eligible for ONE Handicapped Brother/Sister Relief
2) Total Personal Tax Relief is capped at $80,000
3) If you supported the same handicapped sibling or sibling-in-law with other claimants,
   all of you may share this relief based on agreed appointment

Relief Eligible
$5,500 for each handicapped sibling/sibling-in-law''')

number_dependants = int(input('How many dependants are you looking to claim?'))
print('''The following question will determine you eligibility for the Parent/Handicapped Parent Relief, and how much you can claim.
Enter 'y' for yes and 'n' for no, unless otherwise stated
NOTE: ALL QUESTIONS ARE TAKEN TO BE IN THE YEAR PRIOR TO CURRENT YEAR OF ASSESSMENT''')

while number_dependants > 0:
    q1 = input('''Was the dependent living with you in the same household in Singapore/
    Living in a separate household in Singapore and you incurred $2,000 or more supporting him/her?''')
    if q1.lower() == 'y':
        q2 = input('''Was the dependent mentally or physically disabled?''' )
        if q2.lower() == 'y':
            q3 = input('Have anyone else claimed the full Handicapped Brother/Sister Relief on this dependent?')
            if q3.lower() == 'y':
                print('Sorry, you are not eligible for the Handicapped Brother/Sister Relief ')
            elif q3.lower() == 'n':
                q4 = input('Are you looking to split the Handicapped Brother/Sister Relief with other claimants?')
                if q4.lower() == 'y':
                    amount_getting = input('How much are you getting after the split?')
                    print(f'You can claim ${amount_getting} of Handicapped Brother/Sister Relief! ')
                elif q4.lower() == 'n':
                    print(f'You can claim $5,500 of Handicapped Brother/Sister Relief!')
        elif q2.lower() == 'n':
            print('Sorry, you are not eligible for the Handicapped Brother/Sister Relief.')
    elif q1.lower() == 'n':
        print('Sorry, you are not eligible for the Handicapped Brother/Sister Relief.')
