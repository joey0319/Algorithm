# 리스트 안의 정수를 공백한칸씩 두고 출력하기

# 1. List comprehension / join 메서드 활용

lst = [1,2,3,4,5,67,8]
tmp = [str(c) for c in lst]
ans = ' '.join(tmp)
print(ans)

# 2. map / join 메서드 활용

lst2 = [1,2,3,4,5,6,7]
tmp2 = list(map(str, lst2))
ans2 = ' '.join(tmp2)
print(ans2)

