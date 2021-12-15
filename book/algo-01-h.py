'''
https://atcoder.jp/contests/past201912-open/tasks/past201912_h
- 全種類販売はセット販売の組み合わせ（偶数、奇数）
- 全部一律a減らすはO(N)かかるし、クエリ数QにたいしてO(NQ)になる
- minに対する操作だけしたい（O(1)）のと、全種類やセット販売は枚数だけ覚えておいて毎回引くのはやめたい
- ほしいのは偶数min, 奇数min, かったoffset
'''
N = int(input())  # 種類
C = list(map(int, input().split()))  # 在庫数
Q = input(input())  # クエリ数

# 合計販売枚数を最後は出力する
sell = 0

# 全種類で販売した枚数
z = 0
# セット販売した枚数
s = 0

# 奇数せっと販売のCの最小
min_s_C = 10000000
# 偶数のCの最小
min_z_C = 10000000

# minを計算しておく
for i in range(0, N):
    if i % 2 == 0:
        min_s_C = min(C[i], min_s_C)
    else:
        min_z_C = min(C[i], min_z_C)

# クエリ処理
for _ in range(0, Q):
    query = list(map(int, input().split()))  # 1 x a, 2 a, 3 a
    if query[0] == 1:  # 単体販売
        x = query[1] - 1  # index
        a = query[2]
        # カードxを減らす（これはO(1)なので別にいい）
        if x % 2 == 0:
            card_x = C[x] - z - s
        else:
            card_x = C[x] - z
        # a枚以上残っているなら売る、なければ売らない
        if card_x >= a:
            C[x] -= a
            sell += a
            if x % 2 == 0:
                min_s_C = min(C[x], min_s_C)
            else:
                min_z_C = min(C[x], min_z_C)
    elif query[0] == 2:  # セット販売
        a = query[1]
        if min_s_C - s - z >= a:
            s += a
    elif query[0] == 3:  # 全部販売
        a = query[1]
        if min(min_s_C-s-z, min_z_C-z) >= a:
            z += a

# セット販売の合計
for i in range(0, N):
    if i % 2 == 0:
        sell += s

sell += z*N

print(sell)
