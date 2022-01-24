n = int(input())
p = list(map(int, input().split()))

p.sort()
sum = 0
ssum = 0
for i in range(n):
    sum += p[i]
    ssum += sum
print(ssum)
