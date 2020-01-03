def fib(n):
    a = 1
    b = 1
    count = 0
    while True:
        if count == n:
            break
        print(a)
        temp = b
        b = a + b
        a = temp
        count += 1


fib(int(input('Сколько чисел Фибоначчи нужно посчитать?\n')))
