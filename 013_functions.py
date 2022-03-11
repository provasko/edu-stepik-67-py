def min2(a, b):
    if a <= b:
        return a
    else:
        return b

# could be used twice
m = min2(42, 30)
mm = min2(min2(43, 78), 31)
