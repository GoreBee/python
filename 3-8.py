m = 5
n = 4
a=[]

for i in range(n):
    s=0
    print(f"Введите значения {i+1}-й строки через пробел:")
    b = input()
    b = b.split()
    b = b[:m]

    while len(b)<m:
        b.append(0)        
    
    b = [int(j) for j in b]
    s = sum(b)
    b.append(s)
    a.append(b)

for i in a:
    print(i)
