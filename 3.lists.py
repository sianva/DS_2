# **** Списки (lists) ****


# Создание пустого списка

my_list = []
my_list_2 = list()

# метод append

my_list.append(100)
my_list.append(200)
my_list.append("hello")
my_list.append([1,2,3])

# Создание заполненных списков

my_list = [10, 20, 30, 40, "A", 3.14, True]

s = "Привет, Мир!"
list_1 = list(s)

# *** функция range() ***

numbers = list( range(10) ) # создается набор чисел от 0 до 10 не включительно
numbers = list( range(2, 10) ) # создается набор чисел от 2 до 10 не включительно
numbers = list( range(2, 10, 2) ) # создается набор чисел от 2 до 10 не включительно, с шагом 2
numbers = list( range(10, 1, -1) ) # создается набор чисел от 10 до 1 не включительно, в обратном направлении

# *** Методы списков ***

# добавление элемента по индексу

a = [10, 30, 60, 80, 50, 30, 30]
a.insert(0, "A")

# объект.метод()

# удаление элемента по значению
# a.remove(30)

# удаление или очистка списка
# print(a)
# a.clear()

# сортировка списка
b = [8,4,1,6,7,8,9,2,35]
b.sort() # по возрастанию
b.sort(reverse=True) # в сторону убывания


# Обращение к элементам

c = [1,2,3,4,5]

# print( c[0] ) # чтение значения элемента

# del c[1] # способ удаления элемента по индексу

# c[3] = 10 # замена значения элемента по индексу

# c[-1] = 10 #  замена элемента через обратн индекс

# print(len(c)) #len возвращает показывает длину списков массивов и прочее

# *** Срезы (slice)***

c = c + [6,7,8,9,10,11]

c_slice = c[0:3] # срез с 0 по 3 индекс не включительно
c_slice = c[:3] # срез с 0 по 3 индекс не включительно
c_slice = c[1:4] # срез с 1 по 4 индекс не включительно
c_slice = c[1:8:2] # срез с 1 по 8 индекс не включительно с шагом 2

c_slice = c[::2] # срез с шагом 2

c_slice = c[-1:-4:-1] # срез списка с обратынм порядком, поворот списка с удалением части

print(c_slice)