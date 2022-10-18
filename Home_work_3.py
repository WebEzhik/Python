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
import random

#N = int(input('Введите размер списка: '))
N = 4

list1 = []
for i in range(N):
    list1.append(random.randint(0, 10))
print(list1)

mult = []

j = 0
while j >= N - j - 1:
    mult.append(list1[j] * list1[N - j - 1])
    j =+ 1


print(mult)