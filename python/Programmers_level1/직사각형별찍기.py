a, b = map(int, input().strip().split(' '))

for i in range(int(b)):
    for j in range(int(a)):
        print('*', end = '')
    print()