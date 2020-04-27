import math
kamoku, max, avg = [int(x) for x  in input().split()]
tensus = [int(x) for x  in input().split()]

subtensu = avg*kamoku - sum(tensus)
kiriagetensu = math.ceil(subtensu)
if (kiriagetensu>max):
    print("-1")
elif(kiriagetensu<0):
    print("0")
else:
    print(kiriagetensu)

