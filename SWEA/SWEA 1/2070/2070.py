import sys
sys.stdin = open('input.txt')

T = int(input())
ans = ''
for tc in range(1, T+1):
    a, b = map(int, input().split())
    if a < b:
        ans = '<'
    elif a > b:
        ans = '>'
    else: ans = '='
    print(f'#{tc} {ans}')