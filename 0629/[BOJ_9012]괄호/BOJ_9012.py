import sys 
sys.stdin = open('input1.txt') 
# input = sys.stdin.readline

N = int(input())
for i in range(N):
    arr = input()
    stack = []
    k = len(arr)
    for j in range(k):
        if arr[j] == '(':
            stack.append(arr[j])
        elif arr[j] == ')':
            if stack:
                stack.pop()
            else:
                stack.append('1')
                break
    if stack:
        print('NO')
    else:
        print('YES')