max_number = 0
max_digit_sum = 0

while True:
    n = input("Введите натуральное число или 0 для выхода: ")
    if n=='0':
        break
    s = 0
    for i in n:
        s += int(i)
    if s>=max_digit_sum:
        max_digit_sum = s
        max_number = int(n)

print(f"Число {max_number} имеет наибольшую сумму цифр, равную {max_digit_sum}")
