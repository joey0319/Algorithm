# N X N 행렬이 주어질 때 그 내부에서 가능한 모든 M X M 행렬의 값들을 탐색하고 싶을 때

N_list = [
    [1,1,1,1,1],
    [1,0,1,0,0],
    [1,1,0,0,0],
    [0,0,1,1,0],
    [0,1,1,1,0]
]
N = 5
M = 3


section_list = []
for i in range(N-M+1):  
    for j in range(N-M+1): # 시작점의 좌표를 좌측상단 기준으로 보고 탐색할것
        section = [] # 한세트를 탐색하면 초기화 초기화 위치 주의
        for k in range(i, i+M):
            for l in range(j, j+M):
                section.append(N_list[k][l])
        section_list.append(section)

print(section_list)
        


