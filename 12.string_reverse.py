# 역순으로 추가해주는 방법
def myreverse(char):
    word = ''
    for i in range(len(char)):
        word = char[i] + word
    return word

print(myreverse('안녕하세요'))


# 대칭적으로 문자를 하나하나 교환해주는 방법
def reverse(char):
    nlst = list(char)  #list()는 iterable 한것을 하나하나 리스트에 넣어준다.
    n = len(char)
    for i in range(n//2):
        nlst[i], nlst[n-1-i] = nlst[n-1-i], nlst[i]

    nchar = ''.join(nlst)
    return nchar

print(reverse('반갑습니다'))