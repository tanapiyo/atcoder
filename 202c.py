n = int(input())
a_all = list(map(int, input().split()))
b_all = list(map(int, input().split()))
c_all = list(map(int, input().split()))
index_list = {}
a_list = {}
for c in c_all:
    if c >= n:
        continue
    if c in index_list:
        index_list[c] += 1
    else:
        index_list[c] = 1
for a in a_all:
    if a in a_list:
        a_list[a] += 1
    else:
        a_list[a] = 1
print(index_list)
print(a_list)

sum = 0
for i in index_list:
    print(b_all)
    if b_all[i] in a_all:
        sum += index_list[i]*a_list[b_all[i]]
print(sum)

# Dはbitでどの数かみようとおもった
