# 파이썬 약수의 개수 구하는 코드 /  약수 판별 코드 / 소수 판별 코드

N = int(input)

result = []
for number in range(1,N+1):  # N을 1~N까지 모든 수 number로 나눈다.
    if N % number == 0:      # number로 나누었을 때 나머지가 0이면 number는 N의 약수이다.
        result.append(number)

print(result)  # 약수 리스트를 출력한다.
print(len(result))  # 약수의 개수를 출력한다. / 만약 약수의 개수가 두개라면 N은 소수이다.
