# 2차원 리스트 형태로 표가 주어지고 최소값을 구하는 전형적인 백트래킹 문제
# 각 행을 재귀적으로 돌면서 한 행에서 어떠한 열을 선택하면 그 다음 열에서는 선택 못한다.(순열과 비슷)

def backtrack(i, cursum): # 처음 시작하는 열(i)와 현재 합계(cursum)을 인자로 받는다.
    global minV # 최소값은 아주큰값(ex 100000)으로 전역변수를 받아온다.
    if cursum > minV:  # 만약 현재 단계에서 현재 합계가 최소값보다 커버리면 다음칸은 갈필요가 없다. 어차피 더 크기 때문에 그래서 return 으로 중단
        return
    if i == N: # 행이 N이 되면 list index를 벗어나지만 현재까지(N-1행까지) 저장된 cursum은 비교가 가능하다.
        if minV > cursum: # 비교해서 여태까지 구했떤 minV보다 작으면 minV에 cursum을 저장해준다.
            minV = cursum
    else:
        for j in range(N):  # j는 열을 의미한다. 0부터 N-1까지 N개의 열중에 선택하는데
            if not visited[j]: # 아직 해당 열을 선택하지 않았다면
                visited[j] = True # 선택했다는 처리를 해주고
                backtrack(i+1, cursum + lst[i][j]) # 다음 행에 대해 함수를 재귀적으로 호출한다. 그때 cursum에는 더한값을 넘겨준다. / 여기서 계속 가는거는 깊이로 가는것
                visited[j] = False # 그리고 재귀적으로 호출이 모두 끝나고 돌아오면 해당 열을 다시 선택할 수 있어야 하므로 False처리 해준다. / 여기서 다음 for 문 j로 가는것은 너비로 가는것

lst = [
    [1,56,8,94],
    [98,5,36,4],
    [13,56,15,87],
    [55,6,87,9]
]
N = len(lst)
visited = [False] * N
minV = 10000
backtrack(0, 0)
print(minV)