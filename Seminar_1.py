#Задача 1
# N1 = int(input('Введите первое число: '))
# N2 = int(input('Введите второе число: '))

# if (N2 == N1 * N1) or (N1 == N2 * N2):
#     print("Да")
# else:
#     print("Нет")


#Задача 2
# Numbers = []

# for i in range(5):
#     Numbers.append(int(input(f'Введите {i+1} число: ')))

# print(Numbers)

# max = Numbers[i]

# for i in range(len(Numbers)):
#     if Numbers[i] > max:
#         max = Numbers[i]

# print(max)



# max = int(input(f'Введите 1 число: '))

# for i in range(4):
#     i += 1
#     N = int(input(f'Введите {i+1} число: '))
#     if N > max:
#         max = N
# print(max)

#Задача 3

# N = int(input('Введите число N: '))
# N = abs(N)

# # for i in range(-N, N):
# #     print(i, end=', ')
# # print(N)

# i = -N
# while i < N:
#     print(i, end=', ')
#     i += 1
# print(N)

#Задача 4

# N = float(input('Введите число N: '))
# if N % 1 == 0:
#     print("нет")
#     quit()

# N *= 10
# N = int(N % 10)

# print(N)

#Задача 5
N = int(input('Введите число N: '))

if((N % 5 == 0 and N % 10 == 0) or (N % 15 == 0)) and (N % 30 != 0):
    print("Да")
else:
    print("нет")