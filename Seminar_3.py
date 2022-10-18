import datetime

f=(datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()

f=int(f)
print(f)

def myrandint(  start,end,seed=999999999   ):
    a = 32310901 # Сгенерированное случайное число является наиболее равномерным
    b=1729
    rOld=seed
    m=end-start
    while True: # Каждый раз, когда вызывается эта функция myrandint, случайное число генерируется один раз
        rNew = start + (a*rOld+b)%m
        yield rNew
        rOld=rNew
        
 # Симулировать, используя 20 различных семян для генерации случайных чисел
for i in range(5):
    r = myrandint(1,100, f + i)
         # Генерировать 10 случайных чисел на семя
    print ('Seed', i, 'Generate Random Number')
    for j in range(2):
        print( next(r),end=',' )
    print(      )

