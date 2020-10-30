# **** Работа с файлами ****

# *** Создание файла и запись в этот файл ***
#  Контекстный менеджер with
# режимы функции open:
# w - write (запись)
# a - append (добавление)
# r -read (чтение)
# \n - символ каретки
# with open("hello.txt", "w") as f:
#     f.write("Hello, World!\n")
#     f.write("hello, Python\n")


# *** Добавление новой записи без удаления старых
# with open("hello.txt", "a", encoding="utf8") as f:
#     f.write("Привет, Мир!\n")

# *** Чтение всего файла

# with open("hello.txt", "r", encoding="utf8") as f:
#     text = f.readline()
#     print(text)

# *** Чтение отдельных строк
# f.readline - переводит каретку (дважды получится) end=""

# with open("hello.txt", "r", encoding="utf8") as f:
#     row = f.readline()
#     print(row, end="")
#     row = f.readline()
#     print(row, end="")

#  *** Создание списка из строк файла

# with open("hello.txt", "r", encoding="utf8") as f:
#     row_list = f.readlines()
#     # print(row_list)
#     print(row_list[-1])

