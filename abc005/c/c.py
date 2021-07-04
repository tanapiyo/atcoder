# input
t = int(input())  # 賞味期限
n = int(input())  # 総数
a = [int(x) for x in input().split()]  # たこ焼きスケジュール
m = int(input())  # 来店人数
b = [int(x) for x in input().split()]  # 来店スケジュール

# 秒数をどうするか
# 100sでmaxのたこやき100なので、毎秒腐ってるたこ焼きをみてもいい（頭のがくさってるかどうか）

# queueを作る
left = 0
right = 0
array = [0 for x in range(100+1)]  # つくったたこ焼き

a_pointer = 0  # 次につくるやつ

for i in range(m):  # お客さんがくるごとに焼けたたこ焼きを入れるし、きたら取り出す
    # まずはたこ焼きを入れる作業
    while(a_pointer < n and a[a_pointer] <= b[i]):  # 作りきっていなくて、次に作る秒数が来店以下なら
        array[right] = a[a_pointer]
        right += 1
        a_pointer += 1
    # たこやきを出す
    while True:
        # だせない
        if(left >= right):
            print("no")
            exit()
        # だせるならだす
        tako = array[left]
        left += 1
        # 出したたこ焼きが腐っていないか
        if(tako+t >= b[i]):
            break  # もう一回次のたこやきでチャレンジ
print("yes")
