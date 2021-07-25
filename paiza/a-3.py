import copy
# https://techblog.recochoku.jp/5158
# コピーしないと配列の同じところ全部かわる、だから[[0]*W]*Hみたいな初期化をすると全部同じ値を参照する感じになりそう
# 幅優先探索
# 幅優先探索では、マス目の距離が必ず昇順で現れること
H, W, N = map(int, input().split())
s = [list(input()) for _ in range(H)]
s_num = copy.copy(s)
my_p = []
dists = []

for i in range(N):
    dists.append(int(input()))

# 初期位置をmyqに入れる
for y in range(H):
    for x in range(W):
        if s[y][x] == "*":
            s[y][x] = "*"
            s_num[y][x] = 0
            my_p.append([y, x, 1])

# キューがある間
while my_p:
    [y, x, n] = my_p.pop(0)
    if y > 0 and s[y - 1][x] == ".":
        s[y - 1][x] = "*"
        s_num[y-1][x] = n
        # s[y - 1][x] = n
        my_p.append([y-1, x, n+1])
        # operation[y-1][x] += 1
    if y < H - 1 and s[y + 1][x] == ".":
        s[y + 1][x] = "*"
        s_num[y+1][x] = n
        # s[y + 1][x] = n
        my_p.append([y+1, x, n+1])
        # operation[y+1][x] += 1
    if x > 0 and s[y][x - 1] == ".":
        s[y][x - 1] = "*"
        s_num[y][x-1] = n
        # s[y][x - 1] = n
        my_p.append([y, x-1, n+1])
        # operation[y][x-1] += 1
    if x < W - 1 and s[y][x + 1] == ".":
        s[y][x + 1] = "*"
        s_num[y][x+1] = n
        # s[y][x + 1] = n
        my_p.append([y, x+1, n+1])
        # operation[y][x+1] += 1

for y in range(int(H)):
    for x in range(int(W)):
        if(s_num[y][x] in dists):
            print("?", end="")
        else:
            print(s[y][x], end="")
    print()
