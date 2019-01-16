n=int(input("Введите число элементов ряда для суммирования: "))

n1=n
el = 1
elsum = 0

while n1>0:
    elsum +=el
    el /= -2
    n1 -=1

print(f"Решение с помощью цикла. Сумма равна: {elsum}") 

def recur (n,m):
    if n==m+1:
        return (-0.5)**m
    else:
        return (-0.5)**m+recur(n,m+1)

print(f"Решение с помощью рекурсии. Сумма равна: {recur(n,0)}") 
