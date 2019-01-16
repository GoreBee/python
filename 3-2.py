a = input("Введите элементы массива через пробел: ")
a = a.split()
a = [int(i) for i in a]

odd =[]

for i in range(len(a)):
    if a[i] % 2 == 0:
        odd.append(i)

print(f"Индексы четных чисел в исходном массиве (начиная с 0): {odd}")