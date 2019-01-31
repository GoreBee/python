import random
import collections

m = int(input("Введите число m: "))
n = m*2 +1

a = [random.randint(0,100) for i in range(n)]


print(a)

histogramm = collections.Counter()
for i in a:
    histogramm[i] +=1


k = 0
for i in range(max(a)):
    if i in histogramm:
        k += histogramm[i]
    if k> len(a) // 2:
        if histogramm[i]== 1:
            print(f"Медианой массива является число {i}. \n\tКоличество элементов не меньше медианы: {k}\n\tКоличество элементов не больше медианы {len(a)-k+histogramm[i]}")
        else:
            print(f"Наиболее близким к медиане массива является число {i}. \n\tКоличество элементов не меньше медианы: {k}\n\tКоличество элементов не больше медианы {len(a)-k+histogramm[i]}")
        break

