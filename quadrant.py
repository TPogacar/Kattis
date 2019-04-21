abscisa = int(input())
ordinata = int(input())

if abscisa > 0 and ordinata > 0:
    print(1)
if abscisa < 0 and ordinata > 0:
    print(2)
if abscisa < 0 and ordinata < 0:
    print(3)
if abscisa > 0 and ordinata < 0:
    print(4)
