n=int(input("Введите число элементов ряда для суммирования: "))

el = 1
elsum = 0

while n>0:
    elsum +=el
    el /= -2
    n -=1

print(f"Сумма равна: {elsum}") 