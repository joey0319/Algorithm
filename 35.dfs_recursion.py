# 인접행렬이 주어질 때 dfs를 재귀로 구현해보자

def dfs1(i): # i번 노드부터 탐색을 시작하라는 뜻
    visited[i] = 1
    print(i, end = ' ')
    # i 에 인접한 모든 노드에 대해
    for w in range(V+1):
        if adjM[i][w] == 1 and not visited[w]:
            dfs1(w)

# 인접 리스트를 이용하는 방법
def dfs2(v, V): # V는 노드의 수 v는 시작점
    visited[v] = 1
    print(v, end = ' ')
    for w in adjL[v]:
        if not visited[w]:
            dfs2(w,V)


# 입력이 주어질 때 인접행렬을 나타내기
'''
6 8
0 1 0 2 0 5 0 6 5 3 4 3 5 4 6 4
정점이 6개 있고 간선은 8개 있고 다음 줄은 출발 도착 노드순으로 나타냄
'''

# 1. 방향이 없는 그래프
V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjM = [[0] * (V+1) for _ in range(V+1)] # 인접행렬

for i in range(E):
    n1, n2 = arr[i*2], arr[i*2 + 1]
    adjM[n1][n2] = 1 # 연결되어 있으면 1로 안되어 있으면 0으로 표기
    adjM[n2][n1] = 1 # 무향이기 때문에 두개 다 1로 바꿔준다.
    # 방향성이 있으면 한줄만 1로 바꿔줘야 한다.
    # 보통 행을 출발점 열을 도착점이라고 생각한다.

# adjL을 나타내기 0과 연결된 번호를 저장해주는 방식
adjL = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjL[n1].append(n2) # 유향이면 이것 하나만
    adjL[n2].append(n1) # 무향이면 이것 둘다 추가해주느 방식

visited = [0] * (V+1)
dfs1(0)
dfs2(0,V)