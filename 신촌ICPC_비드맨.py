import sys
input = sys.stdin.readline

N = int(input())
arr = list()
for _ in range(N):
    arr.append(int(input()))

arr.sort()

temp = arr[0]
for i in range(N-1):

    # 처음
    if i == 0:
        max1 = arr.pop()
        max2 = arr.pop()
        temp = abs(max1-max2)
        continue

    # 나머지는
    max1 = arr.pop()
    temp = abs(temp - max1)


print(temp)
