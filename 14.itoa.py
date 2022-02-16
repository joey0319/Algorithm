# 숫자를 전달 받아 문자형으로 바꿔주는 코드
# 숫자가 음수일때와 양수일때 나눠서 계산

def itoa(num):
    if num >= 0:
        result = ''
        mok = 1
        while mok != 0:
            remainder = num % 10
            mok = num // 10
            result = chr(48 + remainder) + result #chr(48)은 '0'이므로
            num = num // 10

    else:
        result = ''
        num = -num
        mok = 1
        while mok != 0:
            remainder = num % 10
            mok = num // 10
            result = chr(48 + remainder) + result
            num = num // 10
        result = '-' + result
    return result

print(itoa(156), type(itoa(156)))
print(itoa(-435), type(itoa(-435)))
