# LCS 알고리즘
# 부분 수열은 연속되지 않아도 된다.
'''
예를 들어 A = ACAYKP, B = CAPCAK라면
공통 부분 수열을 찾는 과정은 공백을 삽입하는 과정과 같다.
A = " A CAYKP"
B = "CAPCA K " 이런식으로 하면 ACAK가 공통 부분수열로 추출된다.
일치의 경우는 3가지로 나눌 수 있다.
1. A의 가장 마지막 문자와 B의 가장 마지막 문자가 일치하는경우
2. A의 가장 마지막 문자와 B의 가장 마지막 문자가 일치하지 않아 공백을 A의 오른쪽에 삽입하는 경우
3. A의 가장 마지막 문자와 B의 가장 마지막 문자가 일치하지 않아 공백을 B의 오른쪽에 삽입하는 경우
'''

# dp[i][j] = A가 i까지 B가 j까지 있을 때 LCS의 길이라고 정의한다.
# 만약 A[i] == B[j]라면 dp[i][j] = dp[i-1][j-1] + 1
# 만약 A[i] != B[j]라면 dp[i][j] = max(dp[i][j-1], dp[i-1][j])
# dp[i][j-1]은 A의 오른쪽에 공백삽입, dp[i-1][j]는 B의 오른쪽에 공백삽입
a = input()
b = input()
n = len(a)
m = len(b)
a = " " + a
b = " " + b
d = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if a[i] == b[j]:
            d[i][j] = d[i-1][j-1] + 1
        else:
            d[i][j] = max(d[i-1][j],d[i][j-1])
print(d[n][m])