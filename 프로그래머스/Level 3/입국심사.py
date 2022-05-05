def solution(n, times):
    answer = 0
    times.sort()
    
    len_times = len(times)
    start = times[0]
    end = times[-1] * n
    
    while start <= end:
        mid = (start + end) // 2
        num = 0
        for time in times:
            num += mid // time
            
        if num >= n:
            answer = mid
            end = mid - 1
        elif num < n:
            start = mid + 1

    return answer
