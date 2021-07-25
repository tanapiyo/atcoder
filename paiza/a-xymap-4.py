y, x, n = map(int, input().split())
count = 1  # 連続移動回数
directions = ["E", "S", "W", "N"]  # 常に右にいくので
now_direction = 0
isFirst = True  # 2回連続で移動すると回数が増える
while n > 0:
    if isFirst == False:
        count += 1
    if directions[now_direction] == "N":
        x = x-count
    if directions[now_direction] == "E":
        y = y-count
    if directions[now_direction] == "S":
        x = x+count
    if directions[now_direction] == "W":
        y = y+count
    isFirst = False
    now_direction = (1 + now_direction) % 4
    n -= count


print(y, x)

x, y, n = map(int, input().split())
directions = ["E", "S", "W", "N"]
now_direction = 0
count = 0
max_count = 1
first = True


def move(direction, x, y):
    if direction == "N":
        y -= 1
    elif direction == "E":
        x += 1
    elif direction == "S":
        y += 1
    elif direction == "W":
        x -= 1
    return (x, y)


for _ in range(n):
    (x, y) = move(directions[now_direction], x, y)
    count += 1
    if first and count == max_count:
        first = False
        count = 0
        now_direction = (1 + now_direction) % 4
    elif count == max_count:
        first = True
        count = 0
        max_count += 1
        now_direction = (1 + now_direction) % 4


print(x, y)
