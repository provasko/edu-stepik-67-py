# Sets

s = set()  # Создание пустого множества
basket = {"apple", "orange", "apple", "pear", "orange", "banana"}

print(basket)  # выводит в другом порядке без повторений

"orange" in basket  # True
"cucumber" in basket  # False

basket.add("kiwi")  # Добавляет элемент

basket.remove("orange")  # Удаляет элемент, но если такого нет - ошибка!

basket.discard("grape")  # Тоже удаление, но несовпадение не вызовет ошибку

basket.clear()  # Удаляет все элементы из множества
