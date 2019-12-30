import math
def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i ==0:
            return False
    return True
 
#target = int(input())
target = 100003
 
not_found_flg = True
if target == 2:
    print("2")
else:
    if target %2 == 0:
        target = target+1
    result = 0

    while not_found_flg:
        if (is_prime(target)):
            result = target
            break
        target = target+2
 
    print(result)