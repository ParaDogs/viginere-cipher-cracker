# vigenere cipher cracker
from languages import *
from utils import *
from aripthmetic import *

def coincidence_index(collection):
    sum = 0
    n = len(collection)
    if n*(n-1) == 0: return 0
    for char in set(collection):
        c = collection.count(char) 
        sum += c*(c-1)
    return sum/(n*(n-1))

def priority(patterns_repeats):
    priority = sorted(list(patterns_repeats.items()),key=lambda x: len(x[0]),reverse=True)
    priority = sorted(priority,key=lambda x: x[1],reverse=True)
    return [_[0] for _ in priority]

def distances(text, pattern):
    possitions = []
    start = 0
    while start < len(text):
        pos = text.find(pattern,start) 
        if pos > -1:
            possitions += [pos]
            start = pos + len(pattern) + 1
        else: break
    result = []
    for i in range(len(possitions)-1):
        result += [possitions[i+1]-possitions[i]]
    return result

def key_lenght(text, lang):
    # refactor this code
    patterns_repeats = repeats(text)
    patterns_priority = priority(patterns_repeats)
    # patterns_priority = patterns_repeats
    # print(patterns_priority)

    pattern_size_IC = []
    for pattern in patterns_priority:
        d = gcd_list(distances(text, pattern))
        sizes = sorted(divisors(d),reverse=True)
        for _ in sizes:
            if _ == 1:
                sizes.remove(_)
        if sizes:
            size_IC = dict()
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

                ICs = []
                for index in range(len(table[0])):
                    ICs += [coincidence_index(column(table, index))]
                size_IC[size] = avg(ICs)
            pattern_size_IC += [min(size_IC.items(),key=lambda x: abs(lang.IC_max - x[1]))]
    tmp = sorted(pattern_size_IC,key=lambda x: abs(lang.IC_max - x[1]))
    size_priority = []
    most_common_size = 0
    max_count = 0
    for _ in tmp:
        if tmp.count(_) > max_count:
            max_count = tmp.count(_)
            most_common_size = _[0] 
        if _[0] not in size_priority:
            size_priority += [_[0]]
    # print(size_priority)
    # print(most_common_size)

    return most_common_size



file = open('input.txt', 'r', encoding='utf8')
text = file.read().lower()
print(key_lenght(text, RU))

