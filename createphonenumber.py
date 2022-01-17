#create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

def create_phone_number(n):
    import re
    s = ''.join([str(elem) for elem in n])
    #return ('(%s) %s-%s' % tuple(re.findall(r'\d{4}$|\d{3}', s)))
    return re.sub(r'(\d{3})(\d{3})(\d{4})', r'(\1) \2-\3', s)
    #return ("("+num[:3]+")"+num[3:6]+"-"+num[6:])

if __name__ == '__main__':
    print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) #, "(123) 456-7890")
    print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) #, "(111) 111-1111")
    print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) #, "(123) 456-7890")
    print(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0])) #, "(023) 056-0890")
    print(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) #, "(000) 000-0000")

#def create_phone_number(n):
#    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

#def create_phone_number(n):
#    n = ''.join(map(str,n))
#    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])

#def create_phone_number(n):
#    return "(%i%i%i) %i%i%i-%i%i%i%i" % tuple(n)

#def create_phone_number(n):
#    m = ''.join(map(str, n))
#    return f"({m[:3]}) {m[3:6]}-{m[6:]}"