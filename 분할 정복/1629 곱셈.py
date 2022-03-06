a, b, c = map(int, input().split())

def power(a, b):
    if b == 0:
        return 1
    if b % 2 == 1:
        return (power(a, b//2) ** 2 * a) % c
    else:
        return (power(a, b//2) ** 2) % c

print(power(a, b) % c)
