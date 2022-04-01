# 반복문을 이용하여 조합을 생성하기

def f(i,j,k):
    print(i,j,k)

N = 10
R = 3
for i in range(N-2): # 3개이기때문에 첫번째 고를 숫자의 인덱스 여기까지만 본다
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            f(i,j,k)


# 재귀를 사용해 조합을 만들어보자

def nCr(n, r, s):
    if r == 0:
        print(comb)
    else:
        for l in range(s, n-r+1):
            comb[r-1] = A[l]
            nCr(n, r-1, l+1)

n = 5
r = 3
comb = [0] * 3
A = list(range(1,n+1))
nCr(n,r,0)

# 2차원 리스트에서 조합적으로 선택하려면
# 1차원 리스트에 2차원 리스트의 모든 좌표를 (2,3)이런식으로 저장한 뒤
# 똑같은 재귀 함수를 사용하여 n개를 뽑아 사용한다.

