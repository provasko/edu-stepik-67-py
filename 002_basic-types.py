# целые числа - int
# вещественные числа - float
# логические - bool
# строки - str
print(int(2.3))
print(float(10))

# определить тип объекта
print(type(5))

# переменные и динамическая типизация
a = 10
a = "lol"
a = True
print(type(a))

# ввод данных
b = input()
c = int(input("Enter number 1...5"))
print(b, c)

# Тимофей обычно спит ночью X часов и устраивает себе днем тихий час на Y минут.
# Определите, сколько всего минут Тимофей спит в сутки.
x = int(input("Ночной сон, часов"))
y = int(input("Дневной сон, минут"))
print(x*60 + y)
