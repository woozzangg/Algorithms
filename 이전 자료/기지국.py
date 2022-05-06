import sys
sys.stdin = open('기지국.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]

    print(arr[3][3])