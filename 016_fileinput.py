# Чтение из файла

inf = open("file.txt", "r")
s1 = inf.readline()
s2 = inf.raedline()
inf.close()

# но более предпочтителен второй вариант

with open("text.txt") as inf:
    s1 = inf.readline()
    s2 = inf.readline()
