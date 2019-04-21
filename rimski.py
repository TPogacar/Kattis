rimsko = input()

# če število vsebuje več kot eno črko ter se začne z LX==60,
# ter vsebuje le eno desetko X (XI=9 => če imamo LXXI je to ena desetka),
# lahko 60 zapišemo kot 40
if len(rimsko) > 1 and rimsko[: 2] == 'LX' and (
        not rimsko.startswith('LXX') or rimsko == 'LXXI'):
    rimsko = 'XL' + rimsko[2:]
# če beseda vsebuje zgolj eno črko, ali sta zadnji črki enaki II, je že zapisana optimalno.
# če je dol
if len(rimsko) == 1 or (len(rimsko) >= 2 and rimsko[-2:] == 'II'):
    print(rimsko)

elif rimsko[-1] == 'I' and rimsko[-2] != 'L':
    # predzadnja črka je bodisi V bodisi X => če zadnji
    # dve črki zamenjamo, dobimo manjše število
    print(rimsko[: -2] + 'I' + rimsko[-2])
else:
    # beseda že predstavlja najmanjše število
    print(rimsko)
















###v spremenljivke zapišemo število posameznih znakov
##c, l, x, v, i = 0, 0, 0, 0, 0
##for znak in rimsko:
##    if znak == 'C':
##        c += 1
##    elif znak == 'L':
##        l += 1
##    elif znak == 'X':
##        x += 1
##    elif znak == 'V':
##        v += 1
##    else:
##        i += 1
##
##izpisi = ''
##if c == 1: #imamo med 90 in 99
##    if x == 1 and l == 0:
##        izpisi += 'XC'
##        x = 0
##    else:
##        izpisi += 'C'
##    c = 0
##
##if l == 1: #imamo število med 40 in 99
##    if x == 1: #število med 40 in 49
##        izpisi += 'XL'
##        x = 0
##    else: #število med 50 in 99
##        izpisi = 'L'
##    l = 0
##
##if v == 1: #imamo enice med 4 in 8
##    #ne moremo imeti 9
##    izpisi += 'X' * x
##    x = 0
##    if i == 1: #imamo 4
##        izpisi += 'IV'
##    else: #imamo med 5 in 8
##        izpisi += 'V' + 'I' * i
##else: #lahko imamo ali 9 ali med 0 in 3
##    if x == 0: #imamo med 0 in 3
##        izpisi += 'I' * i
##    else:
##        if i == 1: #imamo 9, ostale X izpišemo pred 'enicami'
##            izpisi += 'X' * (x - 1) + 'IX'
##        else: #imamo 'enice' med 0 in 3, X zapišemo pred 'enice'
##            izpisi += 'X' * x + 'I' * i
##print(izpisi)    





