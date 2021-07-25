H, W, N = map(int, input().split())  # 行数、列数、表示する座標の数
# inputmap = [] # 最初に配列の大きさを確保するようにした方がいい
S = [list(input()) for _ in range(H)]
# for height in range(H):
#     inputmap.append(list(input()))
for _ in range(N):  # 使わないindexは_でよい
    # x, y = map(int, input().split())
    y, x = map(int, input().split())
    print(S[y][x])
