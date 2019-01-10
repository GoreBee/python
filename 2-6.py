import random

def ask_user (n):
    success = False

    guess= int(input("Введите число: "))
    if guess>n:
        print ("Загаданное число меньше")
    elif guess<n:
        print("Загаданное число больше")
    else:
        print("Вы угадали!")
        success = True
    return success


n = random.randint (0,100)
tries = 10

while tries > 0:
    if ask_user (n):
        break
    else:
        tries -=1

if tries ==0:
    print(f"Было загадано число {n}")