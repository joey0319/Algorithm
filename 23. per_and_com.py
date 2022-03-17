# 파이썬 내부 itertools활용 / 순열 조합 쉽게 구할 수 있다.

from itertools import permutations
from itertools import combinations

# 사용법
# permutation(lst, r) lst에는 대상 숫자들이 있고 r은 몇개 뽑을지 결정 / 순열 및 조합은 튜플 형태로 저장된다.
lst = [1,2,3,4]
a = list(permutations(lst, 2))
b = list(combinations(lst,2))
print(a)
print(b)

'''
결과값
[(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]
[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

'''