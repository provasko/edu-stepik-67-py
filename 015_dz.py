# Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь d и два числа:
# key и value. Если ключ key есть в словаре d, то добавьте значение value в список, который хранится 
# по этому ключу. Если ключа key нет в словаре, то нужно добавить значение в список по ключу 2∗key. 
# Если и ключа 2∗key нет, то нужно добавить ключ 2∗key в словарь и сопоставить ему список из переданного
# элемента [value].

def update_dictionary(d, key, value):
    a = key
    b = value
    for key in d.keys():
        if key == a:
            d[key].append(b)
        else:
            if 2*a in d:
                d[2*a].append(b)
            else:
                d[2*a] = b

