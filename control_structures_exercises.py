# Conditional Basics 
# a. prompt the user for a day of the week, print out whether the day is Monday or not 
# b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend
# C. create variables and make up values for
# the number of hours worked in one week
# the hourly rate
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

# a.


from calendar import FRIDAY, MONDAY, THURSDAY, TUESDAY, WEDNESDAY


day_of_the_week = input('What day of the week is it?\n')
if day_of_the_week == 'monday':
    print('It is Monday!')
else:
    print('It is not Monday')

# b.
day_of_the_week = input('What day of the week is it?\n')
weekdays = ['monday', 'tuesday', 'wednesday', 'thurday', 'friday']
weekends = ['saturday', 'sunday']
family = ['craig', 'madison', 'margalo']
if day_of_the_week in weekdays:
    print(f'{day_of_the_week} is a weekday')
elif day_of_the_week in weekends:
    print(f'{day_of_the_week} is a weekend')
elif day_of_the_week in family:
    print(f'{day_of_the_week} is the best!!!')
else:
    print(f'{day_of_the_week} is not a day at all.')

# c.
hrs_per_week = float(input('How many hours a week do you work?\n'))
pay_per_hr = float(input('How much do you get paid per hour?\n'))

if hrs_per_week <= 40:
    paycheck = hrs_per_week * pay_per_hr
elif hrs_per_week > 40:
    paycheck = (((hrs_per_week - 40) * pay_per_hr) * 1.5) + pay_per_hr * 40

print(f'Your pay is {paycheck}')