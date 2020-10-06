# *** Множество (set) ***

# Особенности:
# - неупорядоченная коллекция
# - нету индексов
# - при создании автоматически удаляет все дублирующие элементы

# *** создание множества ***

# первый способ
my_set = {"a","b","c"}

# второй способ
s = "hello"
my_list = [100,200,300,100,200]


my_set_2 = set(s)

# *** добавление элементов ***

my_set.add(777)
my_set.add((1,2,3,4)) # добавляются только картежи


# *** удаление элементов *** только по значению

my_set = {10,20,30,40}
# my_set.remove(30)

# проблема при удалении
# my_set.remove(50)

# решение проблемы
my_set.discard(40)

# *** Объединение множеств ***

users = {"John", "Tom", "Khristina"}
new_users = {"Bob","Kate","John"}

# users = users.union(new_users) позволяет создать новое множество и при этом сохранить исходное
users_2 = users | new_users # короткий аналог union

# users.update(new_users) # то же самое что и union(), но новое множество создается внутри первой переменной

# *** определение пересечений ***

intersect_users = users.intersection(new_users)

# короткий аналог метода пересечений intersevtion()
intersect_users = users & new_users

# *** определение разностей ***
# diff_users = users.difference(new_users) разность только из первого множества
# короткий аналог difference
# diff_users = users - new_users

# sd_users = users.symmetric_difference(new_users) симметричная разность

# короткий аналог


# print(diff_users)
# import this