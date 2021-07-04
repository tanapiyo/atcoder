'''
まずは全探索をすることを考えてみる
全探索だと10^10になりそうなのでこのままだと解けない
読める式一を探す
  Aは1冊よんだとして、Bはどこまで読めますか
  Aは2冊よんだとして、Bはどこまで読めますか という探索をする
  Bがどこまでかを二分探索する
 '''

n, m, k = [int(x) for x in input().split()]  # nとm冊の本、合計k分まで
a = [int(x) for x in input().split()]  # よむのにかかる分数リスト
b = [int(x) for x in input().split()]  # よむのにかかる分数リスト
# n = 3
# m = 4
# k = 730
# a = [60, 90, 120]
# b = [80, 150, 80, 150]

# まず合計分数リストを作ってしまう
for i in range(n-1):
    a[i+1] += a[i]
for i in range(m-1):
    b[i+1] += b[i]
a.insert(0, 0)  # aから読まない場合
b.insert(0, 0)

maxnum = 0  # 何冊読めたか

for a_n in range(n+1):
    # aは全探索
    nokori = k - a[a_n]  # 残り
    if(nokori < 0):
        continue

    # 2分探索
    # 最初は0とはじっこにポインタをもってくる
    ok = 0
    ng = m+1
    while(abs(ok-ng) > 1):  # 1つに定まるまで半分にして探索する
        middle = abs(int((ok+ng)/2.0))
        if(b[middle] <= nokori):
            ok = middle
        else:
            ng = middle
    maxnum = max(maxnum, a_n+ok)

print(maxnum)
