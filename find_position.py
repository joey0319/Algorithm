# 매트릭스 형식으로 주어질 때 좌표 찾는법

# 1이 적혀있는 곳이 현재 위치

# 아래와 같이 mat가 주어질때 위치 좌표는 (3,2) / 원점은 왼쪽하단
# mat은 N행 / M열의 행렬

N = 3
M = 5
mat = [
    [0,0,0,1,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

for i in range(-1,-N-1,-1):
    for j in range(M):
        if mat[i][j]  == 1:
            position = (j,-i-1)
print(position)

