#kako so odgovarjali:
adrian = ['A', 'B', 'C'] * 34
bruno = ['B', 'A', 'B', 'C'] * 25
goran = ['C', 'C', 'A', 'A', 'B', 'B'] * 17

stevilo_vprasanj = int(input())
pravilni_odgovori = [crka for crka in input()] #tabela pravilnih odgovorov

#na koliko vprašanj so pravilno odgovorili:
a, b, g = 0, 0, 0
for indeks in range(stevilo_vprasanj):
    '''če je oseba pravilno odgovorila, povečamo število njegovih pravilnih odgovorov za 1'''
    if pravilni_odgovori[indeks] == adrian[indeks]:
        a += 1
    if pravilni_odgovori[indeks] == bruno[indeks]:
        b += 1
    if pravilni_odgovori[indeks] == goran[indeks]:
        g += 1
najvecje_stevilo_pravilno_odgovorjenih = max(a, b, g)
print(najvecje_stevilo_pravilno_odgovorjenih)

#izpišemo urejena imena tistih, ki so najbolje odgovarjali na vprašanja
if a == najvecje_stevilo_pravilno_odgovorjenih:
    print('Adrian')
if b == najvecje_stevilo_pravilno_odgovorjenih:
    print('Bruno')
if g == najvecje_stevilo_pravilno_odgovorjenih:
    print('Goran')
