# mXm 행렬의 시계방향 90도 회전 이것을 함수화 해서 계속 돌리면 된다.
# 참고한 페이지 : https://bcp0109.tistory.com/150
# 1. 가운데에 가로선을 긋고 그 선을 기준으로 숫자를 교환해준다.
lst = [[1,2,3],[4,5,6],[7,8,9]]
m = len(lst)
line = m // 2 #1의 값이 나오는데 1행이 가로선이라는 얘기

for i in range(m):
    for j in range(m//2):
        lst[m-j-1][i], lst[j][i] = lst[j][i], lst[m-j-1][i]

# 2. 대각선을 긋고 그 선을 기준으로 숫자를 교환해준다. 좌상우하 대각선 기준이면 시계방향 90도회전이고
# 우상좌하 대각선 기준이면 반시계 방향 90도 회전이다.

# 시계방향 90도 회전
for i in range(m):
    for j in range(m):
        if i < j:
            lst[i][j], lst[j][i] = lst[j][i], lst[i][j]

print(lst)