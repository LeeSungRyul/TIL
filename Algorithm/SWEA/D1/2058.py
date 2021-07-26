def calc(num):
    lst = []
    while num > 0:
        lst.append(num % 10)
        n //= 10
    return sum(lst)

N = int(input())

print(calc(N))