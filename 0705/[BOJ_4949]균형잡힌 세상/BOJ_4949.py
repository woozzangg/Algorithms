import sys
sys.stdin = open('input1.txt')
#
# while True:
#     word = input()
#     if word == '. ':
#         break
#     stack = []
#     for i in range(len(word)):
#         if word[i] == '(' or word[i] == ')' or word[i] =='[' or word[i] ==']':
#             stack.append(word[i])
#     # print(stack)
#     q = []
#     ans = 0
#     for i in stack:
#         if i == '(' or i=='[':
#             q.append(i)
#         elif i == ')':
#             if q and q[-1] == '(':
#                 q.pop()
#             else:
#                 ans = -1
#         elif q and i == ']':
#             if q[-1] == '[':
#                 q.pop()
#             else:
#                 ans = -1
#     if ans == 0:
#         print('yes')
#     elif ans == -1:
#         print('no')

# import sys

while True:
    arr=[]
    balance = sys.stdin.readline().rstrip()
    if balance == '.': break
    for i in balance:
        if i =='(' or i ==')' or i =='[' or i ==']':
            arr.append(i)
    arr2 = ''.join(arr)
    for i in range(len(arr2)//2):
        arr2 = arr2.replace('()', '')
        arr2 = arr2.replace('[]', '')
    if len(arr2) == 0: print('yes')
    else: print('no')