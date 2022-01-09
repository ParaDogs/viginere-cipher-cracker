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

def column(table, index):
    assert index < len(table[0])
    result = []
    for i in range(len(table)):
        for j in range(len(table[i])):
            if j == index:
                result += [table[i][j]]
    return result

def avg(collection):
    assert len(collection) != 0
    result = 0
    for _ in collection:
        result += _
    return result/len(collection)