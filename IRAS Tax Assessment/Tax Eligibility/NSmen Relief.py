print('''All eligible operationally ready NSmen are entitled to the NSman Tax Relief.
NSman Tax Relief is to recognise their contributions to National Service. This relief is allowed based on National Service
done in the previous work year (1 April to 31 March).

Rules:
There are 3 types of NSman Tax Relief: 
1) NSman Self Relief
2) NSman Wife Relief
3) NSman Parent Relief

NSman Self Relief:

Qualifying Conditions:
- Must have completed full-time National Service under the Enlistment Act, OR
  deemed to have completed such service by the proper authority
- Regulars from MINDEF, SPF, SCDF, CNB, SPS and NSmen who have committed any disciplinary or criminal offences in
  the preceding work year (1 April to 31 March) are excluded

Rules:
- Do not need to claim NSman Self Relief, IRAS will automatically grant this relief to you based on your eligibility
  and records sent to IRAS by MINDEF, SPF and SCDF
- If you are a father, and, you and your son are both NSman, you will be eligible for EITHER Nsman Self Relief OR
  NSman Parent Relief, whichever is higher
- For Year of Assessment 2024, the work year is from 1 April 2023 to 31 March 2024

Relief Eligible:
Did you perform NS activities                NSmen                          NS key command and staff appointment holders
in the preceding year

No                                           $1,500                                  $3,500
Yes                                          $3,000                                  $5,000



NSman Wife Relief

Qualifying Conditions:
- Singaporean Citizen in the preceding year, and husband is eligible for NSman Self Relief
- Widow of a deceased NSman, unless remarried
- A divorce from NSman will render you ineligible

Rules:
-Do not have to claim NSman Wife Relief, IRAS will automatically grant this relief to you based on your eligibility

Relief Eligible:
$750



NSman Parent Relief

Qualifying Conditions:
-SG Citizen in the preceding year
- Child is eligible for NSman Self Relief
- Child was born to you and spouse/ex-spouse OR your step-child OR legally adopted child
- Parents of deceased NSman are eligible for this relief
- If you and your son are both NSman, you will be eligible for either the NSman Self Relief OR
  the NSman Parent Relief, whichever is higher

Rules:
- Do not have to claim NSman Parent Relief as IRAS will automatically grant it to you based on your eligibility

Relief Eligible:
$750, regardless of number of children who are NSmen






''')

scenario = print('''The following questions are to determine which NSman relief is eligible for you, if any.
Enter 'Y' for Yes, and 'N' for No''')
print('NOTE: NSMan Self Relief overrides all other NSMan Reliefs as it has the highest amount')
q1 = input('Are you a NSman?\n')
if q1.capitalize() == 'Y':
    q2 = input('Did you perform NS activites in the preceding year?\n')
    if q2.capitalize() == 'Y':
        q3 = int(input(
            'Enter "1" if you are a regular NSman or "2" if you are in the NS Key Command and Staff Appointment Holders'))
        if q3 == 1:
            print('You are eligible for $3,000 in NSman Self Relief!')
        elif q3 == 2:
            print('You are eligible for $5,000 in NSman Self Relief!')
    elif q2.capitalize() == 'N':
        q3 = int(input(
            'Enter "1" if you are a regular NSman or "2" if you are in the NS Key Command and Staff Appointment Holders'))
        if q3 == 1:
            print('You are eligible for $1,500 in NSman Self Relief!')
        elif q3 == 2:
            print('You are eligible for $3,500 in NSman Self Relief!')

elif q1.capitalize() == 'N':
    q2 = input('Are you the parent of one or more NSman?')
    if q2.capitalize() == 'Y':
        q3 = input('Are you the father of one or more NSman?')
        if q3.capitalize() == 'Y':
            print('You are eligible for $750 in Nsman Parent Relief!')
        elif q3.capitalize() == 'N':
            q4 = input('Are you the mother of one or more NSman?')
            if q4.capitalize() == 'Y':
                q5 = input('Are you currently married to a NSman, OR widow to a NSman and is not remarried?')
                if q5.capitalize() == 'Y':
                    print('You are eligible to $750 in EITHER Nsman Parent Relief OR NSman Wife Relief!')
                elif q5.capitalize() == 'N':
                    print('Sorry! You are not eligible for any NSman Reliefs.')
            elif q4.capitalize() == 'N':
                print('Sorry! You are not eligible for any NSman Reliefs.')


    elif q2.capitalize() == 'N':
        q3 = input('Are you currently married to a NSman, or widow to a NSman and is not remarried?')
        if q3.capitalize() == 'Y':
            print('You are eligible to $750 in NSman Wife Relief!')
        elif q3.capitalize() == 'N':
            print('Sorry! You are not eligible for any NSman Reliefs.')

