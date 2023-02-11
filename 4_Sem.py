# Задача 1 (25). Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
# Для решения данной задачи используйте функцию .split()
# Пример:
#    a b c d
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# 1 вариант
# stroka = list(input('Введите Вашу строку: ').split(' '))
# # # stroka =  ['a', 'a', 'a', 'b', 'c', 'a', 'a', 'd', 'c', 'd', 'd']
# stroka_2 = set (stroka)
# for i in stroka_2:
#     count = 0
#     print(i, end='')
#     for j in stroka:
#         if i == j:
#             count += 1
#             print(f' {i}_{count} ', end='')
# 2 вариант (семинар)
# stroka = list(input('Введите Вашу строку: ').split(' '))
# primer = 'a a a b c a a d c d d'
# stroka =  primer.split()
# my_dict = {}
# new_list = []
# for i in stroka:
#     my_dict[i] = my_dict.get(i,0)  + 1
#     if my_dict.get(i) > 1:
#         new_list.append(i + '_' + str (my_dict.get(i)-1))
#     else:
#         new_list.append(i)
# # print (*new_list)
# print (' '.join(new_list))

# 3 вариант
# stroka =  'a a a b c a a d c d d'.split()
# for i in range(len(stroka)):
#     k = 1
#     for j in range(i+1, len(stroka)):
#         if stroka[i] == stroka[j]:
#             k +=1
#             stroka[j] = f'{stroka[j]}_{k-1}'
# print (*stroka)
# --------------КОНЕЦ ЗАДАЧИ 1 (25)---------------

# Задача 2 (27). Пользователь вводит текст(строка). Словом считается последовательность непробельных символов
# идущих подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Пример:
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13
# 1 вариант (мои вариант)
# stroka = str("She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells")
# stroka = stroka.upper()
# stroka.remove('')
# words = stroka.split(' ')
# print (len(set(words)))

# 2 вариант (семинар)
# stroka = str("She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells")
# # stroka = stroka.upper() ## удаление лишнх пробелов
# words = set(stroka.split())
# print (len(words))


# 3 вариант (мои вариант + семинар)
# stroka = set(("She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells".split()))
# print (len(stroka))
# --------------КОНЕЦ ЗАДАЧИ 2 (27)---------------

# Задача №29. Ваня и Петя поспорили, кто быстрее решит следующую задачу:
# “Задана последовательность неотрицательных целых чисел. Требуется определить значение наибольшего элемента
# последовательности, которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”.
# Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание. Они
# решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. За помощью товарищи обратились к Вам,
# студентам.
# Ваня:
# n = int(input())
# max_number = 1000
# while n != 0:
#     # n = int(input())
#     if max_number > n:
#         max_number = n
# print(max_number)

# Петя:
# n = int(input())
# max_number = -1
# while n < 0:
#     n = int(input())
#     if max_number < n:
#         n = max_number
# print(n)

#  1 - У обоих не задается последовательность

# chisla = (1, 7, 9, 0)
# max_chislo = 0
# for i in chisla:
#     if i != 0:
#         if max_chislo < i:
#             max_chislo = i
#     if i == 0:
#         break
# print(max_chislo)

# Задача 4. Дана последовательность чисел. Получить список уникальных элементов заданной последовательноcти.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# 1 вариант
# spisok = [1, 2, 3, 5, 1, 5, 3, 10]
# my_dict = {}
# rezult = []
# for i in spisok:
#     my_dict[i] = my_dict.get(i,0)  + 1
# for i in my_dict.keys():
#     if my_dict.get(i) <= 1:
#         rezult.append(i)
# print (f'{spisok} => {rezult}')

# 2 вариант
# spisok = [1, 2, 3, 5, 1, 5, 3, 10]
# rezult = []
# for i in spisok:
#     if spisok.count(i) == 1:
#         rezult.append(i)
# print (f'{spisok} => {rezult}')

# 3 вариант
spisok = [1, 2, 3, 5, 1, 5, 3, 10]
print(f'{spisok} => {[i for i in spisok if spisok.count(i) == 1]}')
