# *** loops Циклы (операторы циклов) ***

# *** Оператор цикла while ***

num = 0

# while num < 10:
#     print(num)
#     num += 1 # num = num + 1

# *** Прерывание цикла ***

# while num <= 10:
#     print(num)
#     num += 1

#     if num == 5: # если значение num станет равной 5
#         break # то прерываем цикл, вызвав инструкцию (команду) break

# while True:
#     s = input("Введите команду: ")

#     print(f"Вы ввели команду: {s}")

#     if s == "стоп":
#         break

# *** Пропуск куска кода

# while True:
#     s = input("Введите слово 'ДА': ")

#     if s != "ДА":
#         print("Вы не ввели слово 'ДА'!!! :((")
#         continue # чтобы вернуть цикл в самое начало

#     print(f"Молодец! Ты ввел команду: {s}")
#     break

# *** Оператор цикло for ***

# 1. читает значения элемента какого-либо итерируемого объекта
# 2. присваивает это значение в свою переменную
# 3. выполняет блок кода своего тела
# for number in [10,20,30,40,50]:
#     print(number)


# my_list = []
# my_tuple = (1,2,3,4,5)
# for i in my_tuple:
#     i *= 100
#     my_list.append(i)

# print(my_list)

# для автоматического создания словаря
# my_dict = {}
# for idx in range(5, 20, 2):
#     my_dict[idx] = idx * 10
#     if idx == 11:
#         break

# print(my_dict)

# *** генератор списка ***

# my_list = [num  for num in range(10)]
# my_list = [num ** 2 for num in range(10)]

my_list = [num  ** 2 for num in range(10) if num > 3]

# print(my_list)

# *** enumerate()***

data = ['a', 'b', 'c', 'd']

# print(list(enumerate(data)))

# for index, item in enumerate(data):
    # print(index, item)

# *** Генератор словаря ***

# my_dict = {i : i for i in ['A', 'B', 'c', 'd'] }

my_dict = {item.upper() : index * 10 for index, item in enumerate(data) if index > 0}

# print(my_dict)

# *** Калькулятор с циклами ***

while True:
    # ввод чисел
    num_list = []
    for n in range(2):
        num = int(input(f"Введите {n} число: "))
        num_list.append(num)

    # ввод команды
    while True:
        cmd = input("Введите команду: ")
        if cmd not in ("stop", "+", "-", "*", "/"):
            print("Вы ввели неправильную команду!!! :((")
            continue
        else:
            break
    # Обработка выключения
    if cmd == "stop":
        print("До свидания")
        break
    # вычисление
    if cmd == "+":
        res = num_list[0] + num_list[1]
    
    elif cmd == "-":
        res = num_list[0] - num_list[1]

    elif cmd == "*":
        res = num_list[0] * num_list[1]
    
    elif cmd == "/":
        res = num_list[0] / num_list[1]
    
    if float is type(res):
    # res = float(res)
    # вывод результата

        print(f"Результат: {res:.4f}")

    else:
        print(f"Результат: {res:.4f}")
