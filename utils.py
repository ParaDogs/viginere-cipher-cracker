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