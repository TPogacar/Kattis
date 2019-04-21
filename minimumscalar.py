st_skalarjev = int(input()) #koliko skalarnih produktov bomo izračunali


for st_vnosa in range(st_skalarjev):
    '''
        izračunamo najmanjšo vsoto produktov koordinad
        (po ena koordinata iz vsakega vektorja)
    '''
    dimenzija_vektorja = int(input()) #dolžina vektorja - koliko števil bo v vsaki tabeli

    #urejena vektorja: 1. od najmanjšega do največjega, 2. obratno
    vektor1 = sorted(map(int, input().split()))
    vektor2 = sorted(map(int, input().split()))[::-1]
    
    min_skalar = 0
    for indeks in range(dimenzija_vektorja):
        '''
            vsota produktov bo najmanjša, kadar bomo
            množili majvečje in najmanjše število ...
        '''
        min_skalar += vektor1[indeks] * vektor2[indeks]
    
    print('Case #{}: {}'.format(st_vnosa + 1, min_skalar))
