import random

a=[]

n=int(input("Введите число элементов массива: "))

for i in range(n):
    a.append(random.randint(0,100))

print (f"Сгенерированный массив: \n{a}")

lb = min(a.index(min(a)), a.index(max(a)))+1
ub = max(a.index(min(a)), a.index(max(a)))

s = sum(a[lb:ub])

print (f"Сумма между минимальным ({min(a)}) и максимальным ({max(a)}) элементом, не включая их, равна {s}")