# 1  разбираем  "for"
# 1 тип использоавние for, для перебора в списке или числе
# a = 'helllo'
# for i in a:
#     print(i, end='')
# print()
# for ind in range(len(a)):
#     print(a[ind], end='')

#  2 тип испольования for, для повторов
# for _ in range (3):   # "_" - означает, что цикл используется для повторов и переменная не важна
#     print ('hello')

# Задача 1 (9). По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N
# (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while.

# n = int(input('Введите целое неотрицательное число: '))
# ind = 1
# fac = 1
# while ind <= n:
#     fac *= ind
#     ind += 1
# print (fac)

# Задача 2. Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A. # Если А не является числом Фибоначчи, выведите число -1
#  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987
#     1  2  3  4  5  6   7   8   9  10  11   12   13   14  15    16

# A = int(input('Введите Ваше любимое натуральное число, которое больше 1: '))
# while A <= 1:
#     A = int(input('Введите НАТУРАЛЬНОЕ число, которое БОЛЬШЕ 1: '))

# # 1 вариант МОЙ
# fib = 0
# fib_1 = 0
# fib_2 = 1
# ind = 0
# while  A > fib_1:    # fib_1 + fib_2 <= A
#     fib = fib_1
#     fib_1 = fib_2
#     fib_2 += fib
#     ind += 1
# if A == fib_1 or A == fib_2:
#     print(
#         f'Число {A}, ВХОДИТ во множество чисел Фибоначчи, и находится по номером {ind}')
# else:
#     print(-1)

# 2 вариант  (разбор на семинаре)
# first_el = 0
# second_el = 1
# number = int(input())
# next_el = first_el + second_el
# i = 3
# while next_el < number:
#     first_el = second_el
#     second_el = next_el
#     next_el = first_el + second_el
#     i += 1
# if next_el == number:
#     print(i)
# else:
#     print(-1)


# Задача 3 (13). Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная
# оттепель за всю историю наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись
# исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель.
# Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия.
# Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# 1 Вариант МОЙ
# N = int(input('Введите общие количество дней в рассматриваемом периоде: '))
# Temperatyra = []
# max = 0
# pol = 0
# for i in range(1, N+1):
#     Temperatyra.append(int(input(f'Введите погоду {i} день: ')))
# for i in Temperatyra:
#     if i > 0:
#         pol += 1
#     else:
#         if max < pol:
#             max = pol
#             pol = 0
#         else:
#             pol = 0
# print(max)

# 2 Вариант разбор на семинаре НЕ РАБОТАЕТ!!
# max_count = 0
# count = 0
# n = int(input())
# for _ in range(n):
#     temp = int(input())
#     if temp > 0:
#         count += 1
#     else:
#         if count > max_count:
#             max_count = count
#         count = 0
# if max_count == 0 and count != 0:
#     print(count)
# else:
#     print(max_count)


# Задача 4 (15). Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком
# много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой
# строчке каждое. Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают
# 30000.
# N = int(input('Введите количество арбузов: '))
# Massa_arbuza = []
# for i in range(1, N+1):
#     Massa_arbuza.append(int(input(f'Введите массу {i} арбуза: ')))
# max = 0
# min = Massa_arbuza [0]
# ind_max = 0
# ind_min = 0

# 1 вариант
# print (Massa_arbuza)
# min_arb = min(Massa_arbuza)
# max_arb = max(Massa_arbuza)
# print (min_arb)
# print (max_arb)

# 2 вариант

# for i in Massa_arbuza:
#     if i > max:
#         max = i
#     elif i < min:
#         min = i
# print (max)
# print (min)

# 3 вариант
# Massa_arbuza.sort()
# print(Massa_arbuza[0])
# print(Massa_arbuza[len(Massa_arbuza)-1])

# 4 вариант

# for i in range(len(Massa_arbuza)):
#     if Massa_arbuza [i] < min:
#         min = Massa_arbuza [i]
#         ind_min = i
#     elif Massa_arbuza [i] > max:
#         max = Massa_arbuza [i]
#         ind_max = i
# print (f'Уважаемый Иван Иванович, Вы выбрали следующие арбузы весом:\n{Massa_arbuza}')
# print(f'Рекомендуем Вам взять арбуз под номером {ind_max+1}, так как он самый тяяжелый и весит {max} кг.\nА вот любимой теще взять арбуз под номером {ind_min+1} - он самый легкий и весит всего {min}кг. Приятного аппетита!')
