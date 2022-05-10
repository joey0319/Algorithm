# 크루스칼 알고리즘
# 가장 적은 비용으로 모든 노드를 연결할 수 있는 방법
# 사이클을 발생시키면 안된다

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

# 선택된 간선을 담을 리스트 정의 / 최종비용 result 정의
edges = []
result = 0

# 모든 간선 정보 입력 받기
for _ in range(e):
    # a에서 b로 연결된 것의 비용이 cost라는 의미
    a, b, cost = map(int, input().split())
    edges.append((cost,a,b))

# 간선을 비용을 기준으로 정렬
edges.sort()

# 간선을 비용이 적은 순서대로 하나씩 확인하면서 사이클이 발생하지 않을 때만 집합에 포함시킨다.
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(a, b)
        result += cost

print(result)