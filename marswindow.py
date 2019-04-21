def leta_ko_gremo_na_mars(leto_x):
    '''
        vrne 'yes', če je leto_x leto, ko se nam splača iti na mars
        (2018 <= leto <= 10000), sicer 'no'
    '''
    if leto_x == 2018:
        #za to leto vemo, da je mars blizu
        return 'yes'
    marsovci_so_zih_bliz = 3 + 2018 * 12 #pretvorimo april 2018 v mesece (gledamo cele mesece, zato april=3)
    mars_je_blizu_vsakih = 26
    
    leto = 2018
    while leto <= 10000:
        marsovci_so_zih_bliz += mars_je_blizu_vsakih #naslednji mesec, ko bo mars blizu
        leto = marsovci_so_zih_bliz // 12 #mesece pretvorimo v cela leta
        if leto == leto_x:
            #našli smo leto, ko je mars blizu
            return 'yes'
        if leto > leto_x:
            #to leto bo mars predaleč
            return 'no'        
    return 'no'

print(leta_ko_gremo_na_mars(int(input())))




































