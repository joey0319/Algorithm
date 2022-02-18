# 에라토스체네스의 체로 소수 구하기 2부터 N까지
# N이 커질수록 for문으로 다 나눠보는 방식은 사용하기 어렵다.


prime = [True]*(N+1) #일단 모든 수를 소수라고 본다 소수면 True 0과 1 포함한 리스트
i = 2
while i**2 <= N:  # 판별은 i가 루트N보다 작을때까지만 하면 된다.
    if prime[i] == True:
        for j in range(2*i,N+1,i):  # 2i부터 i간격으로니까 i의 배수가 된다.
            prime[j] == False #i가 소수라면 그 배수만큼을 합성수라고 바꿔준다.

prime[0] = False
prime[1] = False # 0과1은 소수가 아니므로 False로 바꿔준다.

print(prime) # prime에서 값이 True인 것의 index는 소수이다.