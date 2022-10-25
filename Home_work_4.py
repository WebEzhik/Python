#Задача 1

# def GetIntNumber():
#     N = abs(int(input("Введите число от 1 до 10 для определения точности: ")))
#     if(1 <= N <= 10):
#         return N
#     else:
#         print("Число не верно. Попробуйте снова.")
#         return GetIntNumber

# n = GetIntNumber()
# d = pow(10, -n)
# P = 0
# x = 1
# a = 1
# while True:
#     s = 4/x
#     P = P + a * s
#     if s < d:
#         break
#     a = -a
#     x += 2
# print(round(P, n))



#Задача 2

# N = abs(int(input("Введите натуральное число: ")))

# def CheckSymple(N):
#     for i in range(2, int(N/2)+1):
#         if N % i == 0:
#             return False
#     return True

# a = []
# count = 2
# while count <= N:
#     if not (N % count) and CheckSymple(count):
#         a.append(count)
#     count += 1
# print(a)



#Задача 3

# from random import randint

# list = [randint(1, 4) for i in range(5)]
# #list = [2, 2, 2, 2, 3]
# print(list)

# i = 0
# l = len(list)
# while i < l - 1:
#     j = i + 1
#     while j < l:
#         if list[i] == list[j]:
#             del list[j]
#             l -= 1
#         else:
#             j += 1
#     i += 1
# print(list)


#Задача 4

# from random import randint

# N = abs(int(input("Степень многочлена: ")))
# #N = 7

# string = ""
# for i in range(N, 0, -1):
#     ind = randint(0, 101)
#     if(ind != 0):
#         string = string + str(ind)+ "x^" + str(i) + "+"
# ind = randint(0, 101)
# if(ind != 0):
#     string = string + str(ind)+ "=0"

# f = open('text.txt', 'w')
# f.write(string)
# f.close()

# f = open('text.txt', 'r')
# s = f.read()
# print(s)
# f.close()

#Задача 5


def GetListPolynom(polynom):
    polynom = polynom.split("+")
    polynom[len(polynom)-1] = polynom[len(polynom)-1].replace("=", "x^")
    return polynom

def GetSortList(polynom):
    pol = [[], []]
    for i in range(len(polynom)):
        ind = polynom[i][:polynom[i].find("x")]
        deg = polynom[i][polynom[i].find("^")+1:]
        pol[0].append(ind)
        pol[1].append(deg)
    return pol

def SummPolynom(pol1, pol2):
    polSumm = [[],[]]
    
    for i in range(len(pol1[1])):
        flag = True
        for j in range(len(pol2[1])):
            if pol1[1][i] == pol2[1][j]:
                polSumm[0].append(int(pol1[0][i]) + int(pol2[0][j]))
                polSumm[1].append(int(pol1[1][i]))
                flag = False
        if flag:
            polSumm[0].append(int(pol1[0][i]))
            polSumm[1].append(int(pol1[1][i]))
    return polSumm


f = open('text1.txt', 'r')
polynom1 = f.read()
f.close()

f = open('text2.txt', 'r')
polynom2 = f.read()
f.close()


polynom1 = GetListPolynom(polynom1)
polynom2 = GetListPolynom(polynom2)

polynom1 = GetSortList(polynom1)
polynom2 = GetSortList(polynom2)

# print(polynom1)
# print(polynom2)

if len(polynom1) > len(polynom2):
    Summ = SummPolynom(polynom1, polynom2)
else:
    Summ = SummPolynom(polynom2, polynom1)

# print(Summ)

SummString = ""
for i in range(len(Summ[0])-1):
    SummString = SummString + str(Summ[0][i]) + "x^" + str(Summ[1][i]) + "+"
SummString = SummString + str(Summ[0][len(Summ[0])-1]) + "=0"
print(SummString)