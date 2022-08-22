# 수정 전
def find_parent(parent, x):
    # 루트 노드 아니면 찾을 때까지 재귀 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


# 수정 후
def find_parent(parent, x):
    # 루트 노드 아니면 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
