#                                СЕМИНАР 1

# Задача 1. Сумма трех. Посчитайте сумму трех введенных целых чисел.
# a = int(input('Введите 1-е число: '))
# b = int(input('Введите 2-е число: '))
# c = int(input('Введите 3-е число: '))
# print(f'{a} + {b} + {c} = {a+b+c}')
# -------КОНЕЦ ЗАДАЧИ-------

# Задача 2. Площадь. Пользователь вводит стороны прямоугольника, выведите его площадь.
# Dlina = float(input('Введите длину прямоугольника: '))
# Shirina = float(input('Введите ширину прямоугольника: '))
# print(
#     f'Площадь прямоугольника со сторонами {Dlina} и {Shirina} = {Dlina*Shirina}')
# -------КОНЕЦ ЗАДАЧИ-------

# # Задача 3. Периметр. Пользователь вводит стороны прямоугольника, выведите его периметр.
# Dlina = float(input('Введите длину прямоугольника: '))
# Shirina = float(input('Введите ширину прямоугольника: '))
# print(
#     f'Площадь прямоугольника со сторонами {Dlina} и {Shirina} = {2*(Dlina+Shirina)}')
# -------КОНЕЦ ЗАДАЧИ-------

# Задача 4. Меньшее из двух. Пользователь вводит два целых числа. Выведите меньшее из них.
# a = int(input('Введите 1-ое целое число: '))
# b = int(input('Введите 2-ое целое число: '))
# if a > b:
#     print(b)
# elif a == b:
#     print('Числа равны!')
# else:
#     print(a)
# -------КОНЕЦ ЗАДАЧИ-------

# Задача 5. Четырехзначное? Пользователь вводит целое число. Выведите Yes, если это число
# является четырехзначным, и NO в противном случае.
a = int(input('Введите Ваше любимое целое число: '))
if 999 < a < 10000 or -10000 < a < -999:
    print('Yes')
else:
    print('No')
# -------КОНЕЦ ЗАДАЧИ-------

# Задача 6. Пользователь вводит строки через "enter", пока не введет пустую строку. 
# Гарантируется, что в строках лежат только цифры. Найти сумму введеных чисел, которые кратны 4.



# Задача №1. За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# n = 700
# m = 750
# Output:
# 2

# n = int(input('Введите путь пройденный машиной за день \nn =  '))
# m = int(input('Введите путь значение требуемого маршрута \nm =  '))
# print (round (n/m))
# print (f'Чтобы проехать путь в {m} км. потребуется {int(m/n)} день(ей), {round ((m/n - int(m/n))*24,2)} час(ов) и {round ((((m/n - int(m/n))*24) - (int((m/n - int(m/n))*24)))*60)} минут')
# x = 41.5
# print(round(x))