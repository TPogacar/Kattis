st_poskusov = int(input())

tab_vrjetnosti = []
for _ in range(st_poskusov):
    # zanimajo nas samo vrjetnosti pravilnosti posameznega gesla
    tab_vrjetnosti.append(float(input().split()[-1]))

# tabelo vrjetnosti uredimo od največje do najmanjše
tab_vrjetnosti = sorted(tab_vrjetnosti)[::-1]

odgovor = 0
for ind in range(st_poskusov):
    # odgovoru prištejemo posamezno vrjetnost pomnoženo z njeno 'prioriteto'
    odgovor += (ind + 1) * tab_vrjetnosti[ind]
print(odgovor)
