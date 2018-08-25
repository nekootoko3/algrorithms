def move(n, orig, to, tmp, cnt):
    if n == 0:
        return
    # n-1段をorigからtmpに移動する
    move(n-1, orig, tmp, to, cnt)
    # n段目をtoに移動する
    to.append(orig.pop())
    cnt[0] += 1
    # n-1段をtmpからtoに移動する
    move(n-1, tmp, to, orig, cnt)


import sys

# 引数でハノイの塔の高さを指定する
if len(sys.argv) != 2:
    print("error: no argument. need 1 int argument.")
    exit
N = int(sys.argv[1])

# N段の塔、空の塔を配列で擬似的に示す
orig = [i for i in range(N, 0, -1)]
tmp = []
to = []

# origの塔をtoに動かす
# cntは段を動かした回数
cnt = [0]
print("orig:", orig)
move(N, orig, to, tmp, cnt)
print("to:", to)
print("{}段のハノイの塔は{}回の移動が必要".format(N, cnt[0]))
