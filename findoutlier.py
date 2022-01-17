#[2, 4, 0, 100, 4, 11, 2602, 36]
#Should return: 11 (the only odd number)
#[160, 3, 1719, 19, 11, 13, -21]
#Should return: 160 (the only even number)

def find_outlier(integers):
    a0 = abs(integers[0])
    a1 = abs(integers[1])
    a2 = abs(integers[2])
    d0 = a0/2
    d1 = a1/2
    d2 = a2/2
    i0 = int(a0/2)
    i1 = int(a1/2)
    i2 = int(a2/2)
    s0 = d0 - i0
    s1 = d1 - i1
    s2 = d2 - i2
    b = s0 + s1 + s2
    if b > 0.5:
        pairs = False
    else:
        pairs = True
    for d in range(0,len(integers)):
        if (abs(integers[d]/2) - abs(int(integers[d]/2))) > 0:
            lpair = False
        else:
            lpair = True
        if lpair != pairs:
            outlier = integers[d]
    return outlier

if __name__ == '__main__':
    print(find_outlier([2, 4, 6, 8, 10, 3])) #, 3)
    print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])) #, 11)
    print(find_outlier([160, 3, 1719, 19, 11, 13, -21])) #, 160)

#def find_outlier(int):
#    odds = [x for x in int if x%2!=0]
#    evens= [x for x in int if x%2==0]
#    return odds[0] if len(odds)<len(evens) else evens[0]

#def find_outlier(integers):
#    parity = [n % 2 for n in integers]
#    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]

#def find_outlier(integers):
#    listEven = []
#    listOdd = []
#    for n in integers:
#        if n % 2 == 0:
#            listEven.append(n)
#        else:
#            listOdd.append(n)
#
#    if len(listEven) == 1:
#        return listEven[0]
#    else:
#        return listOdd[0]