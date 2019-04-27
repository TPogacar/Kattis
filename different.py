import sys

for vrstica in sys.stdin:  # preberemo vrstice
    # števili iz posamezne vrstice shranimo v spremenljivki
    st_1, st_2 = map(int, vrstica.split(' '))
    # izpišemo abs. vrednost razlike števil
    print(abs(st_1 - st_2))
