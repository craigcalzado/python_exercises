#1.b.
from posixpath import split
from function_exercises import calculated_tip as ct

ct(50, .2)

#2.a.
from itertools import combinations, permutations, product

x2a = ['a', 'b', 'c']
y2a = [ '1', '2', '3']
pr = list(product(x2a, y2a))
print('There are', len(pr), 'different combinations.')
print(pr)

#b.
x2b = ['a', 'b', 'c', 'd']
y2b = 2
c = list(combinations(x2b, y2b))
print(c)
print('There are', len(c), 'different combinations.')

#c.
x2c = ['a', 'b', 'c', 'd']
y2c = 2
pe = list(permutations(x2c, y2c))
print(pe)
print('There are', len(pe), 'different combinations.')

#3.a. Total number of Users
import json
profiles = json.load(open('profiles.json'))
profiles

num_of_users = len(profiles)
print('Total number of users:', num_of_users)

#b. 
count = 0
for users in profiles:
    if users['isActive']:
        count += 1
print(count)

#c.
count = 0
for users in profiles:
    if not users['isActive']:
        count += 1
print(count)

#d. Total balances for all users
grand_total = 0

for users in profiles:
    clean_data = float(users['balance'].replace('$', '').replace(',', ''))
    grand_total += clean_data

print(grand_total)

#e.
avg_balance = grand_total / num_of_users
print(avg_balance)

#f.
balances = []
for users in profiles:
    clean_data = float(users['balance'].replace('$', '').replace(',', ''))
    balances.append(clean_data)
print(min(balances))

#g.
balances = []
for users in profiles:
    clean_data = float(users['balance'].replace('$', '').replace(',', ''))
    balances.append(clean_data)
print(max(balances))

