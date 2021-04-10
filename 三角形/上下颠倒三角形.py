a = 0
while a < 5:
    m = 5
    while m > a:
        print('*',end='')
        m -= 1
    n = 0
    while n < a:
        print(' ', end='')
        n += 1
    print()
    a += 1