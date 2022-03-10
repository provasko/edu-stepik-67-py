# Двухмерные списки
# from tkinter import N


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(a[1])
print(a[1][1])
print(a[0][2])

# Генерация

n = int(input())

b = [[0] * n] * n

c = [[0] * n for i in range(n)]
d = [[0 for j in range(n)] for i in range(n)]
