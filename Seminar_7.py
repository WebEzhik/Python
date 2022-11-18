# def Enter_number(): # функция ввода числа с проверкой 
#     try:
#         value = int(input())
#         break
#     except:
#         print("Ошибка! Введите число:")
#     return value

def multiplicat_numbers(a, b):
    sign = "*"
    result = round(a * b, 4)
    return sign, result

a, b = multiplicat_numbers(5.3, 7.6)

print(a, b)

# from datetime import datetime



# def sum_logger(data1, data2, data3):
#     time=datetime.now().strftime('%H:%M')
#     with open('log.csv', 'a') as file:
#         file.write("{}; {}; + {}; = {} ". format(time, data1, data2, data3))

# def div_logger(data1, data2, data3):
#     time=datetime.now().strftime('%H:%M')
#     with open('log.csv', 'a') as file:
#         file.write("{}; {}; / {}; = {} ". format(time, data1, data2, data3))


# def sub_logger(data1, data2, data3):
#     time=datetime.now().strftime('%H:%M')
#     with open('log.csv', 'a') as file:
#         file.write("{}; {}; - {}; = {} ". format(time, data1, data2, data3))


# def mult_logger(data1, data2, data3):
#     time=datetime.now().strftime('%H:%M')
#     with open('log.csv', 'a') as file:
#         file.write("{}; {}; * {}; = {} ". format(time, data1, data2, data3))
