# логические операторы

x = 3
y = 3

res = x != y # оператор "не равно"

res = x == y # оператор проверки на равенство "равно"

res = x < y # оператор "меньше"

res = x >= y # оператор "больше либо равно"

# print(f"\nРезультат: {res}")


z = True
k = False

# print( not k ) # оператор НЕ (инвертирующий оператор)

# print( z and k ) # оператор "и"

# print( z or k ) # оператор "или"

condition = z and (z or k)

# print(condition)


# условные операторы

a = 3

if a >= 5:
    c = "больше или равно 5"
elif a == 4:
    c = "равно 4"
elif a == 3:
    c = "равно 3"
else:
    c = "не равно 5"

# print(c)


b = 9

# if b > 0 and b < 10:
#     print("Лампочка вкл")
# else:
#     print("Лампочка выкл")


# ***** Простенький калькулятор *****

num_1 = int(input("Введите первое целое число: "))
num_2 = int(input("Введите второе целое число: "))

operation = input("Введите символ операции (+, -, *, /): ")

if operation == "+":
    res = num_1 + num_2
elif operation == "-":
    res = num_1 - num_2
elif operation == "*":
    res = num_1 * num_2
elif operation == "/":
    res = num_1 / num_2
else:
    res = "Введенный символ некорректный!!!"

print(f"Результат: {res}")

