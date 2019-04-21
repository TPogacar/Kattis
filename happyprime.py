##def je_prastevilo(n):
##    '''vrne, ali je število n praštevilo'''
##    if n <= 1: #vsa praštevila so večja od 1
##        return False
##    else:
##        for stevilo in range(2, n): #polj. praštevilo je deljivo le z 1 in samimseboj
##            if n % stevilo == 0:
##                return False
##        return True


##def je_veselo_stevilo(n):
##    '''
##        vrne, ali je število n veselo
##    '''
##    vesela_stevila = []
##    while n != 1:
##        n = sum(int(stevka) ** 2 for stevka in str(n)) #n je vsota kvadratov njenih števk
##        if n in vesela_stevila:
##            return False
##        vesela_stevila.append(n)
##    return True


##def je_veselo_prastevilo(n):
##    '''
##        vrne YES, če je število veselo praštevilo, sicer NO
##    '''
##    if not je_prastevilo(n): #veselo praštevilo mora biti praštevilo
##        return 'NO'
##    else: #če je število praštevilo, mora biti tudi veselo, da je veselo praštevilo
##        stevilo = str(n)
##        while 42 > 0:
##            vsota_kvadratov_stevk = 0
##            for stevka in stevilo:
##                '''seštejemo kvadrate števk števila stevilo'''
##                vsota_kvadratov_stevk += int(stevka) ** 2
##            stevilo = str(vsota_kvadratov_stevk)
##            if len(stevilo) == 1: #ali se je število zreduciralo do 1
##                if stevilo == '1':
##                    return 'YES'
##                else:
##                    return 'NO'


##vesela_prastevila_do_10001 = []
##for stevilo in range(1, 10001):
##    if je_veselo_stevilo(stevilo) and je_prastevilo(stevilo):
##        vesela_prastevila_do_10001.append(stevilo)
##print(vesela_prastevila_do_10001)


vesela_prastevila_do_10001 = [7, 13, 19, 23, 31, 79, 97, 103, 109, 139, 167, 193, 239, 263, 293, 313, 331, 367, 379, 383, 397, 409, 487, 563, 617, 653, 673, 683, 709, 739, 761, 863, 881, 907, 937, 1009, 1033, 1039, 1093, 1151, 1277, 1303, 1373, 1427, 1447, 1481, 1487, 1511, 1607, 1663, 1697, 1733, 1847, 1933, 2003, 2039, 2063, 2111, 2221, 2309, 2333, 2339, 2383, 2393, 2417, 2557, 2693, 2741, 2833, 2851, 2903, 2963, 3001, 3019, 3067, 3079, 3083, 3109, 3137, 3209, 3301, 3313, 3319, 3323, 3329, 3331, 3371, 3391, 3463, 3607, 3637, 3643, 3673, 3709, 3779, 3797, 3803, 3823, 3833, 3907, 3923, 3931, 4111, 4127, 4157, 4217, 4271, 4363, 4441, 4447, 4481, 4517, 4663, 4721, 4751, 4817, 4871, 5147, 5227, 5281, 5417, 5471, 5477, 5527, 5569, 5659, 5741, 5821, 5879, 5897, 5987, 6037, 6053, 6073, 6163, 6197, 6203, 6329, 6337, 6343, 6353, 6361, 6367, 6373, 6389, 6637, 6661, 6673, 6701, 6703, 6719, 6733, 6763, 6791, 6803, 6899, 6917, 6971, 6983, 7039, 7127, 7309, 7331, 7451, 7457, 7481, 7541, 7547, 7589, 7603, 7691, 7793, 7841, 7937, 8081, 8147, 8233, 8369, 8521, 8597, 8693, 8699, 8741, 8821, 8929, 8963, 8969, 9001, 9007, 9013, 9103, 9133, 9203, 9323, 9377, 9587, 9623, 9689, 9829, 9857]

def je_veselo_prastevilo(n):
    '''
        vrne YES, če je število veselo praštevilo, sicer NO
    '''
    if int(n) in vesela_prastevila_do_10001:
        return 'YES'
    return 'NO'
                          
stevilo_kandidatov = int(input())

for zaporedna_vrstica in range(1, stevilo_kandidatov + 1):
    '''za vsakega kandidata preverimo, ali je veselo praštevilo'''
    vrstica = input()
    kandidat = vrstica.split(' ')[-1] #kandidat je 2. (oz. zadnje) število
    print(zaporedna_vrstica, kandidat, je_veselo_prastevilo(int(kandidat)))

















            
