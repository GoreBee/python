import collections
data = collections.defaultdict(list)

n = int(input("Введите число предприятий: "))
avrev =0  # Средняя прибыль по отрасли

for i in range(n):
    cname = input(f"Введите название предприятия №{i+1}: ")
   
    for j in range(4):
        data[cname].append(int(input(f"\tВведите прибыль за {j+1} квартал: "))) # добавляем данные о поквартальной прибыли
        
    avrev+= sum(data[cname])/n # корректируем значение среднеотраслевой годовой прибыли

print (f"Средняя годовая прибыль по отрасли: {avrev:.2f}")

print("Предприятия с годовой прибылью выше среднего:")
for i in data:
        if sum(data[i])>=avrev:
            print(f"\t{i}: {sum(data[i])}")

print("Предприятия с годовой прибылью ниже среднего:")
for i in data:
    if sum(data[i])< avrev:
        print(f"\t{i}: {sum(data[i])}")
