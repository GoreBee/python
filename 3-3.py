import random
a=[]
n=int(input("Введите число элементов массива: "))

for i in range(n):
    a.append(random.randint(0,100))

print (f"Сгенерированный массив: \n{a}")

imn = a.index(min(a))
imx = a.index(max(a))

a[imn], a[imx] = a[imx], a[imn]

print (f"Трансформированный массив: \n{a}")