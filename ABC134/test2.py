length = int(input())
suretsu=[int(input()) for i in range(length)]
result = []
for i in range(length):
    pop_suretsu = suretsu[0:i] + suretsu[i+1:]
    print(pop_suretsu)
    result.append(str(max(pop_suretsu)))
print('\n'.join(result))

#print('\n'.join(result.split()))
#\n'.join(s.splitlines())

length = int(input())
suretsu=[int(input()) for i in range(length)]
result = []
sorted_suretsu = sorted(suretsu,reverse=True)
zantei_max = sorted_suretsu[0]

for i in range(length):
    if (zantei_max == suretsu[i]):
        result.append(str(sorted_suretsu[1]))
    else:
        result.append(str(zantei_max))
print('\n'.join(result))



box_num = input()
amarilist = [int(x) for x  in input().split()]#ある倍数の箱のボールの和の偶奇を決める

def check(amarilist):
    for i in range(1,len(amarilist)):
        if amarilist[i] == 0:#iの倍数の箱に偶数個入れたい
            if(sum(amarilist[::i])%2 != 0):
                return False
        else:#iの倍数の箱に奇数個入れたい
            if (sum(amarilist[::i])%2 == 0):
                return False
    return True

    #sum(box_num[::i])
kekka = check(amarilist)


#ある倍数が書かれた箱がx個ある
#x個に入れられるのの偶奇が決まっている


box_num = input()
amarilist = [int(x) for x  in input().split()]#

#後ろから見ていく
#倍数に入っている数によって自分が0か1か決める
box_num[-1]