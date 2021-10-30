import math as maths

def ctdfrac(num, L=10): # 5 lines
    digits = list()
    for _ in range(L):
        digits.append(int(num))
        num = 1/(num-int(num))
    return digits

def irrappx(seq): # 4 lines
    appx = seq[-1]
    for i in range(len(seq)):
        appx = 1/appx + seq[len(seq)-i-1]
    return appx

def lenseq(num, tol=10): # 4 lines
    L = 1
    while abs(num-irrappx(ctdfrac(num,L)))>10**(-tol):
        L += 1
    return L

def entire(num, tol=10): # 6 lines
    L = lenseq(num, tol)
    seq = ctdfrac(num, L)
    print("Running method for num",num,"tolerance",tol)
    print("Length of continued fraction:",L)
    print("Sequence of continued fraction:",seq)
    print("Approximation arrived is",irrappx(seq))

entire(maths.pi)