height, width = [int(x) for x  in input().split()]
mymap = [list(input()) for i in range(height)]

now_height = 0
now_width = 0
goal_flg = False

def go_right():
    for width_itr in range(width):
        #ダメになったらreturn
        if(mymap[now_height][width_itr]) == "#":
            return
        if(width_itr==width-1):
            return
        now_width = width_itr

def go_up():
    for height_itr in range(height):
        #ダメになったらreturn
        if(mymap[now_width][height_itr]) == "#":
            return
        if(height_itr==height-1):
            return
        now_height = height_itr

def judge():
    if now_width == 0 and now_height == height-1:
        return True
    if now_width == width-1 and now_height == height-1:
        return True
    if now_width == 0 and now_height == height-1:
        return True


while not goal_flg:
    go_right()
    if()

