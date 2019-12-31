print("Введите неотрицательные целые числа, разделенные через пробел")
ints = [int(num) for num in input().split() if num.isdigit()]
ints.sort()
ints = list(dict.fromkeys(ints))
if ints:
    for x in range(1, 777**777):
        if x > len(ints):
            print(max(ints)+1)
            break
        elif ints[x-1] != x:
            print(x)
            break
