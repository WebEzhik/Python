#Шпаргалка 1
# str1 = input('Введите первую строку: ')
# str2 = input('Введите букву: ')

# start = None
# stop = None

# for i in range(len(str1)):
#     if str1[i] == str2:
#         stop = i + 1
#         if start == None:
#             start = i + 1

# print(start)
# print(stop)

#Шпаргалка 2

# str = input('Введите строку: ')

# print(f'{str * 4}\n{str * 3}\n{str * 2}\n{str}\n')




# f = open('file.txt', 'r')

# number = f.readlines()

# print(number)

# f.close()



#Шпаргалка 3

# import random

# #N = int(input('Введите число N: '))
# N = 10

# list1 = []
# for i in range(N):
#     list1.append(random.randint(15, 21))
# print(list1)

# for i in range(len(list1)):
#     if list1[i] == 20:
#         list1[i] = 200
#         break
# print(list1)

# for i in range(len(list1)):
#     list1[i] = list1[i] * list1[i]

# print(list1)


#Шпаргалка 4

# a = list('list')
# b = ['l','li','lis','list']

# d = {a[i]: b[i] for i in range(len(b))}

# print(d.values())









# Задача 1
# import random

# N = int(input('Введите число N: '))
# print(f"Для N = {N}: ", end= "")

# arr = []
# for i in range(N):
#     arr.append(random.randint(-100, 100))

# print(arr)


# Задача 2

# N = int(input('Введите число N: '))

# dic = {a: 3*a+1 for a in range(1, N+1)}

# print(dic)


# Задача 3

str1 = input('Введите первую строку: ')
str2 = input('Введите вторую строку: ')

# print(str1.count(str2))



count = 0
for i in range(len(str1)-2):
    if str1[i:i+len(str2)] == str2:
        count = count + 1
print("n = ", count)


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
#     print(i[0])
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
