x1 = 1
x2 = 2
y = 0

while x2 < 4000001:
    if x2%2 == 0:
        y += x2
    temp = x2
    x2 += x1
    x1 = temp


print(y)