# vigenere cipher cracker
from languages import *
from utils import *
from aripthmetic import *

# kasiski test
def key_length(cipher, alphabet):
    pass

def coincidence_index(str):
    sum = 0
    n = len(str)
    for char in str:
        c = str.count(char) 
        sum += c*(c-1)
    return sum/(n*(n-1))

# refactor this code
text = 'abcdthisisatextwithsampletextforasampleabcde'
tmp = repeats(text)
print(tmp)
priority = sorted(list(tmp.items()),key=lambda x: x[1],reverse=True)
# max_pattern = max(priority,key=lambda x:x[1])[0]
max_pattern = priority[0][0]
D = []
start = 0
while start < len(text):
    pos = text.find(max_pattern,start) 
    if pos > -1:
        D += [pos]
    else:
        break
    start = pos + len(max_pattern) + 1
print(D)

distances = []
for i in range(len(D)-1):
    distances += [D[i+1]-D[i]]
d = gcd_list(distances)

print(max_pattern)
print(distances) 
print(d)
sizes = sorted(divisors(d),reverse=True)
print(sizes)

for size in sizes:
    table = []
    row = []
    for char in text:
        if len(row) == size:
            table += [row]
            row = []
        else:
            row += [char]
    if row != []:
        table += [row]

    # for _ in table:
    #     print(*_)

    print(coincidence_index([e[0] for e in table]), 'длина ключа', size)
