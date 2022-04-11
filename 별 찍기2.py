i = int(input())
j = '*'
n = ' '
for a in range(i - 1, -1, -1):
    print(n * a, end='*')
    for b in range(1, i - a , 1):
        print(j, end='')
    print()

