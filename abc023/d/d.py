'''
方針
各風船を割るべき制限時間を考えて、時間が短い順にわる
理論上可能かを調べるには上の時間短い順にわってみる（貪欲法）でやってみる
これを愚直にやると計算時間が足りないので、二分探索で境界値を探る
二分探索（判定関数つき）と貪欲法を使う問題

あるスコアPでクリアできるかどうかで二分探索。この時に風船を何秒以内に割らなければいけないかを求める。
これをソートしてi番目の値がiを超えていなければ大丈夫

「できる/できないの境界がある場合のスコアの最大/最小値」を求める場合、できるかできないかで二分探索をする。
スコアk+1は可能だが、スコアkは無理、という値kを見つければ良い。
https://qiita.com/drken/items/97e37dd6143e33a64c8c
'''
# 得点Xが可能かどうか
# 初期高度H、上昇速度Sの風船をX以下でわるには(X-H)/S秒以内に割らなければいけない
# だいたい二分探索をしつつ、探索の中で判定関数を呼んで判断していく感じ
# https://scrapbox.io/longshoujin/ABC023_D_-_%E5%B0%84%E6%92%83%E7%8E%8B
# https://note.com/omotiti/n/nba831daf2b61
INF = 2*10**14  # 得点MAX超える適当な大きい数

# 得点Xが可能かどうか

# 1秒で一個しか処理できないので、それがt+1を越えるとき、false
# t秒以内に処理すべき累積を数え上げる


def check(X):
    # sec = []  # 与えられる風船全部に対し割らなければいけない速度の一覧
    # # スコアX以下にする割るまでの時間の制限secを計算
    # for i in range(N):
    #     H, S = HS[i]  # とりあえず高度と速度に分解した
    #     sec.append((X-H // S))
    # sec.sort()
    # for i in range(N):
    #     if sec[i] < i:
    #         return False
    # return True
    data = [0] * N
    for i in range(N):
        H, S = HS[i]
        j = (X-H)//S
        if j < 0:
            return False
        data[min(j, N-1)] += 1  # jは制限、N-1は風船の数の一番大きいところ。基本一番制限きついやつが入る
    if data[0] >= 2:  # 2つ同時に割らなければいけないとするとだめ
        return False
    for i in range(1, N):
        data[i] += data[i-1]  # i時点ではi以下を全部わっていないとだめ
        # cum[i+1] = cnt[i+1]+cum[i];としてif(cum[t]>t+1){だとfalseでもいい
        if data[i] >= i+2:  # 割り切れない
            return False
    return True


# 入力を受け取る
N = int(input())
HS = [tuple(map(int, input().split())) for _ in range(N)]  # 初期高度と速度のタプルを作る

# 二分探索する
l, u = 0, INF
ans = INF
while l < u:
    m = (l+u) // 2  # 2分割する 下限lと上限uのどっちかを狭めて得点可能領域をcheckしていく
    if(check(m)):
        u = m
    else:
        l = m+1
ans = l  # 探索した結果の下限が答え

print(ans)
