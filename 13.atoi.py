# 문자열을 입력받아서 int형으로 바꿔주는 함수
# int(char) 함수와 동일

def atoi(chr):
    i = 0
    for c in chr:
        i = i*10 + ord(c) - ord('0') # 이 방법을 통해 숫자를 순서에 맞게 넣을 수 있다.
    return i