# Sets

s = set()  # Создание пустого множества
basket = {"apple", "orange", "apple", "pear", "orange", "banana"}

print(basket)  # выводит в другом порядке без повторений

"orange" in basket  # True
"cucumber" in basket  # False

for fruit in basket:
    print(fruit)

basket.add("kiwi")  # Добавляет элемент

basket.remove("orange")  # Удаляет элемент, но если такого нет - ошибка!

basket.discard("grape")  # Тоже удаление, но несовпадение не вызовет ошибку

basket.clear()  # Удаляет все элементы из множества


# СЛОВАРИ

# создание пустого

dict()
d = {}

# непустого

autonomer = {"a001mp77": "ment", "e001kx77": "fsb"}

# Операции со словорями
# поиск - выводит значения True / False
"a001mp77" in autonomer
"x005xx77" not in autonomer
autonomer["e001re77"] = "edro"
print(autonomer["a001mp77"])

# autonomer["x005xx77"] выдаст ошибку! чтобы ошибки не было:

print(autonomer.get("x005xx77"))  # None

del autonomer["e001kx77"]

# Словари изменяемы
# Элементы не имеют порядка
# Все ключи различны
# Ключи не изменяемы

# Перебор элементов списка

nabor = {"C": 14, "A": 12, "T": 9, "G": 18}

for key in nabor:
    print(key, end=" ")
for key in nabor.keys():
    print(key*2, end=" ")
for value in nabor.values():
    print(value//2, end=" ")
for key, value in nabor.items():
    print(key, value, end="; ")

# В значениях (НЕ ключах) могут храниться списки

crnagora = {"Bar": ["Bjelisi", "Susanj"], "Budva": [
    "Lazi", "Maine"], "Podgorica": "Konik"}
print(crnagora["Budva"])
