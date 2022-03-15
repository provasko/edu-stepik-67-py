# объявление функции
def min2(a, b):
    if a <= b:
        return a
    else:
        return b


# вызов функции
# could be used twice
m = min2(42, 30)
mm = min2(min2(43, 78), 31)

#


def f(n):
    return n * 10 + 5


print(f(f(f(10))))

# Произвольное число параметров


def min(*a):
    m = a[0]
    for x in a:
        if m > x:
            m = x
    return m

# Значение параметров по умолчанию

def my_range(start, stop, step=1):
    res = []
    if step > 0:
        x = start
        while x < stop:
            res += [x]
            x += step
    elif step < 0:
        x = start
        while x > stop:
            res += [x]
            x += step
    return res

