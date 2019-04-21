tarifa = int(input())
stevilo_mesecev = int(input())

porabljeni_podatki = 0
for _ in range(stevilo_mesecev):
    '''za vsak mesec skupnemu številu porabljenih podatkov
    prištejemo, koliko podatkov je porabil tekoči mesec'''
    porabljeni_podatki += int(input())


# izpišemo, koliko podatkov bo imel na razpolago prihodnji mesec
print(tarifa * (stevilo_mesecev + 1) - porabljeni_podatki)
