st_dobrin, x = map(int, input().split())
tab_cen = sorted(map(int, input().split()))  # urejena tabela cen

nismo_izpisali = True
for ind in range(st_dobrin - 1):
    # seštejemo dve zaporedni ceni
    vsota = tab_cen[ind] + tab_cen[ind + 1]
    if vsota > x:
        # vsota dveh do sedaj najvišjih zaporednih cen je presegla mejo x
        print(ind + 1)
        nismo_izpisali = False
        break

if nismo_izpisali:
    # v ponudbo lahko vključimo vse artikle
    print(st_dobrin)
