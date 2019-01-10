m = int(input("Введите количество чисел: "))
d = input("Введите цифру для проверки: ")

count = 0

for i in range(1,m+1):
    n = input(f"Введите число {i}: ")
    for j in n:
        if d == j:
            count +=1

print(f"Цифра {d} встречается {count} раз")