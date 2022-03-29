# 튜플이나 리스트에서 두번째 값을 기준으로 정렬하는 방법

lst = [(1,2), (3,6), (5,10), (10,4), (100,1)]
lst.sort(key=lambda x: x[1], reverse=True)
print(lst)