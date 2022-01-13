def repeats(text, min_pattern_length=3):
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

def table(collection, width):
    assert width > 0
    result = []
    row = []
    for _ in collection:
        if len(row) == width-1:
            row += [_]
            result += [row]
            row = []
        else:
            row += [_]
    if row != []:
        result += [row]
        row = []
    return result

def column(table, index):
    assert index < len(table[0])
    result = []
    for i in range(len(table)):
        for j in range(len(table[i])):
            if j == index:
                result += [table[i][j]]
    return result

def string_shift(collection, shift, alphabet):
    result = []
    for _ in collection:
        result += [alphabet[(alphabet.find(_)+shift)%len(alphabet)]]
    return result
    