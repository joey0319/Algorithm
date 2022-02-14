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

# 3. print문 end 사용하기

lst3 = [1,2,3,4,5,6,7]
for number in lst3:
    print(number, end = ' ')

# 위 방법은 코딩테스트에서 유용하게 사용 가능함
for tc in range(5):
    arr = [1,2,5,6,8,7,5,3,45]
    print('#{}'.format(tc+1), end = ' ')
    for number in arr:
        print(number, end = ' ')
    print()  # 이것은 그 다음 테스트 케이스 전에 밑줄로 내리기 위함

