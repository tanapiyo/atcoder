#全探索の例
num = int(input())
zahyo_list = []
max_dist = 0

import math

def calc_dist(alist, blist):
    return math.sqrt((alist[0]-blist[0])**2 + (alist[1]-blist[1])**2)

#初期化
for i in range(num):
    zahyo_list.append([float(x) for x  in input().split()])

for j in range(num):
    for k in range(j,num):
        dist = calc_dist(zahyo_list[j], zahyo_list[k])
        if(dist>max_dist):
            max_dist = dist
print(max_dist)


