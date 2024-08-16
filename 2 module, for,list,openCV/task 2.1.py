x=input("Введите ФИО\n")
if x == "Иванов Иван Иванович":
    print("Подходит")
else:
    print("Не те")
a=float(input("Введите коэффициет при х-квадрат\n"))
b=float(input("Введите коэффициет при х\n"))
c=float(input("Введите свободный член\n"))
d=b*b-4*a*c
if d<0:
    print("Действительных корней нет")
elif d==0:
    result=-b+d**(0.5)
    print("Оба корня равны ",result)
else:
    result_1 = -b + d ** (0.5)
    result_2 = -b - d ** (0.5)
    print("Первый корень ", result_1, "\nВторой корень ", result_2)