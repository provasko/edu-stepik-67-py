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
