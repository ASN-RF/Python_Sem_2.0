# Задача 1 (39). У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы
# используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а
# нужно получить его как есть. Напишите такое лямбда-выражение transformation, чтобы transformed_values
# получился копией values.
# Пример:
# Ввод:
# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#     print(‘ok’)
# else:
#     print(‘fail’)
# Вывод:
# ok

# transformation = lambda x: x
# values = [1, 23, 42, 'asdfg']
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')

# -------- КОНЕЦ 1 ЗАДАЧИ -------


# Задача 2 (49). Решение в группах. Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, по которой вращается
# самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет,
# зато искусственные спутники были запущены на круговые орбиты. Результатом функции должен быть кортеж,
# содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж
# из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины
# полуосей эллипса. При решении задачи используйте списочные выражения. Подсказка: проще всего будет найти
# эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий
# такую площадь. Гарантируется, что самая далекая планета ровно одна.
# Пример:
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10
# import math
# def find_farthest_orbit(x):
#     S = 0
#     rezult = ()
#     for i in range(len(x)):
#         if x[i][0] != x[i][1]:
#             if math.pi*x[i][0]*x[i][1] > S:
#                 S = math.pi*x[i][0]*x[i][1]
#                 rezult = x[i]
#     return rezult


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

# -------- КОНЕЦ 2 ЗАДАЧИ -------

# Задача 3 (51). Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют
# одинаковое значение некоторой характеристики, и возвращают True, если это так. Если значение характеристики
# для разных объектов отличается - то False. Для пустого набора объектов, функция должна возвращать True.
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
# Пример:
# Ввод:
# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print(‘same’)
# else:
#     print(‘different’)
# Вывод:
# same

# 1 вариант
# def same_by(characteristic, objects):
#     rez = []
#     for i in objects:
#         if characteristic(i) == 1:
#             return False
#         else:
#            return True
#  2 вариант 
def same_by(characteristic, objects):
    return len(set(map(characteristic, objects))) == 1 if objects else True        


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
