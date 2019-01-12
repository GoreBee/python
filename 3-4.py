import random

a=[]
n=int(input("Введите число элементов массива: "))

for i in range(n):
    a.append(random.randint(0,10))

print (f"Сгенерированный массив: \n{a}")

b=[]
max_frq=0

for i in range(len(a)):
    frq=0
    for j in range(len(a)-i):
        if a[i] == a[j+i]:
            frq+=1
            if frq > max_frq:
                b=[]
                b.append(a[i])
                max_frq=frq
            elif frq==max_frq:
                b.append(a[i])
            

b.sort()
print(f"Элементы {b} встречаются чаще всего. Частота: {max_frq}")
