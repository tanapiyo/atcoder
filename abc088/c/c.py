'''
方針
全部グリッド上の数値を文字で表すと、列と列をひくと全部同じ値になるはずというのがわかる
行と列のすべての組み合わせに対してチェックすればOK
添字とかも紙に書くとよさそう

ちなみにこれはa1を固定して、b1=c11-a1として、残りの値をすべて出して、矛盾がないか確かめる方法もある
'''
c = []
for _ in range(3):
    row = list(map(int, input().split()))
    c.append(row)

flg = True
# 列について
# 0列目と1列目の差がすべて同じか
target = c[0][0] - c[0][1]
if c[1][0] - c[1][1] != target or c[2][0] - c[2][1] != target:
    flg = False
# 1列目と2列目
target = c[0][1] - c[0][2]
if c[1][1] - c[1][2] != target or c[2][1] - c[2][2] != target:
    flg = False

# 行について
target = c[0][0] - c[1][0]
if c[0][1] - c[1][1] != target or c[0][2] - c[1][2] != target:
    flg = False

target = c[1][0] - c[2][0]
if c[1][1] - c[2][1] != target or c[1][2] - c[2][2] != target:
    flg = False

if flg:
    print("Yes")
else:
    print("No")
