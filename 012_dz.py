# Поиск минимума в списке

a = [int(i) for i in input().split()]
m = a[0]
for x in a:
    if m > x:
        m = x

# Сапер
n, m, k = (int(i) for i in input().split())
a = [[0 for j in range(m)] for i in range(n)]
for i in range(k):
    row, col = (int(i) for i in input().split())
    a[row][col] = -1
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = i + di
                    aj = j + dj

                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
                        a[i][j] += 1

for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            print("*", end=" ")
        elif a[i][j] == 0:
            print(".", end=" ")
        else:
            print(a[i][j], end=" ")
    print()

# Напишите программу, которая считывает с консоли числа (по одному в строке) до тех пор,
# пока сумма введённых чисел не будет равна 0 и сразу после этого выводит сумму квадратов всех считанных чисел.

u = int(input())
che = 0
summ = 0
che += u
summ += u * u

while che != 0:
    u = int(input())
    che += u
    summ += u * u
print(summ)

# alternative
a = int(input())
check = 0
summ = 0
while a != 'z':
    summ += a * a
    check += a
    a = int(input())
    if check == 0:
        print(summ)
        break

# Напишите программу, которая считывает список чисел lst из первой строки и число
# x из второй строки, которая выводит все позиции, на которых встречается число
# x в переданном списке lst.
# Позиции нумеруются с нуля, если число x не встречается в списке, вывести строку "Отсутствует"
# Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.

spis = [int(i) for i in input().split()]
b = int(input())
nomera = 0
for j in range(len(spis)):
    if spis[j] == b:
        print(j, end=" ")
        nomera += 1
if nomera == 0:
    print("Отсутствует")
