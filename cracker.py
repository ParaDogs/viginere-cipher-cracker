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

def merge_index(collention1, collention2):
    sum = 0
    n1 = len(collention1)
    n2 = len(collention2)
    if n1*n2 == 0: return 0
    for char in set(collention1+collention2):
        f1 = collention1.count(char)
        f2 = collention2.count(char)
        sum += f1*f2
    return sum/(n1*n2)

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
    patterns_repeats = repeats(text)
    pattern_size_IC = []
    for pattern in patterns_repeats:
        d = gcd_list(distances(text, pattern))
        sizes = divisors(d)
        sizes = [_ for _ in sizes if _ != 1]
        if sizes:
            size_IC = dict()
            for size in sizes:
                t = table(text, size)
                ICs = []
                for index in range(len(t[0])):
                    ICs += [coincidence_index(column(t, index))]
                size_IC[size] = avg(ICs)
            pattern_size_IC += [min(size_IC.items(),key=lambda x: abs(lang.IC - x[1]))]
    most_common_size = 0
    max_count = 0
    for _ in pattern_size_IC:
        if pattern_size_IC.count(_) > max_count:
            max_count = pattern_size_IC.count(_)
            most_common_size = _[0] 
    return most_common_size

def keys(text, key_len, lang):
    if key_len == None:
        key_len = key_lenght(text, lang)
    t = table(text, key_len)
    columns = [column(t, i) for i in range(key_len)]
    shifts = []
    for col in columns[1:]:
        shift_MI = dict()
        for shift in range(len(lang.alphabet)):
            shifted_col = string_shift(col,shift,lang.alphabet)
            shift_MI[shift] = merge_index(columns[0],shifted_col)
        for sm in shift_MI.items():
            if lang.MIC_min <= sm[1] <= lang.MIC_max:
                shifts += [sm[0]]
                break
    keys = []
    for char in lang.alphabet:
        key = char
        for shift in shifts:
            key += lang.alphabet[(lang.alphabet.find(char)-shift)%len(lang.alphabet)]
        keys += [key]
    return keys

def encrypt(text, key, lang:Language):
    result = ''
    a = lang.alphabet
    for i in range(len(text)):
        result += a[(a.find(text[i]) + a.find(key[i%len(key)])) % len(a)]
    return result

def encrypt(text, key, alphabet):
    result = ''
    a = alphabet
    for i in range(len(text)):
        result += a[(a.find(text[i]) + a.find(key[i%len(key)])) % len(a)]
    return result

def decrypt(text, key, lang):
    result = ''
    a = lang.alphabet
    for i in range(len(text)):
        result += a[(a.find(text[i]) - a.find(key[i%len(key)])) % len(a)]
    return result

def decrypt_all(text, keys, lang):
    if keys == None or keys == []:
        keys = keys(text,key_lenght(text,lang),lang)
    result = []
    for key in keys:
        result += [decrypt(text, key, lang)]
    return result
