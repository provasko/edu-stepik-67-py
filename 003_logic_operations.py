from math import fabs


a = True
b = False
print(a or b)
print(a and b)
print(not a)

a = 5 < 7
b = 6 >= 1
c = a == b
d = c != b
print(c and d)

# например проверка на положительное
m = int(input())
print(m > 0)

# проверка на двузначность
n = int(input())
print(n >= 10 and n < 100)

x1, x2, x3 = False, True, False
print(not x1 or x2 and x3)
# будет вычисляться в порядке not - and - or

print(((not x1) or x2) and x3)
# будет вычисляться в прямом порядке написания
