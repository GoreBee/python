import random

def bubble_sort (orig_list):
    n = 1
    while n <len(orig_list):
        moves = False # Флаг, показывающий были ли во внутреннем цикле перестановки
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1]= orig_list[i+1], orig_list[i]
                moves = True
        if not(moves):  # Если перестановок не было, значит массив уже отсортирован - можно завершать работу алгоритма
            break
        n +=1
    return orig_list

n = int(input("Введите число элементов: "))
orig_list = [random.randint(0,199)-100 for i in range(n)]

print(orig_list)
print(bubble_sort(orig_list[:]))