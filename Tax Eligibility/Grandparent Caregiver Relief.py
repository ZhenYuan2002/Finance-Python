print('''Grandparent Caregiver Relief(GCR) is given to working mothers who engage the help of their
parents, grandparents, parents-in-law or grandparents-in-law(including those of ex-spouses) to take care of their children.


Qualifying Conditions
1) You are a working mother who is married, divorced or widowed
2) Your parent, grandparent, parent-in-law or grandparent-in-law(including those of ex spouses) was, in the year prior to Year of Assessment:
     - Living in Singapore
     - Looking after any of your children who is a Singaporean Citizen aged 12 or below OR
        looking after unmarried handicapped children who is a Singaporean Citizen 
     - Not working or carrying on any trade, business, profession vocation 
3) No one else have claimed GCR on the same caregiver, although the caregiver can still be the subject of relief claims other than GCR
4) Caregiver does not have an annual income exceeding $4,000


Rule
1) Single or male taxpayers are not eligible for GCR
2) Maximum GCR amount you can claim is $3,000 for ONE caregiver, no one else can claim GCR on the specific caregiver
   after that on the same Year of Assessment
3) Total amount of tax relief is capped at $80,000


Relief Eligible
$3000''')


print('''\n\n\n The following questions will determine whether your child is eligible for the tax relief.
Enter "y" for yes or "n" for no.''')

q1 = input('Are you a working mother who is married, divorced or widowed?')
if q1.lower() == 'y':
    q2 = input('''Was your parent, grandparent, parent-in-law or grandparent-in-law(including those of ex spouses), in the year prior to Year of Assessment:
         - Living in Singapore
         - Looking after any of your children who is a Singaporean Citizen aged 12 or below OR
           looking after unmarried handicapped children who is a Singaporean Citizen 
         - Not working or carrying on any trade, business, profession vocation?''')
    if q2.lower() == 'y':
        q3 = input('Have no one else claimed Grandparent Caregiver Relief on the same caregiver?')
        if q3.lower() == 'y':
            q4 = input("Was the caregiver's annual income less than or equals to $4,000 the year prior?")
            if q4.lower() == 'y':
                print('You can claim $3,000 of Grandparent Caregiver Relief!')
            elif q4.lower() == 'n':
                print('Sorry, you are not eligible for the Grandparent Caregiver Relief.')
        elif q3.lower() == 'n':
            print('Sorry, you are not eligible for the Grandparent Caregiver Relief.')
    elif q2.lower() == 'n':
        print('Sorry, you are not eligible for the Grandparent Caregiver Relief.')
elif q1.lower() == 'n':
    print('Sorry, you are not eligible for the the Grandparent Caregiver Relief.')