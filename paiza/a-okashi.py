def get_sum(n, is_buy_morethan_twice, limit):
    min_otsuri_all = 10000000
    # いくつお菓子を買うかでループをまわす（bit全探索）
    for i in range(2**n):
        kounyuu_sum = 0
        min_otsuri_mine = 1000000
        # ビットごとが種類なので、自分のビットが立っていたら購入したことにする
        for j in range(n):
            if((i >> j) & 1):  # 順番に右にシフトさせて最下位のbitチェックをする
                kounyuu_sum += okashi_price[j]
        if i == 2**n and is_buy_morethan_twice:
            is_buy_morethan_twice_mine = sum(okashi_price) < x - kounyuu_sum
            kounyuu_sum += get_sum(n, is_buy_morethan_twice_mine,
                                   limit-kounyuu_sum)
        if limit > kounyuu_sum:
            min_otsuri_mine = limit-kounyuu_sum
            if min_otsuri_all > min_otsuri_mine:
                min_otsuri_all = min_otsuri_mine

    return min_otsuri_all


n = 4
x = 1000
# n, x = map(int, input().split())  # お菓子種類、金額制限
okashi_price = []
# for kind in range(n):
#     okashi_price.append(int(input()))
okashi_price = [200, 20, 500, 60]

is_buy_morethan_twice = sum(okashi_price) < x

res = get_sum(n, is_buy_morethan_twice, x)
print(res)
