while True:
    print("Введите текст...")
    a = input()
    words = a.split()
    words = [word.lower() for word in words]
    uwords = {word:words.count(word) for word in words}
    final = {word:uwords[word] for word in uwords if uwords[word] == max(uwords.values())}
    for word in final:
        print(final[word], " - ", word)
