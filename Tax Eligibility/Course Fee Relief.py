CFR = print('''Course Fees Relief is given to encourage individuals to continuously upgrade their skills and enhance employability

Qualifying Conditions:
1) Attended any course or study, seminar or conference in the previous year for the purpose of gaining an approved academic, professional or vocational qualification
2) Any course, seminar or conference in the previous year that is relevant to your current employment, trade business, profession or vocation
3) Any course, seminar, or conference between 1 Jan 2021 to 31 Dec 2022 that is relevant to your new employment, trade, business, profession or vocation in 2023
4) Approved vocational qualification have the following conditions:
   - the acquired skill/knowledge should be one that can be applied in a vocation or a specific area in an industry, AND
   - the course, seminar or conference provider is a Singapore registered entitiy with the Accounting and Corporate Regulatory Authority(ACRA)
5) The course have not been paid/reimbursed by your employer or any other organisations such as SkillsFuture Credit
   - If course fee have been partially paid by employer (e.g.75%), you can claim the rest of the unpaid fees (e.g.25%)
6) Following types of courses can be claimed:
   - Apitude test fees (Computer Courses)
   - Examination fees
   - Registration/Enrollment fees
   - Tuition Fees

Courses not eligible for relief:
1) Courses, seminars and conferences for recreational, leisure or hobby (e.g. photography, learning, sports courses)
2) Courses, seminars and conferences for gerneral knowledge or skills (e.g.MS Office, basic website building)
3) Polytechnic/University Courses if graduates have never exercised any employment or carried on the trade, profession or vocation previously
4) Vacation jobs or internships are not considered employment for the purpose of this relief

Payout:
$5,500 per year
For multi-year courses where payment have been made upfront, you can claim up to 5,500 per year for the length of the course duration in years
''')

duration = int(input("Enter '1' if you are calculating a course which spans multiple years, or '2' if you are calculating multiple courses which spans a year."))
if duration == 1:
    course_expense = int(
        input('Enter the total expense incurred by the course/study/seminar/conference applicable($):\n '))
    course_duration = int(input('Enter the duration of the course in years:\n '))
    spread = int(input('Enter "1" to spread the fees evenly through the years, or "2" to claim the fees as fast as possible'))
    if course_expense / course_duration <= 5500:
        course_expense = course_expense
        year = 0
        while course_expense > 5500:
            course_expense -= 5500
            year += 1
        else:
            print(f'You can claim $5,500 in Course Fee Relief for {year} years and claim the last ${course_expense} in the {year + 1}th year.')

    elif course_expense / course_duration > 5500:
        print(f"You can claim a maximum of $5,500 in Course Fee Relief for {course_duration} years")

#Find a way to calculate the fastest number of years you can get your course fees back


elif duration == 2:
    course_expense = int(input('Enter the total expenses incurred by all course/study/seminar/conferences applicable($):\n '))
    if course_expense > 5500:
        course_fees_relief = 5500
        print(f'You are eligible for ${course_fees_relief} of Course Fee Relief')
    else:
        print(f'You are eligible for ${course_expense} of Course Fee Relief')