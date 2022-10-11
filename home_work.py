#Задача 1
# N = int(input('Введите день недели: '))
 
# if(N <= 0 or N >= 8):
#     print("Это не день недели.")
# elif(N == 6 or N == 7):
#     print("Выходной.")
# else:
#     print("Будний")
 
#Задача 2
 
# for x in True, False:
#     for y in True, False:
#         for z in True, False:
#             if((not(x or y or z)) == (not(x) and not(y) and not(z))):
#                 print("Истинно")
#             else:
#                 print("Ложно")
 
#Задача 3
 
# x = int(input('Введите x: '))
# y = int(input('Введите y: '))
 
# if(x > 0 and y > 0):
#     print("Первая четверть.")
# elif(x < 0 and y > 0):
#     print("Вторая четверть.")
# elif(x < 0 and y < 0):
#     print("Третья четверть.")
# else:
#     print("Четвертая четверть.")
 
#Задача 4
 
x = int(input('Введите номер четверти: '))

if(x < 1 or x > 4):
    print("Это не четверть")
else:
    if(x == 1):
        print("x > 0, y > 0")
    elif(x == 2):
        print("x < 0, y > 0")
    elif(x == 4):
        print("x < 0, y < 0")
    else:
        print("x > 0, y < 0")
 
#Задача 5
# import math
 
# x1 = int(input('Введите x первой точки: '))
# y1 = int(input('Введите y первой точки: '))
 
# x2 = int(input('Введите x второй точки: '))
# y2 = int(input('Введите y второй точки: '))
 
# AB = math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))
# print(round(AB, 2))

