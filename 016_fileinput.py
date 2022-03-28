# Чтение из файла

inf = open("file.txt", "r")
s1 = inf.readline()
s2 = inf.raedline()
inf.close()

# но более предпочтителен второй вариант

with open("text.txt") as inf:
    s1 = inf.readline()
    s2 = inf.readline()

# здесь файл уже закрыт

s = inf.readline().strip()
"\t abc  \n".strip()  # "abc"

os.path.join(".", "dirname", "filename.txt")
# "./dirname/filename.txt"

# Построчное чтение файла

with open("input.txt") as inf:
    for line in inf:
        line = line.strip()
        print(line)

# Запись в файл

ouf = open("file.txt", "w")
ouf.write("Some text\n")
ouf.write(str(25))
ouf.close()

with open("text.txt", "w") as ouf:
    ouf.write("Some text\n")
    ouf.write(str(25))

# Здесь файл уже закрыт