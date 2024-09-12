n = 7

a = [[i - j for i in range(n)] for j in range(n)]

for r in a:
        print(*[f"{x:2}" for x in r])
