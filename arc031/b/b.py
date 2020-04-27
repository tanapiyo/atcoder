
#'o'が陸地、'x'が海
# (y, x)から到達できるすべての陸地マスのcheckedをtrueにする
def fill_island(board, checked, y, x):
    if y < 0 or y >= 10 or x < 0 or x >= 10:#外側ならreturn
        return checked
    if board[y][x] == 'x':#海ならreturn
        return checked
    if checked[y][x]:#既に調べられているマスならreturn
        return checked
    checked[y][x] = True#y,xを既に調べているという状態に加えておく
    #再起的に上下左右で到達できるマスを埋める
    checked = fill_island(board, checked, y-1,x)
    checked = fill_island(board, checked, y,x+1)
    checked = fill_island(board, checked, y+1,x)
    checked = fill_island(board, checked, y,x-1)
    return checked


def check_connected(board):
    #print(board)
    checked = [[False for j in range(10)] for i in range(10)]#falseが10*1で並ぶ二次元配列
    #print(checked)
    y=0
    x=0
    break_flg = False
    #陸地マスを1つ探す
    for i in range(10):
        for j in range(10):
            if board[i][j] == 'o':
                y=i
                x=j
                break_flg = True
                break
            else:
                continue
        if break_flg:
            break

    checked = fill_island(board, checked,y,x)#見つけた陸地マスから到達できるマスを調べる
    for i in range(10):
        for j in range(10):
            if(board[i][j] == 'o'):#もし陸地なのにチェックされていないのが合ったらfalse
                if not checked[i][j]:
                    return False
    return True


if __name__ == "__main__":
    #1
    #board = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'x', 'x'], ['x', 'x', 'o', 'o', 'o', 'o', 'o', 'x', 'x', 'x'], ['x', 'x', 'x', 'o', 'o', 'o', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'o', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'o', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'o', 'o', 'o', 'x', 'x', 'x', 'x'], ['x', 'x', 'o', 'o', 'o', 'o', 'o', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
    #board = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'x', 'x'], ['x', 'x', 'o', 'o', 'o', 'o', 'o', 'x', 'x', 'x'], ['x', 'x', 'x', 'o', 'o', 'o', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'o', 'o', 'o', 'x', 'x', 'x', 'x'], ['x', 'x', 'o', 'o', 'o', 'o', 'o', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
    #board = [['x', 'x', 'x', 'x', 'o', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'o', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'o', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'o', 'x', 'x', 'x', 'x', 'x'], ['o', 'o', 'o', 'o', 'x', 'o', 'o', 'o', 'o', 'o'], ['x', 'x', 'x', 'x', 'o', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'o', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'o', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'o', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'o', 'x', 'x', 'x', 'x', 'x']]
    board = [list(input()) for _ in range(10)]#入力をboardに突っ込む
    #print(board)
    flag = False
    #1つ埋め立てて見てどうなるか
    for i in range(10):
        for j in range(10):
            if (board[i][j] == 'o'):
                continue
            board[i][j] = 'o'#埋め立てた
            if (check_connected(board)):
                flag = True
                break
            board[i][j] = 'x'#埋め立てを戻す
        else:
            continue
        break
    #出力
    if flag:
        print("YES")
    else:
        print("NO")
