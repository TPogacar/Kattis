max_stevlilo, st_poskusov =  map(int, input().split())

if 2 ** st_poskusov >= max_stevlilo:
    #po metodi bisekcije je mogoče priti do pravilnega rezultata
    print('Your wish is granted!')
else:
    print('You will become a flying monkey!')
