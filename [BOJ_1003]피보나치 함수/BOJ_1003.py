import sys 
sys.stdin = open('input2.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


# def fibo(n):
#     global zero, one
#     if n == 0:
#         zero += 1
#     elif n == 1:
#         one += 1
#     else:
#         fibo(n-1)
#         fibo(n-2)
#
# N = int(input())
#
# for i in range(N):
#     zero = 0
#     one = 0
#     n = int(input())
#     fibo(n)
#     print(zero, one)

zero = [1, 0, 1]
one = [0, 1, 1]


def fibonacci(num):
    length = len(zero)
    if num >= length:
        for i in range(length, num + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print('{} {}'.format(zero[num], one[num]))


T = int(input())

for _ in range(T):
    fibonacci(int(input()))