H, W, N = map(int, input().split())
S = [list(input()) for _ in range(H)]
for _ in range(N):
    y, x = map(int, input().split())
    S[y][x] = "#"
for y in range(H):
    print("".join(S[y]))  # 配列をまとめて表示する
