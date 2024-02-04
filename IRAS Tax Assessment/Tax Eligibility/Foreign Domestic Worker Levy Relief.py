print('''Foreign Domestic Worker Levy(FDWL) is given to encourage married women to stay in the workforce.

Qualifying Conditions:
1) Single and Married Men are NOT eligible for the FDWL Relief
2) You or your husband employed a FDW in the previous year
3) In the previous year, you were either:
   - married and living with your husband
   - married and your husband was not a tax resident of Singapore
   - seperated from your husband, divorced or widowed and had children who lived with you
     AND on whom you could claim child reliefs

Rules:
1) FDWL Relief can only be used to offset your earned income
2) FDWL Relief will lapse for all taxpayers from Year of Assessment 2025
3) Levy rate on first FDW is $300 per month (not on concession). Subsequent FDWs employed is levied at $450 per month.
4) You may claim TWICE the FDW levy paid in the previous year for one foreign domestic worker,
   regardless on whether you or your husband have paid the levy

Payout:
YA 2024                                 Normal                            Concessionary
No.of months levy is paid on 2023        12                                    12
Total levy paid on 2023(1 FDW)OR        $3600 ($300*12)OR                      $720
Total levy paid on 2023(Multiple FDWs)  $5400 ($450*12)
Max FDW Relief for YA 2024              $7200 ($3600*2)OR                      $1440($720*2)
Max FDW Relief for YA 2024              $10800($5400*2)                      
''')



type = input("Enter '1' for normal levy or '2' for concessionary levy")
if type == "1":
    number_fdw = int(input("Insert the number of FDWs you employed in the previous year:\n"))
    if number_fdw == 1:
        levy_rate = 300
        months_paid = int(input("Insert the number of months the FDW was employed by you in the previous year:\n"))
        total_levy_rate = levy_rate * months_paid
        amount_claimable = 2 * total_levy_rate
        print(f'You are eligible for ${amount_claimable} in Foreign Domestic Worker Relief!')
    elif number_fdw > 1:
        levy_rate = 300
        total_levy_rate = 0
        months_paid_1 = int(input("Insert the number of months the first FDW was employed by you in the previous year"))
        levy_rate_1 = levy_rate * months_paid_1
        while number_fdw > 1:
            months_paid = int(
                input("Insert the number of months the next FDW was employed by you in the previous year"))
            total_rates = 450 * months_paid
            total_levy_rate += total_rates
            number_fdw -= 1
        else:
            total_rate = levy_rate_1 + total_levy_rate
            amount_claimable = 2 * total_rate
            if amount_claimable <= 10800:
                print(f'You are eligible for ${amount_claimable} in Foreign Domestic Worker Relief!')
            elif amount_claimable > 10800:
                print(f'You are eligible for $10800 in Foreign Domestic Worker Relief!')


elif type == 2:
    number_fdw = int(input("Insert the number of FDWs you employed in the previous year:\n"))
    levy_rate = number_fdw * 60
    months_paid = int(input("Insert the number of months the FDW was employed by you in the previous year:\n"))
    total_levy_rate = levy_rate * months_paid
    amount_claimable = 2 * total_levy_rate
    if amount_claimable <= 1440:
        print(f'You are eligible for ${amount_claimable} in Foreign Domestic Worker Relief!')
    elif amount_claimable > 1440:
        print(f'You are eligible for $1440 in Foreign Domestic Worker Relief!')
