while True:
    a = input()
    if a.strip() == 'cancel':
        break
    elif not a.strip().isdecimal():
        print("Не удалось преобразовать введенный текст в число.")
    elif int(a)%2 == 0:
        print(int(int(a)/2))
    else:
        print((int(a)*3)+1)