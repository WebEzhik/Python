#Задача 1
# a = {int(a) for a in input("Введите числа: ").split()}

# print(a)

# max = max(a)
# min = min(a)

# print(f"Максимум {max}, минимум {min}")


#Задача 2
# import cmath
# import math
# a = [int(a) for a in input("Введите числа A, B, C через пробел: ").split()]

# print(f"{a[0]}x^2+{a[1]}x+{a[2]}=0")


# D = a[1] * a[1] - 4 * a[0] * a[2]
# print(D)

# if(D < 0):
#     x1 = (- a[1] + cmath.sqrt(D)) / (2 * a[0])
#     x2 = (- a[1] - cmath.sqrt(D)) / (2 * a[0])
#     print(f"х1 = {x1}, x2 = {x2}")
# elif (D > 0):
#     x1 = (- a[1] + math.sqrt(D)) / (2 * a[0])
#     x2 = (- a[1] - math.sqrt(D)) / (2 * a[0])
#     print(f"х1 = {x1}, x2 = {x2}")
# else:
#     x = -a[1] / 2 *a[0]
#     print(f"х = {x}")



#Задача 

# import math
# from scipy.optimize import fsolve
# def func(x):
#     return x*math.cos(x-4)

# x0 = fsolve(func, 0.0)

# Задача 3
from datetime import datetime
import time

start_time = datetime.now()

# A = int(input('Введите число А: '))
# B = int(input('Введите число Б: '))
A = 35592245
B = 60452248


n1 = A
n2 = B
a = True
b = 1
while a:
    if (n1*b) % n2 == 0:
        print(n1*b)
        a = False        
    b += 1

print(datetime.now() - start_time)

start_time = datetime.now()


c = a =A
d = b = B
while a !=0:
    b,a = a, b%a

print(int(c*d/b))


print(datetime.now() - start_time)

start_time = datetime.now()


# for i in range(A, A*B*5):
#     if i % A == 0 and i % B == 0:
#         print(f"НОК = {i}")
#         break

# print(datetime.now() - start_time)

# start_time = datetime.now()

# for i in range(A+B, 0, -1):
#     if A % i == 0 and B % i == 0:
#         print(f"НОД = {i}")
#         break

# print(datetime.now() - start_time)


#Задача 3.1
# def gin(): # get valid int number
#     try:
#         user_input = int(input('Введите целое число '))
#         return user_input
#     except ValueError as v:
#         print(v)         
#         return gin()

# n1 = gin()
# n2 = gin()
# a = True
# b = 1
# while a:
#     if (n1*b) % n2 == 0:
#         print(n1*b)
#         a = False        
#     b += 1

