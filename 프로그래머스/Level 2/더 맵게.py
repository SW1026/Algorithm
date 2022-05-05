from heapq import heappop, heappush

def solution(scoville, K):
    answer = 0
    sco = []
    for _ in scoville:
        heappush(sco, _)
    
    while True:
        if len(sco) == 1 and sco[0] < K:
            answer = -1
            break
        low = heappop(sco)
        if low < K:
            low2 = heappop(sco)
            tmp = low + low2 * 2
            heappush(sco, tmp)
            answer += 1
        else:
            break
    return answer
