# 전, 중, 후위 순회
# 딕셔너리로 구현
# 리스트로는 0,1,2 인덱스를 만들어서 구현(자신, 자식1, 자식2 => 이대로 순회)

n = int(input())
tree = {}
for _ in range(n):
    x, y, z = input().split()
    tree[x] = [y, z]

def pre_order(root):
    if root != ".":
        print(root, end='')
        pre_order(tree[root][0])
        pre_order(tree[root][1])
    return


def in_order(root):
    if root != ".":
        in_order(tree[root][0])
        print(root, end='')
        in_order(tree[root][1])
    return

def post_order(root):
    if root != ".":
        post_order(tree[root][0])
        post_order(tree[root][1])
        print(root, end='')
    return

pre_order("A")
print()
in_order("A")
print()
post_order("A")
