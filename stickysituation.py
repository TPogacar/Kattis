stevilo_palck = int(input())
dolzine_palck = sorted(map(int, input().split())) #urejena številska tabela dolžin palčk

'''
    iz palčk lahko sestavimo trikotnik, kadar
    je vsota dveh stranic večja od tretje (najdaljše)
'''

lahko_naredimo_trikotnik = False
#preverimo ali obstajajo take 3 palčke
for indeks in range(stevilo_palck - 2):
    if dolzine_palck[indeks] + dolzine_palck[indeks + 1] > dolzine_palck[indeks + 2]: #trikotniško pravilo
        #našli smo usterzne palčke
        lahko_naredimo_trikotnik = True
        break
if lahko_naredimo_trikotnik:
    #lahko sestavimo trikotnik
    print('possible')
else:
    #ne moremo sestaviti trikotnika
    print('impossible')
