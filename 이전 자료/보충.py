arr=[3,6,5,8,5,3,5,8,5,3,3,1,1,3]
pattern=[3,5,8,5]

# for i in range(11):
#     if arr[i] == pattern[0] and arr[i+1] == pattern[1] and arr[i+2] == pattern[2] and arr[i+3] == pattern[3]:
#         print('success')
#     else: pass
#
#     for로 모든 칸 스캐닝( 양쪽이 1이면 카운트 0 )
#
# arr 배열 안에 pattern 이 존재 하는지 .. 존재 여부를 출력!!

flag=0
def isPattern(index):
    for i in range(4):
        if pattern[i]!=arr[index+i]:
            return 0
    return 1

for i in range (11):  # 0 ~ 10
    ret=isPattern(i)
    if ret==1:
        flag=1
        break
if flag:
    print("존재함")
else:
    print("패턴은 존재하지 않음")