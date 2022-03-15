#dfs 알고리즘
# 노드와 경로가 주어질 때 시작점(s)부터 목표점(G)까지 갈 수 있는지 파악

def dfs(s):
    st = []
    visited = [False] * N   #N은 노드의 수

    st.append(s)  #출발점 s를 스택에 푸쉬해준다.
    visited[s] = True #방문점 리스트에 s를 추가한다.

    while st:
        s = st.pop()  #pop()은 리스트에서 마지막 원소를 삭제하고 삭제한 원소를 반환해준다.
        if s == G:
            return 1 # G(목표점)까지 도착하면 1을 리턴한다.
        else:
            for e in close[s]:  # close[s]에는 s에서 갈 수 있는 노드의 번호가 들어있다.
                if visited[e] == False:  # e를 방문하지 않았다면
                    st.append(e)    # 스택에 e를 추가하고 / for문을 돌면서 다 추가하는 이유는 그 뒤로 조건에 만족이 안되면 pop을 해서 지워 주고 저장되어 있던 다른 원소를 검사할 것이기 때문
                    visited[e] == True # visited에도 추가하여 방문했다고 표시한다.

    return 0 #스택이 공백이 될 때까지 다 돌았는데도 조건을 만족하는 경로가 없으면 0을 리턴한다.

# 1 2 2 3 3 4 5 4 이런식으로 주어지면 1에서 2로, 2에서 3으로, 3에서 4로 갈 수 있다는 뜻
# 이것을 close 리스트에 저장해준다.
lst = [1,2,2,3,3,4,5,4]
close = [[] for _ in range(N)] # N은 노드의 수
for i in range(0,len(lst),2): #2간격으로 lst를 보면서 어디로 갈 수 있는지 append한다.
    close[i].append(lst[i+1])