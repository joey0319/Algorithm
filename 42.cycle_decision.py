# 서로소 집합을 이용한 사이클 판별 알고리즘

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

# 사이클 발생 여부 확인하기
cycle = False

for i in range(e):
    a, b = map(int, input().split())
    # 부모 노드가 같다면 사이클이 발생한것이다. 왜냐하면 간선 정보에 의해 a,b는 연결되어 있다고 입력이 들어왔고
    # 얘네 둘이 부모 노드가 같다면 a,b는 연결된 상태에서 a는 부모 c와 b도 부모 c와 연결되어 있으므로 a,b,c는 사이클이다.
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        # 부모노드가 다르면 union 연산을 수행한다.
        union_parent(parent, a, b)

if cycle:
    print('cycle 발생')
else:
    print('cycle 발생 안함')
