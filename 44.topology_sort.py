# 위상정렬
# 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것 / 간선 몇번만에 도달할 수 있는지
# 진입차수 = 해당 노드에 들어오는 간선의 개수

from collections import deque

# 노드의 개수와 간선의 개수 입력받기
v, e = map(int, input().split())

# 모든 노드 진입차수 0으로 초기화
indegree = [0] * (v+1)

# 각 노드의 연결정보를 담을 연결리스트 정의
graph = [[] for _ in range(v+1)]

# 방향 그래프의 모든 간선 정보 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    # a에서 b로 갈 수 있다는 말
    graph[a].append(b)
    # b로 갔으므로 b의 진입차수 1 증가
    indegree[b] += 1

# 위상정렬 함수
def topology_sort():
    result = []
    q = deque()
    # 진입차수가 0이면 q에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    # q가 빌때까지 반복
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            # 연결된 간선 제거
            indegree[i] -= 1
            # 간선 제거 후 진입차수가 0인것 q에 삽입
            if indegree[i] == 0:
                q.append(i)
    # 결과 출력
    for i in result:
        print(i, end='')

topology_sort()

