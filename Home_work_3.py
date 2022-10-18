# Задача 1
# import random

# N = int(input('Введите размер списка: '))

# list1 = []
# for i in range(N):
#     list1.append(random.randint(0, 10))
# print(list1)

# sum = 0
# for i in range(1, N, 2):
#     sum = sum + list1[i]
#     #print(list1[i])
# print(sum)

# Задача 2
# import random

# #N = int(input('Введите размер списка: '))
# N = 5

# list1 = []
# for i in range(N):
#     list1.append(random.randint(0, 10))
# print(list1)

# mult = []
# i = 0
# while i <= N - i - 1:
#     mult.append(list1[i] * list1[N - i - 1])
#     i = i + 1

# print(mult)

# Задача 3
# list = [1.1, 1.2, 3.1, 5, 10.01]
# print(list)

# min = round(list[0] % 1, 5)
# max = round(list[0] % 1, 5)
# for i in list:
#     #print(round(i%1, 5))
#     if(round(i%1, 5) != 0):
#         if max < i % 1:
#             max = round(i % 1, 5)
#         if min > i % 1:
#             min = round(i % 1, 5)

# # print()
# # print("min", min)
# # print("min", max)
# print(max-min)


# Задача 3

# N = int(input('Введите десятичное число: '))

# b = ''

# while N > 0:
#     b = str(N % 2) + b
#     N = N // 2

# print(b)

# Задача 4
import math
#N = int(input('Введите число: '))
N = 8

Fib =[0] * (N * 2 +1)

Fib[N + 1] = 1
Fib[N - 1] = Fib[N + 1]

for i in range(2, N + 1):
    Fib[N + i] = Fib[N + i - 2] + Fib[N + i - 1]
    Fib[N - i] = Fib[N - i + 2] - Fib[N - i + 1]

print(Fib)


