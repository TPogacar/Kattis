stevilo_ugrizov = int(input()) #kolikokrat Arild ugrizne
besede = input().split() #kaj reče ob posameznem ugrizu

pavilno_steje = True
#za vsako izgovorjeno besedo preverimo njeno ustreznost
for indeks in range(len(besede)):
    '''za vsako besedo, ki jo izgovori, preverimo, ali je ustrezna'''
    if len(besede) != stevilo_ugrizov:
        #preverimo, ali Arold res vsakič šteje
        pavilno_steje = False
        print('something is fishy')
        break
    if (besede[indeks] != str(indeks + 1)) and (besede[indeks] != 'mumble'):
        #Arild se je zmotil - neustrezno štetje
        pavilno_steje = False
        print('something is fishy')
        break
if pavilno_steje == True:
    print('makes sense')
    
