# 큐 자료구조를 직접 구현해보자 append / pop 활용하지 않고

# 1. 먼저 공백 큐(크기를 미리 정해줘야 함)를 생성 / front와 rear 초기화
Q = [0] * 101
front = -1
rear = -1

#2. 공백상태 검사 함수 생성
def isEmpty():
    if front == rear:
        return True
    else:
        return False

#3. 포화상태 검사 함수 생성
def isFull():
    if rear == len(Q) - 1: # rear가 주어진 배열의 마지막 인덱스이면 포화상태임
        return True
    else:
        return False

#4. 삽입 함수 생성
def enQueue(n):
    if isFull():
        return
    else:
        rear += 1
        Q[rear] = n

#5. 삭제 함수 생성
def deQueue(n):
    if isEmpty():
        return
    else:
        front += 1
        return Q[front]