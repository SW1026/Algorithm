n = input()
a = list(n)
a_int = list(map(int, list(n)))

if '0' not in n or sum(a_int) % 3 != 0:
    print(-1)
    exit(0)

a.sort(reverse=True)
print(''.join(a))


# 3의 배수 : 각 자리 수를 더해서 3으로 나누어 떨어짐
