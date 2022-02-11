for i in 2, 3, 5:
    print(i * 2)

for j in range(10):
    print(j * j)

# range(5) - от 0 до 4 (не включает 5) с шагом 1
# range(2, 6) - все числа от 2 до 5 (не включает 6) с шагом 1
# range(2, 15, 4) - 2, 6, 10, 14 - от 2 до 15 с шагом 4 не включая 15
# по умолчанию старт от 0, шаг 1

# Вывести кввадрат из звездочек 5 на 5
for k in range(5):
    print('*' * 5)

# Вложенный цикл - сделать прямоугольник m на l
m = int(input())
n = int(input())
for i in range(m):
    for j in range(n):
        print('*', end='')
    print()

# создать таблицу Пифагора для отрезков [a; b] [c; d]

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(' ', end='')
for i in range(c, d + 1):
    print('\t' + str(i), end='')
print()
for j in range(a, b + 1):
    print(str(j), end='')
    for k in range(c, d + 1):
        print('\t' + str(j * k), end='')
    print()

# вывести сумму всех нечетных чисел от а до б

v, w = input().split()
v = int(v)
w = int(w)
ss = 0
for i in range(v, w + 1):
    if i % 2 == 1:
        ss += i
print(ss)

# второй вариант - идти сразу по нечетным, чтобы не перебирать их внутри цикла

if v % 2 == 0:
    v += 1
for i in range(v, w + 1, 2):
    ss += 1
print(ss)

# еще вариант записи нескольких переменных

o, p, r = (int(i) for i in input().split())
sss = 0
if o % 2 == 0:
    o += 1
for i in range(o, p + 1, 2):
    sss += i

# Напишите программу, которая считывает с клавиатуры два числа, считает и выводит на консоль
# среднее арифметическое всех чисел из отрезка [a b], которые кратны числу 3.

t, u = (int(i) for i in input().split())
su = 0
kol = 0
while t % 3 != 0:
    t += 1
for i in range(t, u + 1, 3):
    su += i
    kol += 1
print(su / kol)
