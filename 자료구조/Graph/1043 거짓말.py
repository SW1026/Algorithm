n, m = map(int, input().split())

know = set()
tmp = list(map(int, input().split()))
if tmp[0] == 0:
    print(m)
    exit(0)
know.update(tmp[1:])

parties = []
for i in range(m):
    party = list(map(int, input().split()))[1:]
    parties.append(party)

for _ in range(m):
    for party in parties:
        if know & set(party):
            know.update(party)
            continue

cnt = 0
for party in parties:
    if know & set(party):
        continue
    else:
        cnt += 1
print(cnt)

# set operation 이용
