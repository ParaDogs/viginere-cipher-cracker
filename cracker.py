# vigenere cipher cracker
from math import sqrt

I_english = 0.0662
i_english = 0.038

I_russian = 0.0529
i_russian = 0.03

# alphabets
alphabets = {
    'EN_'   : "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ",
    'EN'    : "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    'RU*_'  : "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ ",
    'RU*'   : "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
    'RU_'   : "абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ ",
    'RU'    : "абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
}

def repeats_inside(text, min_pattern_length=3):
    n = len(text)
    m = min_pattern_length
    res = dict()
    for left in range(n-min_pattern_length):
        for right in range(left+m,n):
            pattern = text[left:right]
            repeats = text.count(pattern)
            if repeats > 1:
                res[pattern] = repeats
    return res

# all divisors of number
def divisors(n):
    res = [n]
    border = int(sqrt(n)) + 1
    d = 2
    while d <= border:
        if n%d == 0:
            res += [d,n//d]
        d += 1
    return set(res)

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

# kasiski test
def key_length(cipher, alphabet):
    pass

def coincidence_index(str):
    sum = 0
    m = len(str)
    for char in str:
        c = str.count(char) 
        sum += c*(c-1)
    return sum/(m*(m-1))

# refactor this code
# text = 'abcdthisisatextwithsampletextforasampleabcde'
text = 'GHQTJBSQRLNTUSFVSQPWZEZXSEYMRVGHQXGCIOWSEEURLRRQWEVNSXGAOZWHRCUEDVSFWLUEFLWBRKMKDUUXWOEMYLVFGPSADPINRLATAAGDEHVDQC'
# text = 'aaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaa'
priority = sorted(list(repeats_inside(text).items()),key=lambda x: len(x[0]),reverse=True)
# max_pattern = max(priority,key=lambda x:x[1])[0]
max_pattern = priority[0][0]
D = []
start = 0
while start < len(text):
    pos = text.find(max_pattern,start) 
    if pos > -1:
        D += [pos]
    start += pos + len(max_pattern)

distances = []
for i in range(len(D)-1):
    distances += [D[i+1]-D[i]]
d = gcd_list(distances)

print(max_pattern)
print(distances) 
print(d)
print(sorted(divisors(d),reverse=True))

table = []
row = []
for char in text:
    if len(row) == 2:
        table += [row]
        row = []
    else:
        row += [char]
if row != []:
    table += [row]

for _ in table:
    print(*_)

print(coincidence_index([e[0] for e in table]))
