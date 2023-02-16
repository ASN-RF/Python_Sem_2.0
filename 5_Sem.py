# Задача 1 (31). Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ...,
# где a0 = 0, a1 = 1, ak = = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи. Задание необходимо
# решать через рекурсию.
# Пример:
# Input: 7
# Output: 21  # ОШИБКА
# N = int(input('Введите число: '))
# def fib(numbers):
#     if numbers in [1, 2]:
#         return 1
#     elif numbers == 0:
#         return 0
#     return fib(numbers - 1) + fib(numbers-2)
# print (fib(N))

# --------------КОНЕЦ ЗАДАЧИ 1 (31)---------------

# Задача 2. (33). Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные
# оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные
# – на минимальные.
# Пример:
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
# Kol_ocenok = int (input('Сколько оценок в журнале: '))
# Spisok_ocenok = []
# for _ in range (Kol_ocenok):
#     Spisok_ocenok.append(int(input(f'Введите оценку по {_+1}-му предмету: ')))
# print(f'{Kol_ocenok} -> ', end='')
# print (*Spisok_ocenok)
# x = min(Spisok_ocenok)
# y = max(Spisok_ocenok)
# print (y)
# for i in range (Kol_ocenok):
#     if Spisok_ocenok [i] == y:
#        Spisok_ocenok [i] = x
# print (*Spisok_ocenok)



# --------------КОНЕЦ ЗАДАЧИ 2 (33)---------------

# Задача 3. (35). Напишите функцию, которая принимает одно число и проверяет, является ли оно простым.
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число).
# Пример:
# Input: 5
# Output: yes
def prostoe (x):
    for i in range (2, x//2+1):
        if x%i == 0:
            return 'No'
            break
    else:
        return 'Yes'
        
Chislo = int (input('Введите Ваше любимое число: '))

print (prostoe(Chislo))
# --------------КОНЕЦ ЗАДАЧИ 3 (35)---------------

# Задача 4. (37). Дано натуральное число N и последовательность из N элементов. Требуется вывести эту
# последовательность в обратном порядке. Примечание. В программе запрещается объявлять массивы и использовать
# циклы (даже для ввода и вывода).
# Пример:
# Input: 2 -> 3 4
# Output: 4 3
# def razvorot (x, spisok):
#     for i in range (x):
#         if i 
#         ind = spisok [i]
#         spisok [i] = spisok[x-1-i]
#         spisok[x-1-i] = ind
#     print (spisok)


# N = int (input('Введите число N: '))
# N_elementi = list(int(input(f'Введите {_} элементов через пробел: ').split()))
# for _ in range (N):
#     N_elementi.append()
# razvorot (N, N_elementi)


# --------------КОНЕЦ ЗАДАЧИ 4 (37)---------------
