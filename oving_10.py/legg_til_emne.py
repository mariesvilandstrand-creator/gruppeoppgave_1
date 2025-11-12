
from klasse import*

def legg_til_nytt_emne(emnekode_liste, emne_dict):
    
    emnekode = input("\nHva er emnekoden?")
    
    while len(emnekode) > 6 and len(emnekode)<6:
        emnekode=input("Hva er emnekoden?")
    
    emnekode_liste.append(emnekode)
    
    emne_navn = input("\nHva vil du kalle emne ditt for?")
    
    
    semester=int(input("\nHvilket semester er det?"))
    
    while semester>6 or semester<1:
        print("FEIL")
        semester=int(input("\nHvilket semester er det?"))
    
    
    studiepoeng=int(input("\nHvor mange studiepoeng?"))
    
    while studiepoeng>30 or studiepoeng<5:
        print("Ugyldig poengsum, prøv igjen")
        studiepoeng=int(input("Hvor mange studiepoeng?"))
    
    
    Fullt_emne = Emne(emne_navn, emnekode, semester, studiepoeng) #koss vett eg ke me ska bruga som self??
    
    emne_dict[emne_navn] = Fullt_emne
    
    
    # trudde eg trengte dette for å putta dei inn som objekt
    #emnekode.emne_navn = emne_navn
    #emnekode.emnekode = emnekode
    #emnekode.semester = semester
    #emnekode.studiepoeng = studiepoeng
    
    print(emne_dict[emne_navn])