import random

a=[]

while True:
    n=int(input("Введите число элементов массива: "))
    if n>1:
        break
    print("Число должно быть 2 и больше")

for i in range(n):
    a.append(random.randint(0,100))

print (f"Сгенерированный массив: \n{a}")

min1 = min(a)
a.remove(min1)
min2 = min(a)

print(f"Первый минимум: {min1} Второй минимум: {min2}")