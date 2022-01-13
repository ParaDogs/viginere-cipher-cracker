from math import sqrt

# all divisors of number
def divisors(n):
    res = [n]
    border = int(sqrt(n)) + 1
    d = 1
    while d <= border:
        if n%d == 0:
            res += [d,n//d]
        d += 1
    return list(set(res))

# greatest common divisor
def gcd(a, b):
    if a == 0 or b == 0: 
         return max(a, b)
    if a > b:
        return gcd(a%b, b)
    return gcd(b%a, a)

def gcd_list(a):
    assert len(a) != 0
    if len(a) == 1:
        return a[0]
    if len(a) == 2:
        return gcd(*a)
    return gcd(a[0],gcd_list(a[1:]))

def avg(collection):
    return sum(collection)/len(collection)
