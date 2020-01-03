def degree_converter(x, mode):
    if mode.lower() == 'f':
        return (x - 32) / 1.8            # (Фаренгейт — 32) : 1,8 = Цельсий
    elif mode.lower() == 'c' or mode.lower() == 'с':
        return (x * 1.8) + 32            # Цельсий х 1,8 + 32 = Фаренгейт
    else:
        return 'Ошибка'


print(f'32 градуса по Фаренгейту это {degree_converter(32,"f")} по Цельсию')
print(f'0 градусов по Цельсию это {degree_converter(0, "c")} по Фаренгейту')
print(degree_converter(int(input('Введите число градусов, которое необходимо сконвертировать\n')),
                       input('Введите \"c\" если вы конвертируете из Цельсия в Фаренгейты и \"f\" если наоборот\n')))
