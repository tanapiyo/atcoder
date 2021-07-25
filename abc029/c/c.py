n = int(input())


def brute_force(n, s):  # sに連結していく
    if n == 0:
        print(s)
        return 0
    else:
        for i in ["a", "b", "c"]:
            brute_force(n-1, s+i)


brute_force(n, "")
