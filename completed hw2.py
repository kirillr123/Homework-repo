print("Введите текст. Вводить можно любые слова, слоги, числа и их комбинации, разделенные пробелом")
a = input()
words = a.split()
words = list(dict.fromkeys(words))
for word in words :
    print(word, end=" ")