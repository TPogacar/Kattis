st_stevil = int(input())

stevila = sorted(map(int, input().split())) #vnešena števila zapišemo v urejeno tabelo števil
stevila.append(12557859764542) #tabeli dodamo ogromno število, da je urejanje podatkov v nadaljevanju lažje

prejsnji = stevila[0]
dolzina = 1 #koliko zaporednih števil imamo (ki jih potem lahko združimo)

odgovor = [] #kaj bomo na koncu izpisali

for indeks in range(len(stevila)):
    trenutni = stevila[indeks] #trenutno število, ki ga gledamo
    if trenutni == prejsnji + 1:
        #je naslednih prejšnjega šteevila, zato ju bomo želeli združiti (število združenih števil se poveča)
        dolzina += 1
    else: #trenutno število ni naslednik => trenutno število ne bo združeno s prejšnjimi. Prejšnja dodabo k seznamu odgovor:
        if dolzina >= 3:
            #če so bila prejšnja zaporedna števila vsaj 3, jih zapišemo skupaj z '-'
            odgovor.append('{}-{}'.format(stevila[indeks - dolzina], stevila[indeks - 1]))
        elif dolzina == 2:
            #dneh zaporednih števil še ne zapišemo z '-'
            odgovor.append(stevila[indeks - 2])
            odgovor.append(stevila[indeks - 1])
        else:
            #če je bil en sam, ga dodamo
            odgovor.append(stevila[indeks - 1])
        dolzina = 1 #število zaporednih števil je pomovno enako 1
    prejsnji = trenutni


print(' '.join(map(str, odgovor[1:]))) #izpišemo vse, razen prvega, ki je naše ogromno število
