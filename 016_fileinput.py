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


# Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью
# кодирования повторов, и производит обратную операцию, получая исходный текст.

# Запишите полученный текст в файл и прикрепите его, как ответ на это задание.

# В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

# Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz"
# у вас появляется ссылка "download your dataset". Используйте эту ссылку для того, чтобы загрузить
# файл со входными данными к себе на компьютер. Запустите вашу программу, используя этот файл
# в качестве входных данных. Выходной файл, который при этом у вас получится, надо отправить
# в качестве ответа на эту задачу.


# Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может
# быть не так интересно смотреть, как, например, на наиболее часто используемые.

# Напишите программу, которая считывает текст из файла(в файле может быть больше одной строки)
# и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось.
# Если таких слов несколько, вывести лексикографически первое(можно использовать оператор < для строк).

# В качестве ответа укажите вывод программы, а не саму программу.

# Слова, написанные в разных регистрах, считаются одинаковыми.


# Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк,
# где в каждой строке записана следующая информация:

# Фамилия
# Оценка_по_математике
# Оценка_по_физике
# Оценка_по_русскому_языку

# Поля внутри строки разделены точкой с запятой, оценки — целые числа.

# Напишите программу, которая считывает исходный файл с подобной структурой и для каждого абитуриента
# записывает его среднюю оценку по трём предметам на отдельной строке, соответствующей этому абитуриенту,
# в файл с ответом.

# Также вычислите средние баллы по математике, физике и русскому языку по всем абитуриентам и добавьте
# полученные значения, разделённые пробелом, последней строкой в файл с ответом.

# В качестве ответа на задание прикрепите полученный файл со средними оценками по каждому ученику
# и одной строкой со средними оценками по трём предметам.

# Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим
# образом:

print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']
