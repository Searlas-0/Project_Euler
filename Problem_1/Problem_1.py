x = 1000
y = 0

while x > 0:
    x -= 1
    if x%3 == 0 or x%5 == 0: 
        y += x


print(y)