# 1. 끝 시간 2. 시작 시간 우선 순위로 sort를 한다. (시작시간이 우위여도 안된다.)

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

a.sort(key=lambda x:(x[1], x[0]))
cnt = 0
end = 0
for i in range(n):
    if a[i][0] >= end:
        cnt += 1
        end = a[i][1]
print(cnt)









# 끝나는 시간만 sort할 경우 문제가 생기는 예제
# 7
# 1 4
# 3 5
# 2 5
# 5 5
# 4 5 => 이 값이 count 되지 않는다.
# 0 6
# 5 7

########### 처음 코드는 이렇게 짰는데 (시간 초과),
########### (끝나는 시간, 시작 시간)으로 정렬해야 O(n)으로 줄일 수 있는 아이디어를 추가했다.

# # 시작 시간을 기준으로 sort한 후(오름차순) 각 케이스에 대해 cnt를 세고 append한다.
# # cnt 리스트 중 가장 작은 값을 출력
#
# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
#
# a.sort()
# cnts = []
#
# cnt = 0
# start = 0
# end = 0
# for i in range(n):
#     for j in range(n):
#         if i < j and end <= a[j][0]:
#             cnt += 1
#             start = a[j][0]
#             end = a[j][1]
#     cnts.append(cnt)
#     cnt = 0
#     start = 0
#     end = 0
# print(max(cnts))
