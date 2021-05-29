# まず頭がaかbか決める。aグループの個数は、aが4つbが7つなら、a3つが自由でC(3+7,7)通り
# この操作を続けて文字列を決める
# 二項定理は事前に計算してもいい
A, B, K = map(int, input().split())

# まず二項定理表をつくっちゃう
n = A+B
C = []
for i in range(n+1):
    C.append([0] * (n+1))

C[0][0] = 1
for i in range(n+1):
    C[i][0] = 1
    for j in range(1, n+1):
        C[i][j] = C[i-1][j-1] + C[i-1][j]

a = A
b = B
ans = ''
for i in range(n):
    if K <= C[a+b-1][a-1]:
        ans += 'a'
        a -= 1
    else:
        K -= C[a+b-1][a-1]
        ans += 'b'
        b -= 1

print(ans)
