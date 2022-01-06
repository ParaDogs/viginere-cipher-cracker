# vigenere cipher cracker
from languages import *
from utils import *
from aripthmetic import *

def coincidence_index(str):
    sum = 0
    n = len(str)
    if n*(n-1) == 0: return 0
    for char in set(str):
        c = str.count(char) 
        sum += c*(c-1)
    return sum/(n*(n-1))

def key_lenght(text, lang):
    # refactor this code
    tmp = repeats(text)
    priority = sorted(list(tmp.items()),key=lambda x: x[1],reverse=True)
    print(priority)
    max_pattern = priority[0][0] # TODO
    D = []
    start = 0
    while start < len(text):
        pos = text.find(max_pattern,start) 
        if pos > -1:
            D += [pos]
            start = pos + len(max_pattern) + 1
        else: break

    distances = []
    for i in range(len(D)-1):
        distances += [D[i+1]-D[i]]
    d = gcd_list(distances)
    print(d)

    sizes = sorted(divisors(d),reverse=True)
    # sizes = range(1,len(text)-1,1)
    I_row = dict()
    for size in sizes:
        table = []
        row = []
        for char in text:
            if len(row) == size-1:
                row += [char]
                table += [row]
                row = []
            else:
                row += [char]
        if row != []:
            table += [row]
            row = []
        I_row[size] = coincidence_index([e[5] for e in table if len(e) > 5])
    
    I_row = sorted(list(I_row.items()),key=lambda _: abs(_[1]-lang.IC_max))
    print('index \t\t\t length')
    for _ in I_row:
        print(_[0], '\t', _[1])

file = open('input.txt', 'r', encoding='utf8')
text = file.read().lower()
key_lenght(text, EN)