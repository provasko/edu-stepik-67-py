'''
Напишите программу, которая принимает на стандартный вход список игр футбольных команд 
с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число 
n
n — количество завершенных игр.
После этого идет 
n
n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.
'''

'''
В какой-то момент в Институте биоинформатики биологи перестали понимать, что говорят информатики: 
они говорили каким-то странным набором звуков.

В какой-то момент один из биологов раскрыл секрет информатиков: они использовали при общении 
подстановочный шифр, т.е. заменяли каждый символ исходного сообщения на соответствующий ему другой символ. 
Биологи раздобыли ключ к шифру и теперь нуждаются в помощи:

Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на 
вход две строки одинаковой длины, на первой строке записаны символы исходного алфавита, на второй 
строке — символы конечного алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом, 
и ещё одна строка, которую нужно расшифровать.

Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%

Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, 
c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. 
Получаем следующие строки, которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac
'''

'''
Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".

Попробуем написать подобную систему.

На вход программе первой строкой передаётся количество 
d
d известных нам слов, после чего на 
d
d строках указываются эти слова. Затем передаётся количество 
l
l строк текста для проверки, после чего 
l
l строк текста.

Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.
'''

'''
Группа биологов в институте биоинформатики завела себе черепашку.

После дрессировки черепашка научилась понимать и запоминать указания биологов следующего вида:
север 10
запад 20
юг 30
восток 40
где первое слово — это направление, в котором должна двигаться черепашка, а число после слова — 
это положительное расстояние в сантиметрах, которое должна пройти черепашка.

Но команды даются быстро, а черепашка ползёт медленно, и программисты догадались, что можно написать 
программу, которая определит, куда в итоге биологи приведут черепашку. Для этого программисты просят 
вас написать программу, которая выведет точку, в которой окажется черепашка после всех команд. 
Для простоты они решили считать, что движение начинается в точке (0, 0), и движение на восток 
увеличивает первую координату, а на север — вторую.

Программе подаётся на вход число команд 
n
n, которые нужно выполнить черепашке, после чего 
n
n строк с самими командами. Вывести нужно два числа в одну строку: первую и вторую координату конечной 
точки черепашки. Все координаты целочисленные.
'''

'''
Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.

Напишите программу, которая прочитает этот файл и подсчитает для каждого класса средний рост учащегося.

Файл состоит из набора строк, каждая из которых представляет собой три поля:
Класс Фамилия Рост

Класс обозначается только числом. Буквенные модификаторы не используются. Номер класса может быть 
от 1 до 11 включительно. В фамилии нет пробелов, а в качестве роста используется натуральное число, 
но при подсчёте среднего требуется вычислить значение в виде вещественного числа.

Выводить информацию о среднем росте следует в порядке возрастания номера класса (для классов 
с первого по одиннадцатый). Если про какой-то класс нет информации, необходимо вывести напротив 
него прочерк.

В качестве ответа прикрепите файл с полученными данными о среднем росте.
'''