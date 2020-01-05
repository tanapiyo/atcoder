#全探索でループ数気にする
def check_kingaku(maisu, kingaku):
    if(maisu*10000<kingaku):
        return "-1 -1 -1"
    for itr_1000 in range(maisu+1):
        for itr_5000 in range(maisu-itr_1000+1):
            itr_10000 = maisu - itr_1000 - itr_5000
            target = 1000*itr_1000 + 5000*itr_5000 + 10000*itr_10000
            if(target == kingaku):
                return str(itr_10000) + " " + str(itr_5000) + " " + str(itr_1000)
    return "-1 -1 -1"

maisu, kingaku = [int(x) for x in input().split()]
ret = check_kingaku(maisu, kingaku)
print(ret)
