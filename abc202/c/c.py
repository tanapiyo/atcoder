# 同じような処理を何度も行う」ような問題においては、「前もって計算しておく」
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
# n = 4
# a = [1, 1, 1, 1]
# b = [1, 1, 1, 1]
# c = [1, 2, 3, 4]

countmap = {}
answer = 0

# b[c]=ある値になるjの数を記憶しておいて、あとでjでひく
# ある数:でてくる個数
for i in range(n):
    if c[i] <= n:
        if b[c[i]-1] in countmap:
            countmap[b[c[i]-1]] += 1
        else:
            countmap[b[c[i]-1]] = 1

for j in range(n):
    if a[j] in countmap:
        answer += countmap[a[j]]

print(answer)
