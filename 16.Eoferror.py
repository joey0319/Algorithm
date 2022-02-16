# 파이썬에서 계속 입력을 받아야할 때 Eoferror가 뜨는데 이것을 예외 처리를 통해 해결
# input()은 입력이 없으면 Eoferror가 난다.

while True:
    try:
        a,b = map(int, input().split())
        print(a+b)

    except EOFError:
        break
