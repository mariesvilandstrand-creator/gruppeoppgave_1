#Lag et nytt emne: Et emne skal ha minimum en emnekode, om emnet undervises høst
#eller vår, og antall studiepoeng. Dere kan lagre dette i tre lister, en for emnekoder, en for
#semester (høst eller vår) og en for antall studiepoeng, og hvor samme indeks i de tre
#listene representerer samme emne




def legg_til_nytt_emne(emnekode_liste, semester_liste, studiepoeng_liste, aarstid_liste):
    emnekode=input("Hva er emnekoden?")
    
    while len(emnekode) > 6 and len(emnekode)<6:
        emnekode=input("Hva er emnekoden?")
    emnekode_liste.append(emnekode)
    semester=int(input("Hvilket semester er det?"))
    
    while semester>6 or semester<1:
        print("FEIL")
        semester=int(input("Hvilket semester er det?"))
    semester_liste.append(semester)
    
    
    if semester in [2,4,6]:
        aarstid_liste.append("vår")
    else:
        aarstid_liste.append("høst")
    studiepoeng=int(input("Hvor mange studiepoeng?"))
    
    
    while studiepoeng>30 or studiepoeng<5:
        print("Ugyldig poengsum, prøv igjen")
        studiepoeng=int(input("Hvor mange studiepoeng?"))
    studiepoeng_liste.append(studiepoeng)