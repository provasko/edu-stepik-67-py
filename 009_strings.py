genome = "ATGG"

print(genome[2])
print(genome[-3])
for i in range(4):
    print(genome[i], end="  ")

for c in genome:
    print(c)

# подсчет куска строки / символов

cnt = 0
for j in genome:
    if j == "G":
        cnt += 1
print(cnt)

print(genome.count("G"))

# var="Hello!"
# var[0] -> 'H' - только первый символ
# var[1:] -> 'ello!' - все символы начиная со второго
# var[:3] -> 'Hell' - все символы до четвертого
# var[1:4] -> 'ello' - символы со второго по пятый
# var[::] -> 'Hello!' - выведутся все символы
# var[::2] -> 'Hlo' - здесь выбирается каджый второй символ строки, т.е. 0й 2й и 4й
# var[::-1] -> '!olleH' - выведутся все символы, но с шагом - 1 - каждый символ, но в обратном порядке.

# Методы для строк

s = "aTGcc"
p = "cc"

s.upper()  # "ATGCC"
s.lower()  # "atgcc"
s.count(p)  # 1 (количество вхождений)
s.find(p)  # 3 (индекс первого вхождения)
s.find("A")  # -1 (не встречается)
s.replace("c", "T")  # "aTGTT"

# Последовательные методы
o = "agTtcAGtc"
print(o.upper().count("gt".upper()))

cg = input()
cg_count = (cg.count("c") + cg.count("g"))/len(cg)

# Slicing
dna = "ATTCGGAGCT"
print(dna[1] + " - JUST 2ND")
print(dna[1:4] + " - FROM 2ND TO 5TH")
print("TO 5 TH: " + dna[:4] + " , AND FROM 5TH: " + dna[4:])
print(dna[-4:] + " - FRMOM 4TH AT THE END")
print(dna[1:-1] + " - FROM 2ND TO 2ND FROM THE END OR " +
      dna[1:-1:2] + " - THE SAME BUT WITH STEP 2")
print(dna[::-1] + " - MIRROR")

# Проверка на палиндром
palindrom = input()
for i in range(len(palindrom) // 2 + 1):
    if palindrom[i] != palindrom[-i]:
        print("NO")
        break
    else:
        print("YES")

# FAILED!!! Correct:

pali = input()
i = 0
j = len(pali) - 1
is_pali = True
while i < j:
    if pali[i] != pali[j]:
        is_pali = False
    i += 1
    j -= 1
if is_pali:
    print("YES")
else:
    print("NO")
