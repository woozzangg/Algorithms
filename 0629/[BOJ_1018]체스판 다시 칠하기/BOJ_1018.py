import sys 
sys.stdin = open('input4.txt')
input = sys.stdin.readline

def sol1(a, b, c):
    cnt = 0
    for i in range(8):
        for j in range(8):

            if ((a+i + b+j) % 2) == 0:
                if arr[a+i][b+j] == c:
                    pass
                else:
                    cnt += 1
            else:
                if arr[a+i][b+j] != c:
                    pass
                else:
                    cnt += 1
    return cnt
def sol2(a, b, c):
    cnt = 0
    for i in range(8):
        for j in range(8):

            if ((a+i + b+j) % 2) == 0:
                if arr[a+i][b+j] == c:
                    pass
                else:
                    cnt += 1
            else:
                if arr[a+i][b+j] != c:
                    pass
                else:
                    cnt += 1
    return cnt

N, M = map(int, input().split())
arr = []
for i in range(N):
    s = input()
    arr.append(s)

ans = 64
for i in range(N-7):
    for j in range(M-7):
        B = 'B'
        W = 'W'
        w1 = sol1(i, j ,B)
        w2 = sol2(i, j, W)
        if w1 < w2:
            if ans > w1:
                ans = w1
        else:
            if ans > w2:
                ans = w2
print(ans)