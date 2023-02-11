# Задача 1. Дан список чисел. Определите, сколько в нем встречается различных чисел. Примечание: Пользователь
# может вводить значения списка или список задан изначально.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Vibor = int(input('Вы хотите ввести список чисел сами или использовать список из примера?: \n1 - ввести самому\n2 - использовать список из примера\n'))
# if Vibor == 1:
#     spisok = list(input('Введите Ваши любимые числа через пробел: ').split())
# elif Vibor == 2:
#     spisok = [1, 1, 2, 0, -1, 3, 4, 4]
# else:
#     print ('К сожалению такого варианта не предусмотрено! GAME OVER!!!')

# 1 вариант
# spisok_rez = []
# for i in spisok:
#     if i not in spisok_rez:
#         spisok_rez.append(i)
# print(f'{spisok} -> {len(spisok_rez)}')

# 2 вариант
# print (len(set(spisok)))

# 3 вариант
# print(len(set(input('Введитие ваши числа через пробел: ').split())))

# Задача 2. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число. Примечание: Пользователь может
# вводить значения списка или список задан изначально.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# Vibor = int(input('Вы хотите ввести список чисел сами или использовать список из примера?: \n1 - ввести самому\n2 - использовать список из примера\n'))
# if Vibor == 1:
#     spisok = [int(i) for i in input(
#         'Введите Ваши любимые числа через пробел: ').split()]
# elif Vibor == 2:
#     spisok = [1, 2, 3, 4, 5]
# else:
#     print('К сожалению такого варианта не предусмотрено! GAME OVER!!!')

# k = int(input('Введите число: '))
# k = k % len(spisok)
# spisok_rez = [0]*len(spisok)
# for i in range(len(spisok)):
#     if i+k < len(spisok) and i+k >= 0:
#         spisok_rez[i] = spisok[i+k]
#     if i+k >= len(spisok):
#        spisok_rez[i] = spisok[i+k-len(spisok)]
#     if i+k < 0:
#         spisok_rez[i] = spisok[i+k+len(spisok)]
# print (spisok_rez)

# 2 вариант (на семинаре)
# spisok_rez = list()
# for i in range(k):
#     spisok_rez.append(spisok[len(spisok)-1-i])
# for i in range(len(spisok)-k):
#     spisok_rez.append(spisok[i])
# print(spisok_rez)


# Задача №21. Напишите программу для печати всех уникальных значений в словаре. Примечание: Список словарей
# задан изначально. Пользователь его не вводит.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# dictionary_1 = \
#     {
#         "V": "S001",
#         "V": "S002",
#         "VI": "S001",
#         "VI": "S005",
#         "VII": " S005 ",
#         " V ": " S009 ",
#         " VIII ": " S007 "
#     }
# spisok = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {
#     "VII": " S005 "}, {" V ": " S009 "}, {" VIII ": " S007 "}]
# set_1 = set()
# spisok_rez = list()
# for i in spisok:
#     for j in i:
#         spisok_rez.append(i[j])
# print(spisok_rez)
# spisok_rez = [i.strip(' ') for i in spisok_rez]
# print(spisok_rez)
# print(*set(spisok_rez))

# Задача №23. Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов
# массива, больших предыдущего (элемента с предыдущим номером). Примечание: Пользователь может вводить
# значения списка или список задан изначально.
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
Vibor = int(input('Вы хотите ввести список чисел сами или использовать список из примера?: \n1 - ввести самому\n2 - использовать список из примера\n'))
if Vibor == 1:
    spisok = [int(i) for i in input(
        'Введите Ваши любимые числа через пробел: ').split()]
elif Vibor == 2:
    spisok = [0, -1, 5, 2, 3]
else:
    print('К сожалению такого варианта не предусмотрено! GAME OVER!!!')
count = 0
for i in range(len(spisok)-1):
    if spisok[i+1] > spisok[i]:
        count += 1
print(count)
