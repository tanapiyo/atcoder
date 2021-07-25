n, x = map(int, input().split())  # 種類数n, 距離x
# n = 3
# x = 600
# inputs = [[600, 200, 200, 400], [900, 800, 400, 500], [200, 200, 200, 300]]
maxprice = 0
minprice = 10000000

for kind in range(n):
    price = 0
    dist = x
    # 初乗り距離、初乗り運賃、加算距離、加算運賃
    firstx, firstp, addx, addp = map(int, input().split())
    #firstx, firstp, addx, addp = inputs[kind]
    price += firstp
    dist -= firstx
    while(dist >= 0):
        price += addp
        dist -= addx
    if price > maxprice:
        maxprice = price
    if price < minprice:
        minprice = price
print(str(minprice) + " " + str(maxprice))
