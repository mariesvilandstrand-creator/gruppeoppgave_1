def liste_over_emne(emnekode_liste):
    x = 1
    print("\nRegistrerte emner:\n")
    for i in emnekode_liste:
        print(x,":", i)
        x = x + 1
    