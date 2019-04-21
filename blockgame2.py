def moznost_za_zmago(visina1, visina2):
    '''
        vrne True, če ima stolpih z višinama
        visina1 in visina 2 igralec na
        potezi zmaga, sicer False
    '''
    nizji = min(visina1, visina2)
    visji = max(visina1, visina2)
    if visji % nizji == 0:
        #če je višina višjega stolpa večkratnik višine nižjega, lahko višjega 'uničimo'
        return True
    if visji > 2 * nizji:
        #trenutni igralec lahko zmaga, saj lahko nasprotnika prisili v zgornji položaj tako,
        #da ga pusti ali z (visji % nizji, nizji), ali z (nizji, visji % nizji + nizji)
        #pri čemer oba položaja zagotavljata zmago igralcu na potezi
        return True
    #zadnja možnost: nizji <= visji < 2 * nizji, pri čemer je edina možna poteza
    #(visji - nizji, nizji). Zato nadaljujemo preverjanje možnosti za zmago pri teh višinah.
    #Upoštevamo, da je na potezi nasprotnik.
    return not moznost_za_zmago(visji - nizji, nizji)


visina1, visina2 = map(int, input().split())

if moznost_za_zmago(visina1, visina2):
    #igralec na potezi ima možnost za zmago
    print('win')
else:
    #nasprotnik lahko igralca na potezi prisili v poraz
    print('lose')
