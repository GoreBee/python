import random
import string

def matcher(text, pattern, d, q):
    n = len(text)
    m = len(pattern)
    h = pow(d,m-1)%q
    p = 0
    t = 0
    result = []
    for i in range(m): 
        p = (d*p+ord(pattern[i]))%q
        t = (d*t+ord(text[i]))%q
    for s in range(n-m+1): 
        if p == t: 
            match = True
            for i in range(m):
                if pattern[i] != text[s+i]:
                    match = False
                    break
            if match:
                result = result + [s]
        if s < n-m:
            t = (t-h*ord(text[s]))%q 
            t = (t*d+ord(text[s+m]))%q 
            t = (t+q)%q 
    return result

s_len = input("Введите строку или длину строки: ")

try:
    int(s_len) !=0
    s=''.join([random.choice(string.ascii_lowercase) for i in range(s_len)])
    min_i = max(int(input("Введите минимальную длину искомых подстрок: ")),1)-1
    max_i = min(int(input("Введите максимальную длину искомых подстрок: ")),s_len)
except ValueError:
    s = s_len
    s_len = len(s)
    min_i =0
    max_i = s_len-1


if min_i > max_i:
    min_i, max_i = max_i, min_i

checked={}

print("Cтрока: ",s)


for i in range(min_i,max_i):
    for j in range(s_len - i):
        patt=s[j:j+i+1]
        if not(patt in checked):
            print(f"\tПодстрока: {patt} Кол-во вхождений: {len(matcher(s,patt,257,11))}")
            checked[patt] = True

print("\tКоличество уникальных подстрок: ", len(checked))