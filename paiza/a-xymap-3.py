y, x, now_direction = input().split()
y = int(y)
x = int(x)
d = input()
lr = 1

if d == "L":
    lr = -1

if now_direction == "N":
    x += lr
elif now_direction == "E":
    y += lr
elif now_direction == "S":
    x -= lr
elif now_direction == "W":
    y -= lr

print(y, x)
