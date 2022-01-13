from cracker import *

file = open('input.txt', 'r', encoding='utf8')
text = file.read().lower()

key_len = key_lenght(text, RU)
print('KEY LENGTH =', key_len)
keys_ = keys(text, key_len, RU)

print('KEY LIST:')
print(keys_)
print('--------------')

for key in keys_:
    print('KEY =',key)
    print(decrypt(text,key,RU))
    print('--------------')
