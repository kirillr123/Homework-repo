import re
import functools
print("Введите целые неотрицательные числа, разделенные любым не цифровым литералом (пробел, запятая, %, буква и т.д.).")
a = input()
p = re.compile(r'-?[0-9]+')
print(functools.reduce(lambda a,b : int(a)+int(b), p.findall(a)))