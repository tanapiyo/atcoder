H, W, = map(int, input().split())
S = [list(input()) for _ in range(H)]
for y in range(H):
    for x in range(W):
        if S[y][x] == "#":
            print(str(y) + " " + str(x))  # print(y, x)で平気だった
