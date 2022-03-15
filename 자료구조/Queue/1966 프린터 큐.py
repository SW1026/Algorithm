T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    # m은 인덱스임
    a = list(map(int, input().split()))
    c = [0] * n

    cnt = 1
    real_order = m
    while a:
        idx = a.index(max(a))
        if idx == real_order:
            # 정답 발견
            print(cnt)
            break
        elif real_order > idx:
            # 만약 현 idx 3이고 나중 idx 4이면 real_order 가 0이 됨
            real_order -= (idx + 1)
        else:
            real_order = (len(a)-1) - idx + real_order

        # 0부터 idx 전까지 지워 주고 뒤에 추가해 줌
        for _ in range(idx):
            tmp = a[0]
            del a[0]
            a.append(tmp)
            
        # idx 없애 주기
        del a[0]

        cnt += 1
