import sys
sys.stdin = open('퍼펙트셔플.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(str, input().split()))
    ans_arr = []
    if len(arr) % 2 == 1:

        la = len(arr)//2 +1
    else: la = len(arr)//2
    arr_1 = arr[:la]
    arr_2 = arr[la:]
    for i in range(len(arr_2)):
        ans_arr.append(arr_1[i])
        ans_arr.append(arr_2[i])
    if len(arr_1) > len(arr_2):
        ans_arr.append(arr_1[len(arr_1)-1])
    print(f'#{tc}', *ans_arr)
