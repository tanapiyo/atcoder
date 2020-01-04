# 5 2
# 8 7 6
# rsrpr

#k回前と同じ手は出せない

# gamenum, limit = [int(x) for x in input().split()]
# ten_rock, ten_scissors, ten_paper = [int(x) for x in input().split()]
# strategy_list = list(input())

gamenum, limit = [7,5]
ten_rock, ten_scissors, ten_paper = [100,10,1]
strategy_list = list("sssssssssss")

tokuten_dict = {"r": ten_paper, "s":ten_rock, "p": ten_scissors}
strategy_dict = {"r": "p", "s": "r", "p": "s"}

tokuten = 0
history = []
i=1
check_idx = 0
for strategy in strategy_list:
    if(i - limit -1<0)or i ==1:
        tokuten = tokuten+tokuten_dict[strategy]
        history.append(strategy_dict[strategy])
    else:
        check_idx = i - limit -1
        if history[check_idx] == strategy_dict[strategy]:
            history.append(strategy)
        else:
            tokuten = tokuten+tokuten_dict[strategy]
            history.append(strategy_dict[strategy])
    i=i+1
print(history)
print(tokuten)
