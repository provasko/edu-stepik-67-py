from re import X


a = 5
while a > 0:
    print(a, end=' ')
    a -= 1

# Какое значение будет у переменной i после выполнения фрагмента программы?
i = 0
while i <= 10:
    i = i + 1
    if i > 7:
        i = i + 2

# 13

# Сколько итераций цикла будет выполнено в этом фрагменте программы?
i = 0
while i <= 10:
    i = i + 1
    if i > 7:
        i = i + 2

# 9

# Нарисовать треугольник от 1 до 5 звездочек
c = 1
while c <= 5:
    print('*' * c)
    c += 1

n = int(input())
stars = '*'
while len(stars) <= n:
    print(stars)
    stars += '*'

# Вычислить сумму целых чисел от х до у
s = 0
i = x
while i <= y:
    s += i
    i += 1
print(s)

# breal - оператор завершения цикла, continue - переход к следующей итерации цикла

# какое значение будет иметь переменная i после выполнения следующего фрагмента программы:
i = 0
s = 0
while i < 10:
    i = i + 1
    s = s + i
    if s > 15:
        break
    i = i + 1

# 7

i = 0
s = 0
while i < 10:
    i = i + 1
    s = s + i
    if s > 15:
        continue
    i = i + 1

# 10

'''
Напишите программу, которая считывает целые числа с консоли по одному числу в строке.

Для каждого введённого числа проверить:
если число меньше 10, то пропускаем это число;
если число больше 100, то прекращаем считывать числа;
в остальных случаях вывести это число обратно на консоль в отдельной строке.
'''
a = 0
while a <= 100:
    a = int(input())
    if a < 10:
        continue
    if a > 100:
        break
    print(a)
