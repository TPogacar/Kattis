igre = input()


##rank = 25
##st_zvezd = 0
##zaporedne_zmage = 0
##
##for igra in igre:
##    if igra == 'W': #to igro je zmagal
##        st_zvezd += 1 #ker je zmagal dobi zvezdico
##        zaporedne_zmage += 1 
##        if rank >= 6: #če 3x zaporedno zmaga na nivojih 6-25, dobi dodatno zvezdico
##            if zaporedne_zmage >= 3:
##                st_zvezd += 1
##        if rank in {25, 24, 23, 22, 21}:
##            if st_zvezd >= 3: #število zvezd na tem nivoju je 2
##                rank -= 1
##                st_zvezd -= 2
##        if rank in {20, 19, 18, 17, 16}:
##            if st_zvezd >= 4: #število zvezd na tem nivoju je 3
##                rank -= 1
##                st_zvezd -= 3
##        if rank in {15, 14, 13, 12, 11}:
##            if st_zvezd >= 5: #število zvezd na tem nivoju je 4
##                rank -= 1
##                st_zvezd -= 4
##        if rank in {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}:
##            if st_zvezd >= 6: #število zvezd na tem nivoju je 5
##                if rank == 1: #najboljša stopnja je Legend, kjer ne morš izgubiti ranka
##                    rank = 'Legend'
##                    break
##                else:
##                    rank -= 1
##                    st_zvezd -= 5
##         
##        
##    else:
##        zaporedne_zmage = 0
##        if rank <= 20: #izguba nima vpliva na rank > 20
##            st_zvezd -= 1
##            if st_zvezd < 0:
##                if rank == 20:
##                    st_zvezd = 0
##                else:
##                    rank += 1
##                    if rank in {2, 3, 4,  5, 6, 7, 8, 9}:
##                        st_zvezd = 4 #max. število na teh nivojih je 5
##                    if rank in {10, 11, 12, 13, 14}:
##                        st_zvezd = 3 #max. število na teh nivojih je 4
##                    if rank in {15, 16, 17, 18, 19, 20}:
##                        st_zvezd = 2 #max. število na teh nivojih je 3
##print(rank)


def zvezde_za_rank(rank):
    '''
        vrne, koliko zvezd je pri danem ranku
    '''
    if rank >= 21:
        return 2
    if rank >= 16:
        return 3
    if rank >= 11:
        return 4
    return 5


rank = 25
zvezdice = 0
st_zaporednih_zmag = 0


for igra in igre:
    if rank == 0: #najboljša stopnja je Legend, kjer ne morš izgubiti ranka
        break
    if igra == 'W': #to igro je zmagal
        st_zaporednih_zmag += 1
        zvezdice += 1
        if st_zaporednih_zmag >= 3 and rank >= 6: #če vsaj 3x zaporedno zmaga na nivojih 6-25, dobi dodatno zvezdico
            zvezdice += 1
        if zvezdice > zvezde_za_rank(rank): #napreduje v naslednji rank
            zvezdice -= zvezde_za_rank(rank)
            rank -= 1
    else: #to igro je zgubil
        st_zaporednih_zmag = 0
        if rank <= 20: #izguba nima vpliva na rank > 20
            if zvezdice > 0:
                zvezdice -= 1
            else:
                if rank < 20: 
                    rank += 1
                    zvezdice = zvezde_za_rank(rank) - 1

if rank == 0: #rank 0 imenujemo 'Legend'
        rank = 'Legend'
print(rank)













    
