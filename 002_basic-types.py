# целые числа - int
# вещественные числа - float
# логические - bool
# строки - str
from re import M


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

# Коля каждый день ложится спать ровно в полночь и недавно узнал, что оптимальное время для его сна составляет X минут.
# Коля хочет поставить себе будильник так, чтобы он прозвенел ровно через X минут после полуночи,
# однако для этого необходимо указать время сигнала в формате часы, минуты. Помогите Коле определить, на какое время завести будильник.
z = int(input())
chas = z // 60
minut = z % 60
print(chas, minut)

# то же задание, но спать ложится не в полночь а h:m
h = int(input())
m = int(input())
absol = h*60 + m + z
chas2 = absol // 60
minut2 = absol % 60
