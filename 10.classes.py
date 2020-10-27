# **** Основы объектно-ориентированного программирования (ООП)****

# Объекты обладают свойствами и методами
# Каждый объект принадлежит к определенному типу данных (классу)
# Класс - это абстракция объекта, "чертеж" объекта
# "Реализация" класса - это объект (экземпляр, инстанс)

#  Создание класса. Название класса приянто писать с заглавной буквы
class Cat(object):
    # метод - функция внутри класса
    def mur(self, name):
        # атрибут (свойства, поля)
        self._name = name 
        print("Мяу! Меня зовут: ", self._name)
    # метод информации
    def info(self):
        print(f"Name: {self._name}")

# Создание объекта (экземпляра) класса Cat, cat_1 это переменная
cat_1 = Cat()
cat_2 = Cat()

# # Вызов первого метода объекта
# cat_1.mur("Richard")
# cat_2.mur("Hav")

# # вызов второго метода, который использует атрибут, созданным в первом метода
# cat_1.info()


# метод-конструктор

class Dog:
    # конструктор (initialyzer)
    # нужен для каких-либо настроек или других приготовлений в момент создания объектов
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def gaf(self):
        print(f"Гав! Меня зовут {self.name}")

dog_1 = Dog("Цезарь", 10, 7.3)
dog_2 = Dog("Тузик", 5, 3.3)

# чтение значения атрибута
name_dog_1 = dog_1.name
# print(name_dog_1)
# # изменение значения атрибута
dog_1.name = "Барбос"
# print(dog_1.name)
# print(name_dog_1)

# вызов метода
# dog_1.gaf()
# dog_2.gaf()

# *** Принцип Наследования - 1-й принцип ООП ***

# родительские (предковый) класс
class Animal:
    def __init__(self, legs=0):
        self.num_legs = legs
    def move(self):
        print(f"Я двигаюсь. у меня {self.num_legs}  ног.")

# дочерние классы
class Insect(Animal):
    pass

class Wokf(Animal):
    pass

bug = Insect(8)
wolf = Wokf(4)

# bug.move()
# wolf.move()

class Human(Animal):
    def __init__(self, name, num_legs):
        self.num_legs = num_legs
        self.name = name
    def info(self):
        print(f"Я человек. Меня зовут {self.name}")
# john = Human("John", 2)
# john.move()
# john.info()

# **** Принцип полиморфизма ****
# поли + морф = разные формы чего-то одного (информационный объект)

# 1 вид. Разные классы могут обладать методами с одним имененм, но с разной функциональностью

# родительский класс
class A:
    def method_1(self, arg):
        print(f'Data: {arg}')

# дочерний класс у которого родительский метод переопределен
class A_1(A):
    def method_1(self, a, b):
        print(f"Data: {a + b}")

a = A()
a_1 = A_1()

# вызов методов у экземпляров
# a.method_1(100)
# a_1.method_1(10, 20)

# 2 вид. Применение "магических" методов (методов перегрузки операторов)

# метод, который позволяет из экземпляра (объекта) класса "делать" функцию (пеердает поведение похожее на функцию)

class CustomSum:
    def __init__(self,param):
        self.coeff = param
    
    # маг-метод, предоставляющий поведение обычной функции
    def __call__(self, a, b):
        res = (a + b) * self.coeff
        print(f"Result: {res}")
    
    # маг-метод, который возвращает строку, когда экземпляр передается функции print() 
    def __str__(self):
        return f"CustomSummator. Coeff: {self.coeff}"

sum_1 = CustomSum(0.5)
sum_2 = CustomSum(1.53)

#  эффект нашего "магического" метода
# sum_1(2, 3)
# sum_2(2, 3)

# print(sum_1)


# **** Инкапсуляция ****
# инкапсуляция - скрытие атрибутов и/или методов
# не строгая инкапсуляция
class B:
    def __init__(self, arg):
        self._atrr = arg
    
    def _method(self):
        print("Hello!")

# "строгая" инкапсуляция
    def __method_2(self):
        print("World!")
    
    # не инкапсулированный метод
    def _method_3(self):
        self.__method_2()

b = B(100)
# print(b._atrr)
# b._method()

# ctrl+shift+P
# print(b._B__atrr2)

# b._B__method_2()
# b.method_3()

# *** Композиция (Агрегация) ***

#  использование экзмепляров одних классов внутри других классов

class C:
    def __call__(self, a):
        return a ** 2
class D:
    def method(self, x):
        c = C() # создается объект класса D
        res = c(x) + x # тут он используется в качестве функции
        print(res)

d = D()
d.method(10)