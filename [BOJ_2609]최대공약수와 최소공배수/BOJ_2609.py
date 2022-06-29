import sys 
sys.stdin = open('input1.txt') 

N, M = map(int, input().split())
N_list = []
M_list = []
for i in range(1,N+1):
    if N % i == 0:
        N_list.append(i)

for i in range(1,M+1):
    if M % i == 0:
        M_list.append(i)
S_list = set(N_list) & set(M_list)

yak = max(S_list)
bae = yak * (N // yak) * (M // yak)
print(yak)
print(bae)
