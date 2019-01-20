import timeit


n=int(input("Введите число элементов ряда для суммирования: "))

def c (n):
    n1=n
    el = 1
    elsum = 0

    while n1>0:
        elsum +=el
        el /= -2
        n1 -=1
    return elsum




def recur (n,m):
    if n==m+1:
        return (-0.5)**m
    else:
        return (-0.5)**m+recur(n,m+1)


rtime = timeit.timeit("recur(n,0)", setup="from __main__ import recur, n")
ctime = timeit.timeit("c(n)", setup="from __main__ import c, n")

print(f"Решение с помощью цикла. Сумма равна: {c(n)}. Время на выполнение: {ctime}")
print(f"Решение с помощью рекурсии. Сумма равна: {recur(n,0)}. Время на выполнение: {rtime}")

"""
Вариант решения с помощью цикла быстрее

Например, для n=10
Решение с помощью цикла. Сумма равна: 0.666015625. Время на выполнение: 4.359652958000002
Решение с помощью рекурсии. Сумма равна: 0.666015625. Время на выполнение: 12.100967929000001
