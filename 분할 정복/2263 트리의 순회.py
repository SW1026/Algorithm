import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

in_order_idx = {in_order[i]: i for i in range(n)}

# 전위 순회 : 루트 -> 오 -> 왼
def find_tree(i_start, i_end, p_start, p_end):
    if (i_start > i_end) or (p_start > p_end):
        return

    # 서브 Tree 마다 루트 찾아서 출력
    root = post_order[p_end]
    print(root, end=" ")

    left = in_order_idx[root] - i_start
    right = i_end - in_order_idx[root]

    # 왼쪽 서브 트리 방문
    find_tree(i_start, i_start+left-1, p_start, p_start+left-1)
    # 오른쪽 서브 트리 방문
    find_tree(i_end-right+1, i_end, p_end-right, p_end-1)

find_tree(0, n-1, 0, n-1)


# 메모리초과 => python으로 제출
