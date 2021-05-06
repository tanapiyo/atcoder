'''
方針
飴全部獲得したらKになった場合の数を数える
飴が自分のマスにあったら２個でカウントすると、行列の飴の個数で計算できる
自分のマスにあったときはK+1個になれば足していないことになるし、K個だと余計にカウントしていることになるので調整

あるマスにいたら、行列が同じ飴を取得する

まず飴マップを紙にかく、デバッガで読めないところを読む
'''

# for test
R, C, K = 3, 5, 3
N = 5
ameInfo = [[1, 2], [2, 1], [2, 5], [3, 2], [3, 5]]

# 行列と飴の個数
# R, C, K = map(int, input().split())  # 空行くぎりのstringで渡ってくる
# N = int(input())  # 飴情報の個数
# ameInfo = [list(map(int, input().split()))
#            for i in range(N)]  # N行分空行くぎりのstringがくる

# 飴マップを作る
row = [0]*R
column = [0]*C

for x, y in ameInfo:  # 飴座標1つずつについて、飴マップに情報を入れる。マスはインデックス+1なので-1に入れる
    row[x-1] += 1
    column[y-1] += 1


answer = 0


# カウント
# ここだけわからない
rowx = [0] * (K+1)  # Kはターゲットの飴の数 [0,0,0,0]みたいなのができる
columnx = [0] * (K+1)

for rowi in row:
    if rowi <= K:
        rowx[rowi] += 1  # K個以下獲得する場合、飴の個数インデックスのところに＋１。0もある
for columni in column:
    if columni <= K:
        columnx[columni] += 1
for i in range(K+1):
    # K個飴を取得組合せ。i=1でK=3ならrowから1個、columnから2個とれる場合…をかけている
    answer += rowx[i] * columnx[K-i]

# 余剰分をのぞく
for x, y in ameInfo:
    if row[x-1]+column[y-1] == K:
        answer -= 1
    elif row[x-1]+column[y-1] == K+1:
        answer += 1


print(answer)
