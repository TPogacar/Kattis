mn_sin = set()
for _ in range(int(input())):
    mn_sin.add(int(input()))

for mod in range(1, 10 ** 6 + 1):
    if len({sin % mod for sin in mn_sin}) == len(mn_sin):
        print(mod)
        break
