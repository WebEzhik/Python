# #Домашняя работа 3 Задача 2
# import random

# #N = int(input('Введите размер списка: '))
# N = 5

# list1 = ""
# for i in range(N):
#     list1 = list1 + str(random.randint(0, 10)) + " "

# list1 = list(map(int, list1.split()))

# print(list1)

# mult = []
# i = 0
# while i <= N - i - 1:
#     mult.append(list1[i] * list1[N - i - 1])
#     i = i + 1

# print(mult)





#Домашняя работа 3 Задача 3

# list1 = [1.1, 1.2, 3.1, 5, 10.01, 0]
# print(list1)

# list1 = list(map(lambda i: abs(i) % 1, list1))
# list1 = list(filter(lambda e: e != 0, list1))
# print(round(max(list1), 5) - round(min(list1), 5))





#Для фенкции zip не нашел задачи с двумя массивами

import random

def GenArr(N):
    list1 = ""
    for i in range(N):
        list1 = list1 + str(random.randint(0, 10)) + " "

    list1 = list(map(int, list1.split()))

    return list1

#N = int(input('Введите размер списка: '))
N = 5

list1 = GenArr(N)
print(list1)
list2 = GenArr(N)
print(list2)

list_zip = zip(list1, list2)

for i in list_zip:
    print(i, end=" ")

list3 = []
for i in list_zip:
    list3.append(i[0])
    list3.append(i[1])
    #print(i, end=" ")

print(list3)