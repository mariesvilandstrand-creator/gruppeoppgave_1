

from legg_til_emne import*

from klasse import*


def fjerne_emne_fra_studieplan(emnekode_liste, studieplan_liste, emne_dict):
    
    for (i, studieplan) in enumerate(studieplan_liste):
       print(i, ":", studieplan)
        
    tall = int(input("Hvilken studieplan vil du fjerne emne i?"))
    
    hvilken_studieplan = studieplan_liste[tall]
    
    
    x = 1
    for i in emnekode_liste:
        print(x,":", i)
        x = x + 1
    
    while True:
        try:
            hvilket_emne = int(input("Hvilket emne vil du fjerne fra studieplanen din?: ")) - 1
            if hvilket_emne > len(emnekode_liste) :
                print("feil")
                continue
            break
        except ValueError:
            print("FEIL")
            
    emne = emne_dict.get(emnekode_liste[hvilket_emne])
    
    print(emne)
    
    semester = int(input("Hvilket semester: ")) - 1

    hvilken_studieplan.fjerne_emne(emne, semester)