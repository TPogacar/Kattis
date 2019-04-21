# n = št. ovir, y = št. ovir, ki jih Mario najde
n, y = map(int, input().split(' '))

mn_najdenih_ovir = set()
for _ in range(y):
    mn_najdenih_ovir.add(int(input()))

for st_ovire in range(n):
    if st_ovire not in mn_najdenih_ovir:
        print(st_ovire)

print(f'Mario got {len(mn_najdenih_ovir)} of the dangerous obstacles.')
