while True:
    print("Введите два числа и знак операции")
    n1 = float(input("\tПервое число: "))
    n2 = float(input("\tВторое число: "))
    op = input("\tОперация (+,-,/,*, для выхода - 0 ): ")
    
    if op == '0': break
    
    if op == '/' and n2 == 0:
        print("Невозможно разделить на ноль")
    else:
        if op == '+':
            print(f"\tРезультат: {n1+n2}")
        elif op == '-':
            print(f"\tРезультат: {n1-n2}")
        elif op == '/':
            print(f"\tРезультат: {n1/n2}")
        elif op == '*':
            print(f"\tРезультат: {n1*n2}")
        else:
            print("Неустановленная операция")
