#플로이드 워셜 알고리즘 (모든 지점에서 모든지점으로 가는 최단거리 구할 때 사용)

INF = int(1e9)

# 노드 개수 간선 개수 입력 받기
n, m = map(int, input().split())

# 최단거리 저장할 2차원 리스트 생성 및 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화(2차원리스트의 대각선)
for i in range(1, n+1):
    graph[i][i] = 0

# 각 간선의 정보를 입력받고 그 값으로 초기화 a에서 b로가는 비용이 c라고 입력이 주어질 때 입력에 없으면 무한으로 될 것이고 차차 갱신될 것이다.
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
# 점화식 : min(D_ab, D_ak + D_ab) // a에서 b로 바로 가는것과 k를 거쳐 가는것중 작은것을 선택한다.
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])