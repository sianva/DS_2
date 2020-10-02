# *** Словарь (dictionary) ***
#
# пары "ключ:значение"
my_dict = {10:555, 1:100, 2:700, "A":3.14, 'abc':[1,2,3]}
# список списков
# a = [
#     ['A',1000],
#     ['B', 2000]
# ]

a = [['A',1000], ['B', 2000]]

my_dict_2 = dict(a)

# print(my_dict_2)

# чтение данных

# item = my_dict["abc"]
item = my_dict[10]
# print(item)

# изменение значения
# my_dict[10] = 777

# удаление значения
# del my_dict[2]

# добавление нового элемента
my_dict["hello"] = 1000

# *** проблемы с чтением значения
d = {"key_1":100, "key_2":300}

k = "key_3"
# val = d["key_3"]
# val = d[10]

# первый вариант решения использваоние условынх операторов
# if k in d:
#     val = d[k]
# else:
#     val = "такого ключа нет"

# второй вариант решения применение встроенного
# val = d.get(k) # None - ключевое слово пустота для безопасной работы с ключами в словарях

val = d.get(k, "пусто") # по русски, любое слово можно писать или без кавычек 0 вместо None

# *** проблемы при удалении по несуществующему ключу ***

# del d[k]
k = "key_1"
# решение этой проблемы
val = d.pop(k, None) # метод удаляет элемент если ключ существует и при этом значения можно присвоить переменной вместо None можно всякое в кавычках писать
# print(val, d)

# обновление значений
d_1 = {"key_1":100, "key_2":300}

d_2 = {"key_1":777, "key_3":200}

d_1.update(d_2)

d_1.

print(d_1)