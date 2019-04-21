n = input().strip()  # števec
m = input().strip()  # imenovalec

dol_n = len(n)
dol_m = len(m) - 1  # štejemo samo število ničel

if dol_n > dol_m:
    # pri deljenju dobimo število večje od 0
    st_celih = dol_n - dol_m  # koliko števk je pred decimalno vejico
    kolicnik = n[: st_celih] + '.' + n[st_celih:]
else:
    # količnik je manjši od 0 - za dec. vejico dodamo ustrezno število ničel
    kolicnik = '0.' + '0' * (dol_m - dol_n) + n

zadnja = -1
while kolicnik[zadnja] == '0':
    # ugotovimo, na katerem mestu z desne količnika je prva neničelna števka
    zadnja -= 1

if zadnja == -1:
    print(kolicnik)
elif kolicnik[zadnja] == '.':
    # deljenje je celoštevilsko
    print(kolicnik[: zadnja])
else:
    # dobili smo decimalno število => izbišemo vse števke o vključno i-te z desne
    print(kolicnik[: zadnja + 1])
