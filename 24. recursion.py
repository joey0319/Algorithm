# 재귀의 기본형

def f(i, N):
    if i == N:
        return
    else:
        f(i+1, N)

# 배열 A = [10,20,30]을 재귀를 활용해 복사해 보자
A = [10,20,30]
B = [0,0,0]
def g(i, N):
    if i == N:
        return
    else:
        B[i] = A[i]
        g(i+1, N)  # if 칸에 리턴 값이 없고 리턴만 있으면 else칸에 리턴 값 필요 없음
g(0,3)
print(B)

# 재귀를 활용하여 배열 안에 특정값이 있는지 찾아보자
# 배열 C에 V가 있으면 1리턴 없으면 -1 리턴
C = [7,2,5,4,1,3]
n = len(C)
V = 5
def h(i, n, V):
    if i == n:
        return -1
    elif C[i] == V:
        return 1
    else:
        return h(i+1, n, V)  # return 값을 전달 해줘야한다. / if elif 칸에 return 값이 있으면 else칸에서도 reuturn 필요

print(h(0,n,V))

# 길이가 3인 배열에 0또는 1을 삽입하는 모든경우의 수
N = 3
A = [0] * N
# A[i]에 0 또는 1을 채우는 함수
def F(i, N):
    if i == N:
        print(A)
    else:
        for j in range(2): # A에 0또는 1을 넣고 그 다음 행 채우는 함수를 호출
            A[i] = j       # range 안의 숫자의미는 0또는 1 두가지라는 의미이다.
            F(i+1, N)
F(0,N)

# 1,2,3을 중복사용해서 3자리수 만들기 (중복순열)

N = 3
A = [0] * N
def G(i, N):
    if i == N:
        print(A)
    else:
        for j in range(1,4):
            A[i] = j
            G(i+1, N)
G(0,N)

# 1부터 K까지를 중복사용해 3자리수 만들기

N = 3
K = 5
A = [0] * N
def H(i, N, K):
    if i == N:
        print(A)
    else:
        for j in range(1,K+1):
            A[i] = j
            H(i+1, N, K)

H(0, N, K)

# 1부터 k를 중복사용하여 3자리수를 만들어 V값을 만들 수 있으면 1 리턴 없으면 0 리턴
N = 3
K = 5
A = [0] * N
V = 115
def find(i, N, K, V):
    if i == N:
        if A == [1,1,5]:
            return 1
        else:
            return 0
    else:
        for j in range(1,K+1):
            A[i] = j
            if find(i+1, N, K, V) == 1: # 찾았음을 그 위에 함수에도 전달해줘야 하므로 1을 리턴
                return 1
        return 0  # for 문을 다 돌아도 탐색에 실패하면 그 위의 함수에도 실패정보를 전달해야 하므로 0 리턴
    
print(find(0,N,K,V))


# A의 부분집합 중 합이 K인 부분집합의 개수(cnt) 구하기

A = [1,2,3,4,5,6,7,8,9,10]
N = len(A)
cnt = 0
K = 55
def sub(i, N, s, K):  # s = i-1원소까지 고려된 부분집합의 합
    global cnt
    if i == N:
        if s == K:
            cnt += 1 # 부분집합의 합이 K와 같으면 카운트 1 증가
    else:
        sub(i+1, N, s+A[i], K)  # 이경우는 A[i]가 포함됐다는 의미
        sub(i+1, N, s, K)   # 이경우는 A[i]가 포함 안됐다는 의미 그래서 안더해줌

sub(0,N,0,K)
print(cnt)

        








