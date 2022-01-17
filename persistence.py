#39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
#999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
#4 --> 0 (because 4 is already a one-digit number)

def persistence(n):
    s = str(n)
    l = 0 # loops
    nOut = 1 # mult factor
    #if len(s) > 1:
    while len(s) > 1:
        nOut = 1
        l = l + 1
        for i in s:
            #print("IN: n="+str(n)+", l="+str(l)+ ", s="+s+", nOut="+str(nOut)+", i="+i+", len(s)="+str(len(s)))
            nOut = nOut * int(i)
            s = str(nOut)
            #print("OUT: n=" + str(n) + ", l="+str(l)+", s=" + s + ", nOut=" + str(nOut) + ", i=" + i+", len(s)="+str(len(s)))
    return l

if __name__ == '__main__':
    print(persistence(39)) #, 3)
    print(persistence(4)) #, 0)
    print(persistence(25)) #, 2)
    print(persistence(999)) #, 4)


#import operator
#def persistence(n):
#    i = 0
#    while n>=10:
#        n=reduce(operator.mul,[int(x) for x in str(n)],1)
#        i+=1
#    return i

#def persistence(n):
#    nums = [int(x) for x in str(n)]
#    sist = 0
#    while len(nums) > 1:
#        newNum = reduce(lambda x, y: x * y, nums)
#        nums = [int(x) for x in str(newNum)]
#        sist = sist + 1
#    return sist