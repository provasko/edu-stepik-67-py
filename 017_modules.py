# Модули

# Содержит функции и данные в отдельном файле. Объекты из модуля можно импортировать в другие модули
# Имя файла = имя модуля + .py

# Импорт модуля

# Рассмотрим файл my_module.py. Пусть в нем описана функция foo()
import sys
from my_module import foo as my_foo
from my module import *
from my_module import foo
from asyncio import subprocess
import my_module
my_module.foo()

# Импорт from

foo()

foo()

my_foo()

# стандартные модули docs.python.org/3/library/
# docs.python.org/3/tutorial/modules.html
# ibm.com/developerworks/ru/library/l-python_part_5/

# Аргументы командной строки
# Модуль sys
print(len(sys.argv))

# Запуск внешних процессов
# Модуль subprocess

subprocess.call(["python", "-h"])

# Напишите программу, которая подключает модуль math и, используя значение числа π из этого модуля,
# находит для переданного ей на стандартный ввод радиуса круга периметр этого круга и выводит его
# на стандартный вывод.


# Напишите программу, которая запускается из консоли и печатает значения всех переданных аргументов
# на экран(имя скрипта выводить не нужно). Не изменяйте порядок аргументов при выводе.

# Для доступа к аргументам командной строки программы подключите модуль sys и используйте переменную
# argv из этого модуля.

# Пример работы программы:
# python3 my_solution.py arg1 arg2
# arg1 arg2
