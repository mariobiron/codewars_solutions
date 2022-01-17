# Attribute a "weight" to numbers. The weight of a number will be from now on the sum of its digits.
# For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99.
# Given a string with the weights of FFC members in normal order can you give this string ordered by "weights" of these numbers?
# Example:
# "56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes:
# "100 180 90 56 65 74 68 86 99"
# When two numbers have the same "weight", let us class them as if they were strings (alphabetical ordering) and not numbers:
# 180 is before 90 since, having the same "weight" (9), it comes before as a string.
# All numbers in the list are positive numbers and the list can be empty.
# Notes
# it may happen that the input string have leading, trailing whitespaces and more than a unique whitespace between two consecutive numbers
# For C: The result is freed.

def order_weight(strng):
    newstr = ''
    new_list = []
    final_list = []
    str_list = strng.split()
    v = enumerate(str_list)
    for e in v:
        w = 0
        for i in e[1]:
            w += int(i)
        new_list.append((w,str(e[1])))
    final_list = sorted(new_list, key=lambda x: (x[0], x[1]))
    for x,y in final_list:
        newstr += str(y) + ' '
    return(newstr.strip())


print(order_weight("103 123 4444 99 2000")) #, "2000 103 123 4444 99")
print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123")) #, "11 11 2000 10003 22 123 1234000 44444444 9999")
print(order_weight("")) #, "")

# def order_weight(_str):
#     return ' '.join(sorted(sorted(_str.split(' ')), key=lambda x: sum(int(c) for c in x)))

# def sum_string(s):
#     sum = 0
#     for digit in s:
#         sum += int(digit)
#     return sum
#
# def order_weight(strng):
#     # your code
#     initial_list = sorted(strng.split())
#     result = " ".join(sorted(initial_list, key=sum_string))
#
#     return result

# def weight_key(s):
#     return (sum(int(c) for c in s), s)
# def order_weight(s):
#     return ' '.join(sorted(s.split(' '), key=weight_key))

# def order_weight(strng):
#     return " ".join( sorted(strng.split(), key=lambda x: (sum(int(d) for d in x) , x)  ) )