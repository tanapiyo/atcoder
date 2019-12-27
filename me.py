






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

