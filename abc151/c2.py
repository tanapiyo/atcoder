toisuu, subsuu = [int(x) for x  in input().split()]
ac_list = []
wa_list = []

def check_inside(toi, res):
    if res == "AC":
        if toi in ac_list:
            return 
        else:
            ac_list.append(toi)
            return
    elif res == "WA":
        if toi in ac_list:
            return
        if toi not in ac_list:
            wa_list.append(toi)
            return

if(subsuu == 0):
    print("0 0")
else:
    for i in range(subsuu):
        toi, res = input().split()
        check_inside(toi, res)

    all_ac = len(ac_list)
    all_wa = 0
    for key in ac_list:
        all_wa += wa_list.count(key)

    print(str(all_ac) + " " + str(all_wa))