import sys 
sys.stdin = open('input1.txt') 

T = int(input())
N = input()
ans = 0
for i in range(T):
    ans += (ord(N[i])-96) * (31 ** i)
print(ans)

print(ord('a') % M)