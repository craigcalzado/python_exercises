#1. 
# is_two defines the input which is an int and will return True or False depending it its a 2. 
def is_two(int(n)):
    if n == 2 :
        return True
    else:
        return False

# better way to ans
#def is_two(n)
#    return n == 2 or n == '2'

is_two(input('Pick a number between 1 and 3'))

#2.
def is_vowel(vowel):
    if vowel in ('aeiou'):
        return True
    else:
        return False


is_vowel(input('Enter a single letter:'))

#3.
def is_consonant(x):
    if x not in ('aeiou'):
        return True
    else:
        return False

is_consonant(input('Enter another single letter'))

#4.
def is_word(x):
    if x[0] not in 'aeiou':
        return x.capitalize()
    else:
        print('does not start with consonant or not a word')
        return x 

is_word(input('Enter a word:'))

#5.
def calculated_tip(tip_percent, bill):
    amount_to_tip = tip_percent * bill
    return amount_to_tip

calculated_tip(float(input('Enter tip percent:')), int(input('Enter bill amount:')))

#6.
def apply_discount(price, discount):
    amount_discounted = price * discount
    price_post_discount = price - amount_discounted
    return price_post_discount

apply_discount(int(input('Enter price:')), float(input('Enter discount:')))

#7.
def handle_commas(x):
    no_commas = x.replace(',', '')
    if no_commas.isdigit():
        return int(no_commas)
    else:
        print('Get outta here with those letters!')

handle_commas(input('Enter a large number:'))

#8.
def get_letter_grade(x):
    if x in range(0, 60):
        return 'F'
    elif x in range(60, 67):
        return 'D'
    elif x in range(67, 80):
        return 'C'
    elif x in range(80, 88):
        return 'B'
    elif x in range(88, 100):
        return 'A'
    else:
        print('I dont know what to do...')  

get_letter_grade(int(input('Enter your grade')))

#9.
def remove_vowels(x):
    r_vow = ''
    for char in x:
        if char in ('aeiou'):
            continue
        else:
            r_vow += char
    return r_vow

remove_vowels(input('Enter a word:'))

#10.
all_char = ' abcdefghijklmnopqrstuvwxyz_1234567890'
def normalize_name(x):
    norm_x = ''
    prime_x = x.strip().lower()
    for char in prime_x:
        if char not in all_char:
            continue
        else:
            norm_x += char
    return norm_x.strip().replace(' ', '_')

normalize_name(input('Entere your full name:'))

#11. 
def cumulative_sum(x):
    for n in range(1, len(x)):
        x[n] += sum(x[n - 1:n])
    return x



list = [1, 2, 3, 4]
cumulative_sum(list)

