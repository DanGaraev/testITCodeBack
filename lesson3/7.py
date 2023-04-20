p = int(input())
i = 1
a = 0
b = 1
c = a + b
if p == 1:
    print(c)
else:
    while i < p:
        c = a + b
        a = b
        b = c
        i += 1
    print(c)