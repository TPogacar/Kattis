st_period = int(input())

qaly = 0
for _ in range(st_period):
    perioda, kvaliteta = map(float, input().split())
    qaly += perioda * kvaliteta

print(round(qaly, 4))
