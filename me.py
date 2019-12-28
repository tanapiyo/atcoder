num500 = int(input())
num100 = int(input())
num50 = int(input())
amount = int(input())
rst = 0
for itr500 in range(num500+1):
    for itr100 in range(num100+1):
        for itr50 in range(num50+1):
            kingaku = itr50*50+itr100*100+itr500*500
            print("itersは50¥", itr50, "100¥", itr100, "500¥", itr500)
            print(kingaku)
            if(kingaku==amount):
                rst += 1
print(rst)




num = input()

nums = [int(x) for x  in input().split()]



if __name__ == "__main__":
    
    evens = [6,4,10,4]
    itr = 0
    flg = True
    while flg:
        evens = list(map(lambda x: (x/2), evens))
        is_evens = list(map(lambda x: x.is_integer(), evens))
        if not all(is_evens):
            flg = False
            break
        itr+=1
        print(evens)
    print(itr)



def check_sum(num):
    sum = 0
    while num>0:
        sum += num%10
        num //= 10
    return sum

limit, bottom, top = [int(x) for x  in input().split()]
total = 0
for i in range(1,limit+1):
    print("number is",i)
    sum = check_sum(i)
    print("sum",sum)
    if ((sum >= bottom) and (sum <= top)):
        print("OKだった")
        total += i
print(total)

nums = [int(x) for x  in input().split()]
nums = sorted(nums, reverse=True)#大きい順に並べる
alice = sum(nums[::2])#偶数を取る
bob = sum(nums[1::2])#基数を取る

n=int(input())
nums=[input() for i in range(n)]
print(len(set(nums)))




maisu, kingaku = [int(x) for x in input().split()]
result = [-1,-1,-1]
for itr_10000 in range(maisu+1):
    for itr_5000 in range(maisu+1-itr_10000):
        itr_1000 = maisu - itr_5000 - itr_10000
        total = itr_10000*10000 + itr_5000*5000 + itr_1000*1000
        if total == kingaku:
            result = [itr_10000, itr_5000, itr_1000]
result = map(str, result)
print(' '.join(result))