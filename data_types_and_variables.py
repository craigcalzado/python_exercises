
from atexit import register
from concurrent.futures.process import _ThreadWakeup
from re import T
from sre_constants import SUCCESS

# 1.
the_little_mermaid = 3 #days
brother_bear = 5 #days
hercules = 1 #days
cost_per_movie = 3 # dollars

total_days_rented = the_little_mermaid + brother_bear + hercules

total_cost = total_days_rented * cost_per_movie
print(total_cost)


# 2.
google = 400
amazon = 380
facebook = 350

payment = (facebook * 10) + (google * 6) + (amazon * 6)

print(payment)

# 2.
class_closed = False
class_open = True
schedule_conflicts = False
schedule_not_conflicts = True

class_open and schedule_not_conflicts
class_open and schedule_conflicts
class_closed or schedule_conflicts

reg_for_classes = class_open and schedule_not_conflicts
print(reg_for_classes)

# 3.
items_in_cart = 4

min_items = 3

offer_expired = False
offer_not_expired = True
premium_member = True
not_premium_member = False

items_in_cart >= min_items and offer_not_expired
discount_applied = items_in_cart >= min_items or premium_member and offer_not_expired
print(discount_applied)

# 4.
username = 'codeup'
password = 'notastrongpassword'

min_pass_char = 5
max_user_char = 20
same_info = username == password
 
pass_char = len(password) >= min_pass_char
user_char = len(username) < max_user_char

success = pass_char and user_char and not same_info

print(success)

# Bonus
user_space = username[0] == ' ' or username[-1] == ' '
pass_space = password[0] == ' ' or password[-1] == ' '

success = pass_char and user_char and not same_info and not (user_space or pass_space)

print(success)

# BONUS
 