# 2つの座標の距離はマンハッタン距離で、x-xiとy-yiを足したやつ（絶対値で）
# 時刻tiからti+1までに使える時間の中でたどり着けるか

n = int(input())
answer = ""
plans = []
for i in range(n):
    plans.append(list(map(int, input().split())))

# n = 1
# plans = [[2, 100, 100]]

# n = 2
# plans = [[5, 1, 1], [100, 1, 1]]


# 初期位置
px = 0
py = 0
pt = 0

# # 時間nまでの旅行について考える
for i in range(n):
    distance = abs(px - plans[i][1]) + abs(py - plans[i][2])  # 何ターンでたどり着くかの距離
    dt = plans[i][0] - pt  # 残された時間
    if dt < distance:
        answer = "No"
        break
    # distanceとdtの偶奇があっていればたどり着く
    if(dt - distance) % 2 == 1:  # ここ思いつかなかった
        answer = "No"
        break
    pt = plans[i][0]
    px = plans[i][1]
    py = plans[i][2]
if answer != "No":
    answer = "Yes"
print(answer)
