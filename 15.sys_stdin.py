# 입력을 빠르게 받고 싶을 때
# 여러 줄을 입력할 때 시간초과가 날 수 있기때문에 사용해 줄 수 있다.

import sys

for i in range(10000):
    a, b = map(int, sys.stdin.readline().split())
