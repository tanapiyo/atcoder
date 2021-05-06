#深さ優先探索をする
#今いるところから隣にいくのを四方向試し尽くす
#基本みぎに進んで、進めなかったら戻ってくる感じ
#深いところから先に探索する（分岐を無視）
#stackで実装する方法もある
#枝かりもできる

if __name__ == "__main__":
    height, width = input().split()
    town = [list(input()) for _ in range(height)]#list(input())で一行をlistに突っ込むので
    #startを探す
    #startから.を辿って上下左右にいくdfs（再帰）
    #goalまで行けるか試す