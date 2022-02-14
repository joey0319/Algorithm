# 각 자리수를 더하는 코드

total = 0
num = 15849

for j in str(num): # 숫자를 문자로 만들어서 숫자 하나씩 iterable하게 만듬
    total += int(j)

print(total)

# 여러개의 숫자가 주어질때 각자리수를 더하는 코드

for i in [15,158,698,5487,6669989]:
    total = 0
    for j in str(i):
        total += int(j)
    print(total)