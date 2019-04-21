stevilo_celic = int(input()) #koliko besedilnih celic bomo imeli

for _ in range(stevilo_celic):
    '''za vsako besedilno celico izpiše, koliko različnih mest je obiskala'''
    stevilo_mest = int(input())
    mesta = []
    for _ in range(stevilo_mest):
        '''sestavi tabelo mesta, ki vsebuje smo različna imena mest s trenutnega potovanja'''
        mesto = input()
        if mesto not in mesta:
            '''če v tem mestu še ni bila, ga doda v tabelo mesta'''
            mesta.append(mesto)
    print(len(mesta))
        
