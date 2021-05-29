# 全部replaceで消してく人もいた
s = input()

# s = "erasedream"
# s = "dreameraser"
#s = "dreamerer"

dividers = ["dream", "dreamer", "erase", "eraser"]

t_dividers = list(map(lambda x: x[::-1], dividers))
t_s = s[::-1]

answer = True

# すべての文字について、dividerを1つずつためす
i = 0
while i < len(t_s):
    can_devided = False
    for t_divider in t_dividers:
        # きってみる
        if (t_s[i:i+len(t_divider)] == t_divider):
            i += len(t_divider)
            can_devided = True
    # dividerのどれでもきれなかった
    if not can_devided:
        answer = False
        break

if answer:
    print("YES")
else:
    print("NO")
