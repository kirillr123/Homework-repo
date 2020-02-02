import re


def ispalindromic10(a):
    return str(a) == str(a)[::-1]


def ispalindromic2(a):
    return str(re.sub('(0b)', '', bin(a))) == str(re.sub('(0b)', '', bin(a))[::-1])


x = 0
for i in range(1, 1_000_000):
    if ispalindromic10(i):
        if ispalindromic2(i):
            x = x+i

print("Ответ - число: ", x)
