import sys 
sys.stdin = open('input1.txt') 

N, K = map(int, input().split())
ans1 = 1
ans2 = 1
for i in range(K):
    ans1 *= N-i
    ans2 *= i+1
print(ans1 // ans2)
