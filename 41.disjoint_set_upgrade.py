# 경로 압축 기법을 적용하여 개선된 서로소 집합 알고리즘
def find_parent(parent, x):
    # 루트 노드가 아니라면(처음에 parent 테이블은 자기 자신을 부모로 갖고 있다고 초기화 되어 있음)
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    # 합치는 노드번호의 부모를 찾는다.
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 둘중 작은 숫자를 부모로 한다.
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

#노드와 간선의 개수 입력받기
v, e = map(int, input().split())

# 부모 테이블 만들고 자기자신을 부모로 초기화
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

#unoin 연산 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합을 출력하면 그 집합이 동일할 경우 동일 집합에 속해있다는 의미
for i in range(1, v+1):
    print(find_parent(parent, i), end='')