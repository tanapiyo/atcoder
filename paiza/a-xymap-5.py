x, y, n = map(int, input().split())
directions = ["N", "E", "S", "W"]
now_direction = 0
for _ in range(n):
    walk = input()
    if walk == "L":
        now_direction = (3+now_direction) % 4  # この書きかた（何回まわるか）
    else:
        now_direction = (1+now_direction) % 4
    if directions[now_direction] == "N":
        y -= 1
    elif directions[now_direction] == "E":
        x += 1
    elif directions[now_direction] == "S":
        y += 1
    elif directions[now_direction] == "W":
        x -= 1

    print(x, y)
