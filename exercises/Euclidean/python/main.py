def get_nums():
    while(True):
        try:
            num1 = int(input("Please enter a positive integer: "))
            break
        except TypeError:
            pass
    while(True):
        try:
            num2 = int(input("Please enter a positive integer: "))
            break
        except TypeError:
            pass

    return [num1,num2]

def euclid_loop(x,y,prev):
    big = max(x, y)
    small = min(x, y)

    r = big % small
    return prev if r == 0 else euclid_loop(r, small, r)

def euclid(x,y):
    return euclid_loop(x,y,min(x,y))

def modular_inverse(num1,mod):
    ret = modular_inverse_loop(num1 % mod, mod, mod, 1, None, None, None, None)
    if (ret == False):
        return str(num1) + " does not have an inverse mod " + str(mod)
    else:
        return "The inverse of " + str(num1) + " mod " + str(mod) + " is " + str(ret)

# Here is a reference for the extended Euclidean algorithm
# http://www-math.ucdenver.edu/~wcherowi/courses/m5410/exeucalg.html
# q1/p1 represent the values from the previous step
# q2/p2 represent the values from two steps prior
# loopcount records the number of iterations in order to manually set the correct values for the first two loops
def modular_inverse_loop(x,y,mod,loopcount,q1,q2,p1,p2):
    big = max(x, y)
    small = min(x, y)

    q0 = int(big / small)
    r = big % small

    if (loopcount == 1):
        p0 = 0
        q1 = None
        p1 = None
    elif (loopcount == 2):
        p0 = 1
        p1 = 0
    else:
        p0 = (p2 - p1*q2) % mod

    if (r == 1):
        pnext = 1 if loopcount == 1 else (p1 - p0*q1) % mod
        return (p0 - pnext*q0) % mod
    elif (r == 0):
        return False
    else:
        return modular_inverse_loop(small,r,mod,loopcount + 1,q0,q1,p0,p1)

if __name__ == '__main__':
    print(modular_inverse(4,8))