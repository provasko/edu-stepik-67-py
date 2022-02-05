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
