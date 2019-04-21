def fakulteta(n):
    '''
        vrne n!
    '''
    if n == 1:
        return 1
    else:
        # fakulteta je produkt vseh naravnih števil <= n
        return n * fakulteta(n - 1)


for _ in range(int(input())):
    # za vsako vnešeno število izpiše zadnjo števko njene fakultete
    print(fakulteta(int(input())) % 10)
