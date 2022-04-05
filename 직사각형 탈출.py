x, y, w, h = map(int, input().split())
a = [0, 0, 0, 0]
a[0] = x
a[1] = y
a[2] = w - x
a[3] = h - y
gg = a[0]
for i in range(4):
    if gg > a[i]:
        gg = a[i]

print(gg)
