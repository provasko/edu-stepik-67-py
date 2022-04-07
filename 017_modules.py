# Модули

# Содержит функции и данные в отдельном файле. Объекты из модуля можно импортировать в другие модули
# Имя файла = имя модуля + .py

# Импорт модуля  

# Рассмотрим файл my_module.py. Пусть в нем описана функция foo()
from asyncio import subprocess
import my_module
my_module.foo()

# Импорт from

from my_module import foo
foo()

from my module import *
foo()

from my_module import foo as my_foo
my_foo()

# стандартные модули docs.python.org/3/library/ 
# docs.python.org/3/tutorial/modules.html 
# ibm.com/developerworks/ru/library/l-python_part_5/

# Аргументы командной строки
# Модуль sys
import sys
print(len(sys.argv))

# Запуск внешних процессов
# Модуль subprocess

subprocess.call(["python", "-h"])
