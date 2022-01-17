def high_and_low(numbers):
    lNums = numbers.split()
    nNums = []
    for n in range(0,len(lNums)):
        nNums.append(int(lNums[n]))
    nNums.sort(reverse=True)
    sNums = str(nNums[0]) + ' ' + str(nNums[len(nNums)-1])
    return sNums


if __name__ == '__main__':
    print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
    print(high_and_low("1 2 3"))

#def high_and_low(numbers): #z.
#    nn = [int(s) for s in numbers.split(" ")]
#    return "%i %i" % (max(nn),min(nn))