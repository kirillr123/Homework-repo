import math
[[print("Project Euler problem 9 solution:", a * b * (1000 - a - b)) for a in range(1000) if
  1000 - a - b == math.sqrt(a ** 2 + b ** 2) and a < b < 1000 - a - b] for b in range(1000)]

