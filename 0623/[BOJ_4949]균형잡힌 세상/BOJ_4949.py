import sys 
sys.stdin = open('input1.txt') 

input = sys.stdin.readline

while True:
    arr = input()
    if arr == '.':
        break