# 순열 p[n]을 채우는 함수, k는 배열의 크기, m은 주어진 숫자
def f(n, k, m):
    if n == k:
        print(p)
    else:
        for i in range(m):  # used에서 사용되지 않은 숫자 검색
            if used[i] == 0: # 앞에서 사용되지 않은 경우
                used[i] = 1 # 사용함으로 표시
                p[n] = a[i]
                f(n+1, k, m)
                used[i] = 0 # a[i]를 다른자리에서 사용해아 하므로 원상복귀시켜 줌

a = [1,2,3,4,5]
p = [0] * 3
used = [0] * 5
f(0, 3, 5)

