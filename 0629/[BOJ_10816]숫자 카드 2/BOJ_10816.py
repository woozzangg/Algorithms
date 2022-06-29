import sys 
sys.stdin = open('input1.txt') 
# input = sys.stdin.readline
# N = int(input())
# N_list = list(map(int ,input().split()))
# M = int(input())
# M_list = list(map(int ,input().split()))
#
# # for i in M_list:
# #     cnt = 0
# #     for j in N_list:
# #         if j == i:
# #             cnt += 1
# #     print(cnt, end=' ')
#
# M_index = [0]*M
# for i in range(len(M_list)):
#     M_index[i] = N_list.count(M_list[i])
# for i in M_index:
#     print(i, end=' ')

from sys import stdin
_ = stdin.readline()
N = map(int,stdin.readline().split())
_ = stdin.readline()
M = map(int,stdin.readline().split())
hashmap = {}
for n in N:
    if n in hashmap:
        hashmap[n] += 1
    else:
        hashmap[n] = 1

print(' '.join(str(hashmap[m]) if m in hashmap else '0' for m in M))