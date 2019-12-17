"""
Первым циклом проходимся по листу введенных данных и записываем слова и количества повторов в словарь, вторым считываем
"""
while True:
    print("Введите текст...")
    a = input()
    words = a.split()
    uwords = dict()
    maxcount = 0
    for word in words:
        if not uwords.__contains__(word.lower()):
            uwords[word.lower()] = 1
        else:
            uwords[word.lower()] = uwords[word.lower()] + 1
            if maxcount < uwords[word.lower()]:
                maxcount = uwords[word.lower()]
    for word in uwords:
        if uwords[word] == maxcount:
            print(uwords[word], " - ", word)

