# 2차원 리스트를 1차원 리스트로 변환하기
# 예를들어 [[1,2],[2,3]]을 [1,2,2,3]으로 변환하기
# list comprehension 이용

lst = [[1,2],[2,3]]
nlst = [y for x in lst for y in x]
# 이렇게 써주면 for x in lst부터 해석해서 x에는 [1,2] / [2,3]이
# 들어오고 그 다음 for y in x를 해석해서 y에는 1,2,2,3이 들어와서
# 최종적으로 리스트안에 y가 저장된다.
print(nlst)