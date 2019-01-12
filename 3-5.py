import random

a=[]
n=int(input("Введите число элементов массива: "))

for i in range(n):
    a.append(random.randint(0,100)-50)

print (f"Сгенерированный массив: \n{a}")

mx_neg = min(a)
imx_neg = a.index(mx_neg)

for i in a:
    if i<0 and i>mx_neg:
        mx_neg =i
        imx_neg = a.index(i)

if mx_neg >=0:
    print("Массив не содержит отрицательных элементов")
else:
    print (f"Максимальный отрицательный элемент: {mx_neg} находится на {imx_neg+1} позиции")