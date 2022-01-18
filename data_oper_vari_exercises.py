# identify data types
type(99.9) #float
type("False") #str
type(False) #bool
type('0') #str
type(0) #int
type(True) #bool
type('True') #str
type({}) #dict
type({'a': []}) #dict

#A term or phrase typed into a search box?
#ANS: str
#If a user is logged in?
#ANS: str
#A discount amount to apply to a user's shopping cart?
#ANS: int
#Whether or not a coupon code is valid?
#ANS: bool
#An email address typed into a registration form?
#ANS: str
#The price of a product?
#ANS: float
#A Matrix?
#ANS: dict
#The email addresses collected from a registration form?
#ANS: dict
#Information about applicants to Codeup's data science program?
#ANS: dict

'1' + 2
# cannot concat str and int
6 % 4
# what can into six and four
type(6 % 4)
# the 6 % 4 will produce an int
type(type(6 % 4))
# returns with 'type'
'3 + 4 is ' + 3 + 4
# the '' make that data a str and trys to concat
0 < 0
# False 0 is not less then 0
'False' == False
# returned False due to 'False' does not equal False
True == 'True'
# False is returned because 'True" is a str
5 >= -5
# True because 5 is greater then -5
True or '42'
# True is returned because '42' is not associated with a bool
6 % 5
# 1 is returned because 1 can go into 6 and 5
5 < 4 and 1 == 1
# False, because 5 is not greater then 4
'codeup' == 'codeup' and 'codeup' == 'Codeup'
# False due to the last codeup to be CAPS
4 >= 0 and 1 !== '1'
# returns an error because '!==' is not proper oporator
6 % 3 == 0
# True because 
5 % 2 !=0
# True 5 remainder 2 does not equal 0
[1] + 2
# can only concat list to list
[1] + [2]
# [1, 2] concat both list
[1] * 2
# [1, 1] concat fist list twice
[1] * [2]
# error cannot multpy by non-int
[] + [] == []
# True 
{} + {}
# error unsupported