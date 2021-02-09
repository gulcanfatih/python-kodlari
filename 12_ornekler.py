a = 0
b = 1

for i in range(10):
    c = a
    a = a+b
    b = c
    print(b, end=" ")