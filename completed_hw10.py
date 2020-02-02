print("Гипотеза Коллатца. Введите натуральное число: ")
while True:
    a = input()
    if a.isdecimal():
        a = int(a)
        break
    else:
        print("Вы неправильно ввели число!")

count = 0
while a != 1:
    count += 1
    if a % 2 == 0:
        a = a / 2
    else:
        a = a * 3 + 1

print(f"Для заданного натурального числа получилось {count} шагов")
