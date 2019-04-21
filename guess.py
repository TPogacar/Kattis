najmanjse = 1 #spodnja meja intervala števil, na katerem se nahaja iskano število
najvecje = 1001 #zgornja meja intervala

while -1 != 42:
    #ponavljamo, dokler ne najdemo števila (bisekcija)
    srednje = (najvecje + najmanjse) // 2 #ker želimo, da gre dolžina intervala števil proti nič, vzamemo za pol manjši interval
    print(srednje) #izpišemo naše število
    stevilo = input() #izvemo uspešnost ugibanja
    if stevilo == 'correct':
        #našli smo iskano število
        break
    if stevilo == 'lower':
        #iskano število je manjše od srednjega z našega intervala
        najvecje = srednje
    if stevilo == 'higher':
        #iskano število je večje od srednjega z našega intervala
        najmanjse = srednje
