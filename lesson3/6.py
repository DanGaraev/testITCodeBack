a = int(input())
counter = 0
i = 1
while i <= a:
    if a % i == 0:
        counter += 1
    i += 1
if counter > 2:
    print('Составное')
else:
    print('Простое')
