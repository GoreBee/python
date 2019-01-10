n=input("Введите число: ")

odd = 0
even = 0 

for d in n:
    if int(d) % 2 == 0:
        odd +=1
    else:
        even +=1

print(f"Количество нечетных цифр: {even}; количество четных цифр: {odd}")