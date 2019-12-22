import re
sum = 0
def ispalindromic10(i):
    if str(i) == str(i)[::-1]:
        return True
    else:
        return False

def ispalindromic2(i):
    if str(re.sub('(0b)', '', bin(i))) == str(re.sub('(0b)', '', bin(i))[::-1]):
        return True
    else:
        return False


for i in range(1,1_000_000):
    if ispalindromic10(i):
        if ispalindromic2(i):
            sum = sum+i

print("Ответ - число: ", sum)