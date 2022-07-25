import sys 
sys.stdin = open('input1.txt') 

N, K = map(int, input().split())
arr = []
for i in range(2,N+1):
    arr.append(i)
cnt = 0
while True:
    a = arr[0]

    ans = 0
    while True:
        ans += a
        if ans in arr:
            arr.remove(ans)
            cnt += 1
        if cnt == K:
            print(ans)
            exit()

        if ans > N:
            break
        else:
            pass