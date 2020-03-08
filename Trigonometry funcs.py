import math


class Arguments:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Functions (Arguments):
    def sumc(self, a, b):
        self.a = a
        self.b = b
        print(2 * math.cos((a + b) / 2) * math.cos((a - b) / 2))

    def diffc(self, a, b):
        self.a = a
        self.b = b
        print(2 * math.sin((a + b) / 2) * math.sin((a - b) / 2))

    def sums(self, a, b):
        self.a = a
        self.b = b
        print(2 * math.cos((a + b) / 2) * math.sin((a - b) / 2))

    def diffs(self, a, b):
        self.a = a
        self.b = b
        print(2 * math.sin((a + b) / 2) * math.cos((a - b) / 2))


print("Нажмите 1, чтобы вычислить сумму косинусов")
print("Нажмите 2, чтобы вычислить разность косинусов")
print("Нажмите 3, чтобы вычислить сумму синусов")
print("Нажмите 4, чтобы вычислить разность синусов")
print("Введите 5, чтобы завершить работу")


while 1:
    i = int(input("Введите номер операции: "))

    if i == 5:
        break
    else:
        c = int(input("Введите аргумент 'a':"))
        d = int(input("Введите аргумент 'b':"))
        if i == 1:
            func = Functions(c, d)
            print(func.sumc(c, d))
        elif i == 2:
            func = Functions(c, d)
            print(func.diffc(c, d))
        elif i == 3:
            func = Functions(c, d)
            print(func.sums(c, d))
        elif i == 4:
            func = Functions(c, d)
            print(func.diffs(c, d))
        else:
            print("Операции под номером " + str(i) + " не существует!")
        continue
