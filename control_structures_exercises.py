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
    paycheck = (((hrs_per_week - 40) * pay_per_hr) * 1.5) + (pay_per_hr * 40)

print(f'Your pay is {paycheck}')

# Loop Basics
# While
# a. Create an integer variable i with a value of 5.
#   Create a while loop that runs so long as i is less than or equal to 15
#   Each loop iteration, output the current value of i, then increment i by one.
i = 5
while i <= 15:
    print(i)
    i += 1

# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
i = 0
while i <= 100:
    print(i)
    i += 2
# Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i >= -10:
    print(i)
    i -= 5
# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000.
i = 2
while i < 1000000:
   print(i)
   i = i**2

i = 100
while i >= 5:
   print(i)
   i -= 5

# For Loops
# b. i. 

number = input('Enter a number:\n')
for n in range(1, 11):
    intn = n
    n = int(number) * n
    print(number,' x ',intn,' = ', n)
# ii.

for n in range(1, 10):
    print(str(n) * n)

# c. i.
num = input('Enter an odd number between 1 and 50:')
if num.isdigit():
    while (int(num) > 50) or (int(num) % 2 == 0):
        num = input('Enter an odd number between 1 and 50:')
        while not num.isdigit():
            num = input('Enter an odd number between 1 and 50:')
    for n in range(1, 51):
        if int(num) == n:
            print('Skipping')
            continue
        elif n % 2 == 0:
            continue
        else:
            print(f'Here is an odd number: {n}')
else:
    while num.isdigit():
        num = input('Enter an odd number between 1 and 50')

# d.
num = input('Enter a positive number:')
while not num.isdigit():
    num = input('Try Again!')
for n in range(0, int(num) + 1):
    print(n)

# e.
num = input('Enter a positive number:')
while not num.isdigit():
    num = input('Try Again!')
n = int(num)
while n >= 1:
    print(n)
    n -= 1

# 3. 

for n in range(1, 101):
    if n % 3 == 0 or n % 5 == 0:
        if n % 3 == 0 and n % 5 == 0:
            print('FizzBzz')
        elif n % 3 == 0:
            print('Fizz')
        elif n % 5 == 0:
            print("Buzz")
    else:
        print(n)

# 4.
num = int(input('Enter a number!\n'))
print('------ Your Table ------')
print('number | squared | cubed')
print('------ | ------- | -----')
for n in range(1, num+1):
    print('{0:7}'.format(f'{n}') + '| ' + 
    '{0:9}'.format(f'{n**2}') + '| ' + f'{n**3}')
ans = input('Do you want to use another number y/n:\n')
while ans == 'y':
    num = int(input('Enter a number!\n'))
    print('------ Your Table ------')
    print('number | squared | cubed')
    print('------ | ------- | -----')
    for n in range(1, num+1):
         print('{0:7}'.format(f'{n}') + '| ' + 
         '{0:9}'.format(f'{n**2}') + '| ' + f'{n**3}')
    ans = input('Want try another number y/n')