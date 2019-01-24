

class Hex_num:
    
    def __init__ (self,value):
        self.value = value
  
    def __add__ (self, obj):
        s1 = int(''.join(self.value),16)
        s2 = int(''.join(obj.value),16)
        self.value = list(hex(s1+s2))[2:]
    
    def __mul__ (self,obj):
        m1 = int(''.join(self.value),16)
        m2 = int(''.join(obj.value),16)
        self.value = list(hex(m1*m2))[2:]


a = Hex_num(list(input("Введите первое число:")))
b = Hex_num(list(input("Введите второе число:")))

print(f"a = {a.value}, b = {b.value}")

a1=Hex_num([])
a1.value = a.value
a + b
a1 * b
print(f"Сумма: {a.value}\nПроизведение: {a1.value}")

    


