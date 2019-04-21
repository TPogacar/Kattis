import sys

st_matrik = 1
st_vrstice = 1
for vrstica in sys.stdin:  # prebere posamezno vrstico v datoteki
    if st_vrstice == 3:
        # imamo prazno vrstico => v naslednji vrstici se začne
        # nova matrika, ali pa je konec dokumenta
        st_vrstice = 0
        st_matrik += 1
    elif st_vrstice == 1:  # prva vrstica matrike
        print('Case {}:'.format(st_matrik))
        a, b = map(int, vrstica.split())
    elif st_vrstice == 2:  # druga vrstica matrike
        c, d = map(int, vrstica.split())
        # vsako komponento inverza moramo celoštevilsko deliti z determinanto
        determinanta = a * d - b * c
        print('{} {}\n{} {}'.format(d // determinanta, -b // determinanta,
                                    -c // determinanta, a // determinanta))
    st_vrstice += 1
