Y, X, N = map(int, input().split())
for _ in range(N):
    direction = input()
    if direction == "N":
        Y -= 1
    if direction == "S":
        Y += 1
    if direction == "W":
        X -= 1
    if direction == "E":
        X += 1
    print(Y, X)
