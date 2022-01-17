def myfib(n):
    fibo = [0, 1]
    for i in range(1,n+1): fibo[0], fibo[1] = fibo[1], fibo[0]+fibo[1]
    return fibo[0]

def fib(n):
    mtx = [(1,1),
           (0,1)]
    f = mtx[1]
    if n<0:
        for i in range(n - 1, -1, 1):
            f = f[1] - f[0], f[0]
    else:
        if n & 1:
            f = mtx[0]
        n //= 2
        while n > 0:
            mtx[0] = ((mtx[1][0]*mtx[0][0])+(mtx[1][1]*mtx[0][1])), ((mtx[1][0]*mtx[0][1])+(mtx[1][1]*(mtx[0][0]+mtx[0][1])))
            mtx[1] = mtx[0][1]-mtx[0][0],mtx[0][0]
            if n&1:
                f = ((mtx[1][0]*f[0])+(mtx[1][1]*f[1])), ((mtx[1][0]*f[1])+(mtx[1][1]*(f[0]+f[1])))
            n //= 2
    return f[0]

# Nth Fibonacci number (exponential iterations) O(log(N)) time (N>=0)
def fastfib(n):
    a,b = 1,1
    f0,f1 = 0,1
    r,s = (1,1) if n&1 else (0,1)
    n //= 2
    while n > 0:
        #print('n=' + str(n))
        a,b = ((f0*a)+(f1*b)), ((f0*b)+(f1*(a+b)))
        #print('a='+str(a)+', b='+str(b))
        f0,f1 = b-a,a
        #print('f0='+str(f0)+', f1='+str(f1))
        if n&1: r,s = ((f0*r)+(f1*s)), ((f0*s)+(f1*(r+s)))
        #print('r='+str(r)+', s='+str(s))
        n //= 2
    return r

# Negative values
print(str(fib(-6))) # == -8
print(str(fib(-96))) # == -51680708854858323072
print(str(fib(-35))) # == 9227465
print(str(fib(-63))) # == 6557470319842
print(str(fib(-25))) # == 75025
print(str(fib(0))) # 0
print(str(fib(1))) #,1)
print(str(fib(2))) #,1)
print(str(fib(3))) #,2)
print(str(fib(4))) #,3)
print(str(fib(5))) #,5)
print(str(fib(1000))) #,
print(str(fib(-5))) #,
print(str(fib(2000000))) #,
# 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875)
# 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875

# def fib(n):
#   if n < 0: return (-1)**(n % 2 + 1) * fib(-n)
#   a = b = x = 1
#   c = y = 0
#   while n:
#     if n % 2 == 0:
#       (a, b, c) = (a * a + b * b,
#                    a * b + b * c,
#                    b * b + c * c)
#       n /= 2
#     else:
#       (x, y) = (a * x + b * y,
#                 b * x + c * y)
#       n -= 1
#   return y

# from numpy import matrix
#
# def fib(n):
#     return (matrix(
#         '0 1; 1 1' if n >= 0 else '-1 1; 1 0', object
#         ) ** abs(n))[0, 1]

# import gmpy2
#
# def fib(n):
#     return gmpy2.fib(abs(n)) * (-1 if n < 0 and n % 2 == 0 else 1)