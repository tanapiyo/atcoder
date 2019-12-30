#tree_num, monitor_distance = [int(x) for x  in input().split()]
import math
tree_num, monitor_distance = [20,4]
hitori = monitor_distance*2 + 1
kazu = (tree_num + monitor_distance*2) / hitori
print()
print(int(kazu))
# if tree_num % monitor_distance == 0:
#     print(kazu+1)
# else:
#     print(kazu)
