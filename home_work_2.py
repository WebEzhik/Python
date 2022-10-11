# Задача 1

# N = float(input('Введите число N: '))
# N = str(N)

# summ = 0
# Num = 0
# for i in range(len(N)):
#     if(N[i:i+1].isnumeric()):
#         Num = int(N[i:i+1])
#         if Num > 0:
#             summ = summ + Num
# print(summ)


# Задача 2

# N = int(input('Введите число N: '))
# arr = []

# for i in range(1, N+1):
#     mult = 1
#     for j in range(1, i+1):
#         mult = mult * j
#     arr.append(mult)
# print(arr)



# Задача 3

# N = int(input('Введите число N: '))

# dic = {i: round((1 + (1/i))**i, 2) for i in range(1, N+1)}
# print(dic, 2)

# summ = sum(dic.values())
# print(round(summ, 2))



# Задача 4
# import random

# N = int(input('Введите число N: '))

# list1 = []
# for i in range(N):
#     list1.append(random.randint(-N, N))
# print(list1)

# f = open('file.txt', 'r')
# number = f.readlines()

# mult = 1
# for i in number:
#     #print(i[0])
#     mult = mult * list1[int(i[0])]
# print(mult)

# f.close()


# Задача 5
# import random

# arr = []
# N = 10
# for i in range(N):
#     arr.append(i+1)
# print(arr)

# mix = 0
# for i in range(len(arr)):
#     mix = random.randint(0, len(arr)-1)
#     temp = arr[i]
#     arr[i] = arr[mix]
#     arr[mix] = temp

# print(arr)
