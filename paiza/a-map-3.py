H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
result = []

for y in range(H):
    for x in range(W):
        if x == 0 or S[y][x-1] == "#":
            if x == W-1 or S[y][x+1] == "#":  # 0かw-1のときは判定スキップ
                print(y, x)
