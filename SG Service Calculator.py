#This is a calculator you can use to calculate GST, Service Charge, Tips
#There are also options to split the bill or to choose someone random to foot the bill

print('''Hi! Welcome to the GST and Service Charge calculator!
 Here are the options we have available for you:
1) GST + Service Charge + Subtotal + Tip(optional)
2) GST + Subtotal + Tip(optional)
3) Service charge + Subtotal + Tip(optional)
4) Split the total balance among X people + Tip(optional)
5) Calculate GST,Service Charge and Subtotal and tip(optional) and split the total balance among X people
6) Choose someone random to pay the bill
''')
country = input('Please enter a country')
number = int(input('Please enter your desired option:\n '))


#SERVICE CHARGE IS SUBJECTIBLE TO GST, subtotal + (subtotal + servicecharge%) first, then total + (subtotal * gst%)
#Still have to find a way to round of to nearest interger instead of nearest 2.dp and return total at 2.d.p
if number == 1:
    print('You have choosen to calculate GST and Service Charge and Subtotal')
    subtotal = float(input('What is the subtotal?($)'))
    gst = int(input('What is the GST(%) in your country?\n'))
    service_charge = int(input('How much is the Service Charge(%)\n'))
    _gst = subtotal * ((gst / 100))
    _servicecharge = subtotal * ((service_charge / 100))
    servicecharge_gst_subtotal = subtotal + _servicecharge + _gst
    servicecharge_gst_subtotal_rounded = round(servicecharge_gst_subtotal, 2)
    print(f'You total is ${servicecharge_gst_subtotal_rounded}')

#total + (subtotal * gst%)
elif number == 2:
    print('You have to calculate GST and Subtotal')
    subtotal = float(input('What is the subtotal?($)'))
    gst = int(input('What is the GST(%) in your country?\n'))
    _gst = subtotal * ((gst / 100))
    _gst_and_subtotal = _gst + subtotal
    gst_and_subtotal_rounded = round(_gst_and_subtotal, 2)
    print(f'Your total is ${gst_and_subtotal_rounded}')

#total = subtotal + (subtotal * servicecharge%)
elif number == 3:
    print('You have choosen to calculate Service Charge and Subtotal')
    subtotal = float(input('What is the subtotal?($)'))
    service_charge = int(input('How much is the Service Charge(%)\n'))
    _servicecharge = subtotal * ((service_charge / 100))
    servicecharge_subtotal = subtotal + _servicecharge
    servicecharge_subtotal_rounded = round(servicecharge_subtotal, 2)
    print(f'Your total is ${servicecharge_subtotal_rounded}')

#each individual must pay total/X
elif number == 4:
    print('You have choosen to split the total balance among X people')
    totalbill = input('What was the total bill($)?')
    tip = input('What percentage tip would you like to give?')
    people = input('How many people to split the bill?')
    total_amount = ((float(totalbill) * float(tip)) / 100) + float(totalbill)
    individual = float(total_amount) / float(people)
    individual_amount = round(individual, 2)
    print(f'Each person should pay: ${individual_amount}')


elif number == 5:
    print('You have choosen to calculate the total and split it among X people')
    subtotal = float(input('What is the subtotal?($)'))
    gst = int(input('What is the GST(%) in your country?\n'))
    service_charge = int(input('How much is the Service Charge(%)\n'))
    _gst = subtotal * ((gst / 100))
    _servicecharge = subtotal * ((service_charge / 100))
    servicecharge_gst_subtotal = subtotal + _servicecharge + _gst
    totalbill = servicecharge_gst_subtotal
    tip = input('What percentage tip would you like to give?')
    people = input('How many people to split the bill?')
    total_amount = ((float(totalbill) * float(tip)) / 100) + float(totalbill)
    individual = float(total_amount) / float(people)
    individual_amount = round(individual, 2)
    print(f'The total bill after tipping is ${round(total_amount, 2)}')
    print(f'Each person should pay: ${individual_amount}')

elif number == 6:
    print('You have choosen the Banker Roulette!')
    names_string = input("Enter the players names, seperate them by a comma and space:\n ")
    names = names_string.split(", ")
    import random
    random_integer = random.randint(0, len(names) - 1)
    x = int(random_integer)
    if random_integer == x:
        print(names[int(x)] + ' is going to buy the meal today!')



print('''Hi! Welcome to the GST and Service Charge calculator!
 Here are the options we have available for you:
1) GST + Service Charge + Subtotal + Tip(optional)
2) GST + Subtotal + Tip(optional)
3) Service charge + Subtotal + Tip(optional)
4) Split the total balance among X people + Tip(optional)
5) Calculate GST,Service Charge and Subtotal and tip(optional) and split the total balance among X people
6) Choose someone random to pay the bill
''')

number = int(input('Please enter your desired option:\n '))


#SERVICE CHARGE IS SUBJECTIBLE TO GST, subtotal + (subtotal + servicecharge%) first, then total + (subtotal * gst%)
#Still have to find a way to round of to nearest interger instead of nearest 2.dp and return total at 2.d.p
if number == 1:
    print('You have choosen to calculate GST and Service Charge and Subtotal')
    subtotal = float(input('What is the subtotal?($)'))
    gst = int(input('What is the GST(%) in your country?\n'))
    service_charge = int(input('How much is the Service Charge(%)\n'))
    tip = float(input('What percentage tip would you like to give?'))
    _gst = subtotal * ((gst / 100))
    _servicecharge = subtotal * ((service_charge / 100))
    servicecharge_gst_subtotal = subtotal + _servicecharge + _gst
    total_amount = ((float(servicecharge_gst_subtotal) * float(tip)) / 100) + float(servicecharge_gst_subtotal)
    total_amount_rounded = round(total_amount, 2)
    print(f'You total is ${total_amount_rounded}')

#total + (subtotal * gst%)
elif number == 2:
    print('You have to calculate GST and Subtotal')
    subtotal = float(input('What is the subtotal?($)'))
    gst = int(input('What is the GST(%) in your country?\n'))
    tip = float(input('What percentage tip would you like to give?'))
    _gst = subtotal * ((gst / 100))
    _gst_and_subtotal = _gst + subtotal
    total_amount = ((float(_gst_and_subtotal) * float(tip)) / 100) + float(_gst_and_subtotal)
    total_amount_rounded = round(total_amount, 2)
    print(f'Your total is ${total_amount_rounded}')

#total = subtotal + (subtotal * servicecharge%)
elif number == 3:
    print('You have choosen to calculate Service Charge and Subtotal')
    subtotal = float(input('What is the subtotal?($)'))
    service_charge = int(input('How much is the Service Charge(%)\n'))
    tip = float(input('What percentage tip would you like to give?'))
    _servicecharge = subtotal * ((service_charge / 100))
    servicecharge_subtotal = subtotal + _servicecharge
    total_amount = ((float(servicecharge_subtotal) * float(tip)) / 100) + float(servicecharge_subtotal)
    total_amount_rounded = round(total_amount, 2)
    print(f'Your total is ${total_amount_rounded}')

#each individual must pay total/X
elif number == 4:
    print('You have choosen to split the total balance among X people')
    totalbill = input('What was the total bill($)?')
    tip = input('What percentage tip would you like to give?')
    people = input('How many people to split the bill?')
    total_amount = ((float(totalbill) * float(tip)) / 100) + float(totalbill)
    individual = float(total_amount) / float(people)
    individual_amount = round(individual, 2)
    print(f'Each person should pay: ${individual_amount}')


elif number == 5:
    print('You have choosen to calculate the total and split it among X people')
    subtotal = float(input('What is the subtotal?($)'))
    gst = int(input('What is the GST(%) in your country?\n'))
    service_charge = int(input('How much is the Service Charge(%)\n'))
    _gst = subtotal * ((gst / 100))
    _servicecharge = subtotal * ((service_charge / 100))
    servicecharge_gst_subtotal = subtotal + _servicecharge + _gst
    totalbill = servicecharge_gst_subtotal
    tip = input('What percentage tip would you like to give?')
    people = input('How many people to split the bill?')
    total_amount = ((float(totalbill) * float(tip)) / 100) + float(totalbill)
    individual = float(total_amount) / float(people)
    individual_amount = round(individual, 2)
    print(f'The total bill after tipping is ${round(total_amount, 2)}')
    print(f'Each person should pay: ${individual_amount}')

elif number == 6:
    print('You have choosen the Banker Roulette!')
    names_string = input("Enter the players names, seperate them by a comma and space:\n ")
    names = names_string.split(", ")
    import random
    random_integer = random.randint(0, len(names) - 1)
    x = int(random_integer)
    if random_integer == x:
        print(names[int(x)] + ' is going to buy the meal today!')







#Global GST and Service Charge calculator
#Identify the countriey user is from
#Import their currency symbol
#Step 1: Identify the subtotal in their respective currencies
#Step 2: Input GST rate(%)
#Step 3: Input Service charge rate(%)
#Step 4: Return total with GST added only
#Step 5: Return total with Service charge only
#Step 6: Return total with GST and Service Charge
#Step 7: Allows you to split the bill evenly
#gst, servicecharge, gst and subtotal, service charge and subtotal, gst and service charge and subtotal,
#SERVICE CHARGE IS SUBJECTIBLE TO GST, subtotal plus service charge first, then total + (subtotal + gst)
#Tip Calculator
#Banker Roulette

#Calculations Used
#_gst = subtotal * ((gst/100))
#gst_rounded = round(only_gst,2)
#_servicecharge = subtotal * ((service_charge/100))
#servicecharge_rounded = round(only_servicecharge,2)
#_gst_and_subtotal = subtotal + _gst
#gst_and_subtotal_rounded = round(only_gst_and_subtotal,2)
#servicecharge_gst_subtotal = subtotal + _service_charge + _gst
#servicecharge_gst_subtotal_rounded = round(_servicecharge_gst_subtotal,2)
#servicecharge_subtotal = subtotal + servicecharge
#servicecharge_subtotal_rounded = round(servicecharge_subtotal,2)




