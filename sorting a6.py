import timeit
import random

def selection_sort (orig_list):
    for i in range(len(orig_list)):
        idx_min =i
        for j in range(i+1,len(orig_list)):
            if orig_list[j]<orig_list[idx_min]:
                idx_min =j
        orig_list[i], orig_list[idx_min] = orig_list[idx_min], orig_list[i]
    return orig_list

def insertion_sort(orig_list):
    for i in range(len(orig_list)):
        v = orig_list[i]
        j = i
        while (orig_list[j-1]>v and j >0):
            orig_list[j] =orig_list[j-1]
            j-=1
        orig_list[j] = v
    return orig_list

def bubble_sort (orig_list):
    n = 1
    while n <len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] > orig_list[i+1]:
                orig_list[i], orig_list[i+1]= orig_list[i+1], orig_list[i]
        n +=1
    return orig_list

def quick_sort(orig_list):
    if len(orig_list) <= 1:
        return orig_list
    else:
        pivot = random.choice (orig_list)
        less = [x for x in orig_list if x < pivot]
        equal = [x for x in orig_list if x == pivot]
        greater = [x for x in orig_list if x > pivot]

    return quick_sort(less)+equal + quick_sort(greater)


def shell_sort (orig_list):
    def new_increment(orig_list):
        i = int(len(orig_list) / 2)
        yield i
        while i != 1:
            if i ==2:
                i =1
            else:
                i = int(round(i/2.2))
            yield i
        
    for increment in new_increment(orig_list):
        for i in range(increment, len(orig_list)):
            for j in range(i,increment-1, -increment):
                if orig_list[j-increment] < orig_list[j]:
                    break
                orig_list[j], orig_list[j-increment]=orig_list[j-increment], orig_list[j]
    return orig_list


def reverse_sort(orig_list):
    return sorted(orig_list)



#n = int(input("Введите число элементов: "))

n_list =[10,100,1000]
stime = {}
itime={}
btime={}
qtime={}
sltime={}
rtime={}

for n in n_list:
    orig_list = [random.randint(0,100) for i in range(n)]

    #print(orig_list)
    print("Расчитываем время для n = ",n)

    #print(selection_sort(orig_list[:]))
    print("\tСортируем по алгоритму selection sort")
    stime[n]=timeit.timeit("selection_sort(orig_list[:])", number = 1000,globals=globals())

    #print(insertion_sort(orig_list[:]))
    print("\tСортируем по алгоритму insertion sort")
    itime[n]=timeit.timeit("insertion_sort(orig_list[:])", number = 1000,globals=globals()) 
 
    #print(bubble_sort(orig_list[:]))
    print("\tСортируем по алгоритму пузырьковой сортировки")
    btime[n]=timeit.timeit("bubble_sort(orig_list[:])", number = 1000,globals=globals())

    #print(quick_sort(orig_list[:]))
    print("\tСортируем по алгоритму быстрой сортировки")
    qtime[n]=timeit.timeit("quick_sort(orig_list[:])", number = 1000,globals=globals())

    #print(shell_sort(orig_list[:]))
    print("\tСортируем по алгоритму shell sort")
    sltime[n] = timeit.timeit("shell_sort(orig_list[:])", number = 1000,globals=globals())

    #print(reverse_sort(orig_list[:]))
    print("\tСортируем по алгоритму встроенной сортировки")
    rtime[n]=timeit.timeit("reverse_sort(orig_list[:])", number = 1000,globals=globals())

print("n = \tSelect\tInsert\tBubble\tQuick \tShell \t Built-in")
for n in n_list:
    print(f"{n:4}\t{stime[n]:6.3f}\t{itime[n]:6.3f}\t{btime[n]:6.3f}\t{qtime[n]:6.3f}\t{sltime[n]:6.3f}\t{rtime[n]:6.3f}")

"""
Сравнение времени выполнения алгоритмов для разных n (размера списка)

n =     Select  Insert  Bubble  Quick   Shell    Built-in
  10     0.007   0.008   0.014   0.019   0.020   0.000
 100     0.396   0.436   0.783   0.169   0.313   0.005
1000    41.389  56.606  84.082   0.950   6.855   0.080
    

"""


