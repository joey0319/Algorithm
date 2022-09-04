'''
3 5 7 9 15
15 9 7 5 3 을 재귀호출로 출력해보자
'''

def f(i):
    if i == len(lst):
        print()
        return
    print(lst[i], end = ' ')
    f(i+1)
    print(lst[i], end = ' ')

lst = [3,5,7,9,15]
f(0)