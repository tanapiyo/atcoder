'''
かくけたで9つずつゾロ目の数はある
'''
import math
n = int(input())
keta = math.ceil(n/9)
num = n % 9  # けたの中でいくつめか
if num == 0:
    num = 9

answer = ""
for _ in range(0, keta):
    answer += str(num)

print(answer)
