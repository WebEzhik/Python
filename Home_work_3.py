#Задача 1
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

#Задача 2
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

#Задача 3
list = [1.1, 1.2, 3.1, 5, 10.01]
print(list)

min = round(list[0] % 1, 2)
max = round(list[0] % 1, 2)
for i in list:
    print(max)
    if 
    if max < i % 1:
        max = round(i % 1, 2)
    if min > i % 1:
        min = round(i % 1, 2)
print(min)
print(max)
print(max-min)