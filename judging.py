n = int(input())  # število oddaj

domjudge = {}  # slovar za rezultate oddaj ocenjene z DOMjudge
kattis = {}  # slovar za rezultate oddaj ocenjene s Kattisom

for _ in range(n):
    '''
        prvih n oddaj (ocenjene z DOMjudge) zapišemo v slovar domjudge
    '''
    rezultat = input()
    if rezultat in domjudge:
        # če ta rezultat že obstaja, se število teh poveča za 1
        domjudge[rezultat] += 1
    else:
        # ta rezultat še ne obstaja (pojavil se je prvič), zato ustvarimo
        # ključ z imenom tega rezultata in vrednostjo 1
        domjudge[rezultat] = 1

for _ in range(n):
    '''
        naslednjih n oddaj (ocenjene s Kattis) zapišemo v slovar domjudge
    '''
    rezultat = input()
    if rezultat in kattis:
        # ta rezultat že obstaja
        kattis[rezultat] += 1
    else:
        # ta rezultat se je pojavil prvič
        kattis[rezultat] = 1

# največje število potenicialno enakih rezultatov je enako vsoti najmanj
# ponovitev iz Katissa in DOMjudge za posamezni rezultat
st_enakih = 0
for rezultat in domjudge:
    if rezultat not in kattis:
        '''z ocenjevanjem v kattisu nismo nikoli dobili takega rezultata'''
        continue
    else:
        # prištejemo max št. potencialno enakih rešitev za posamezni rezultat
        st_enakih += min(kattis[rezultat], domjudge[rezultat])

print(st_enakih)
