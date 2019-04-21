for _ in range(int(input())):
    d = int(input())  # koliko mest ima število
    # izračunamo, koliko takšnih števil ne vsebuje števke 9
    st_ustreznih_stevil = 8 * pow(9, d - 1, 1000000007) % 1000000007
    print(st_ustreznih_stevil)
