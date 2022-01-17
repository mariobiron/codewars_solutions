# Write the function that parses the mileage number input, and returns a 2 if the number is "interesting" (see below), a 1 if an interesting number occurs within the next two miles, or a 0 if the number is not interesting.
# Note: In Haskell, we use No, Almost and Yes instead of 0, 1 and 2.
# "Interesting" Numbers
# Interesting numbers are 3-or-more digit numbers that meet one or more of the following criteria:
# Any digit followed by all zeros: 100, 90000
# Every digit is the same number: 1111
# The digits are sequential, incementing†: 1234
# The digits are sequential, decrementing‡: 4321
# The digits are a palindrome: 1221 or 73837
# The digits match one of the values in the awesome_phrases array
# † For incrementing sequences, 0 should come after 9, and not before 1, as in 7890.
# ‡ For decrementing sequences, 0 should come after 1, and not before 9, as in 3210.
# Error Checking
# A number is only interesting if it is greater than 99!
# Input will always be an integer greater than 0, and less than 1,000,000,000.
# The awesomePhrases array will always be provided, and will always be an array, but may be empty. (Not everyone thinks numbers spell funny words...)
# You should only ever output 0, 1, or 2.

import re

def palyndrom(num,inc):
    if num+inc >= 100 and str(num + inc) == str(num + inc)[::-1]:
        return True
    else:
        return False

def increments(num,inc):
    if num+inc >= 100 and (len(re.findall(str(num+inc) + "+", '9876543210')) > 0 or len(re.findall(str(num+inc) + "+", '1234567890')) > 0):
        return True
    else:
        return False

def endsinzeros(num,inc):
    if num+inc >= 100 and re.match("\d?00+$", str(num+inc)):
        return True
    else:
        return False

def samedigits(num,inc):
    if num+inc >= 100 and len(sorted(set(str(num+inc)))) == 1:
        return True
    else:
        return False

def awesome(num,inc,alist):
    if num+inc >= 100 and num+inc in alist:
        return True
    else:
        return False

def is_interesting(number, awesome_phrases):
    interest = 0
    # find near interesting
    if palyndrom(number,1) or palyndrom(number,2) or increments(number,1) or increments(number,2) or endsinzeros(number,1) or endsinzeros(number,2) or samedigits(number,1) or samedigits(number,2) or awesome(number,1, awesome_phrases) or awesome(number,2, awesome_phrases):
        interest = 1
    # find of real interest
    if palyndrom(number,0) or increments(number,0) or endsinzeros(number,0) or samedigits(number,0) or awesome(number,0,awesome_phrases):
        interest = 2
    return interest
#print(str(number)+' or ('+str(number+1)+' and '+str(number+2)+') or '+str(number)[::-1]+' is: ',end='')
print(is_interesting(9800,[1337, 256])) # 	{'n': 3, 'interesting': [1337, 256], 'expected': 0},
print(is_interesting(9000,[1337, 256])) # 	{'n': 3, 'interesting': [1337, 256], 'expected': 0},
print(is_interesting(100,[1337, 256])) # 	{'n': 3, 'interesting': [1337, 256], 'expected': 0},
print(is_interesting(3,[1337, 256])) # 	{'n': 3, 'interesting': [1337, 256], 'expected': 0},
print(is_interesting(1336,[1337, 256])) # 	{'n': 1336, 'interesting': [1337, 256], 'expected': 1},
print(is_interesting(1337,[1337, 256])) # 	{'n': 1337, 'interesting': [1337, 256], 'expected': 2},
print(is_interesting(256,[1337, 256])) # 	{'n': 256, 'interesting': [1337, 256], 'expected': 2},
print(is_interesting(11208,[1337, 256])) # 	{'n': 11208, 'interesting': [1337, 256], 'expected': 0},
print(is_interesting(11209,[1337, 256])) # 	{'n': 11209, 'interesting': [1337, 256], 'expected': 1},
print(is_interesting(11211,[1337, 256])) # 	{'n': 11211, 'interesting': [1337, 256], 'expected': 2},
# "boring" numbers
print(is_interesting(3, [1337, 256]))    # 0
print(is_interesting(3236, [1337, 256])) # 0

# progress as we near an "interesting" number
print(is_interesting(11207, [])) # 0
print(is_interesting(11208, [])) # 0
print(is_interesting(11209, [])) # 1
print(is_interesting(11210, [])) # 1
print(is_interesting(11211, [])) # 2

# nearing a provided "awesome phrase"
print(is_interesting(1335, [1337, 256])) # 1
print(is_interesting(1336, [1337, 256])) # 1
print(is_interesting(1337, [1337, 256])) # 2

# Any digit followed by all zeros: 100, 90000
print(is_interesting(100, [1337, 256])) # 2
print(is_interesting(90000, [1337, 256])) # 2

# Every digit is the same number: 1111
print(is_interesting(1111, [1337, 256])) # 2

# The digits are sequential, incementing†: 1234
print(is_interesting(1234, [1337, 256])) # 2

# The digits are sequential, decrementing‡: 4321
print(is_interesting(3210, [1337, 256])) # 2

# The digits are a palindrome: 1221 or 73837
print(is_interesting(1221, [1337, 256])) # 2
print(is_interesting(73837, [1337, 256])) # 2

print(is_interesting(80083, [80085])) # 1

# def is_incrementing(number): return str(number) in '1234567890'
# def is_decrementing(number): return str(number) in '9876543210'
# def is_palindrome(number):   return str(number) == str(number)[::-1]
# def is_round(number):        return set(str(number)[1:]) == set('0')
#
# def is_interesting(number, awesome_phrases):
#     tests = (is_round, is_incrementing, is_decrementing,
#              is_palindrome, awesome_phrases.__contains__)
#
#     for num, color in zip(range(number, number+3), (2, 1, 1)):
#         if num >= 100 and any(test(num) for test in tests):
#             return color
#     return 0

# def is_good(n, awesome):
#     return n in awesome or str(n) in "1234567890 9876543210" or str(n) == str(n)[::-1] or int(str(n)[1:]) == 0
#
# def is_interesting(n, awesome):
#     if n > 99 and is_good(n, awesome):
#         return 2
#     if n > 97 and (is_good(n + 1, awesome) or is_good(n + 2, awesome)):
#         return 1
#     return 0