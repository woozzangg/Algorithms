import sys 
sys.stdin = open('input1.txt') 

# N = int(input())
# fn_list = []
# age_list = []
#
# for i in range(N):
#     a = input()
#     fn_list.append(a)
#     if a[1] == ' ':
#         age_list.append(int(a[0]))
#     elif a[1] == ' ':
#         age_list.append(int(a[0:1]))
#     else:
#         age_list.append(int(a[0:2]))
# print(age_list)
#
# for i in range(N):
#     min_age = 201
#     min_index = 0
#     for j in range(N):
#         if min_age > age_list[j]:
#             min_age = age_list[j]
#             min_index = j
#     print(fn_list[min_index])
#     age_list[min_index] = 200


n = int(input())
member_lst = []

for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    member_lst.append((age, name))

member_lst.sort(key = lambda x : x[0])	## (age, name)에서 age만 비교

for i in member_lst:
    print(i[0], i[1])