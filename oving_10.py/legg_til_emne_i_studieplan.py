
from legg_til_emne import*

from klasse import*

def legg_til_emne_i_studieplan(emnekode_liste, studieplan_liste, emne_dict):
    
    for (i, studieplan) in enumerate(studieplan_liste):
       print(i, ":", studieplan)
        
    tall = int(input("Hvilken studieplan vil du legge emne til i?"))
    
    hvilken_studieplan = studieplan_liste[tall]

    
    # student_id.ID = student_id // trur ikkje me trrenge dette
    

    
    # student_id.navn = studieplan_navn // eller dette
    
    
    x = 1
    for i in emnekode_liste:
        print(x,":", i)
        x = x + 1
    
    while True:
        try:
            hvilket_emne = int(input("Hvilket emne vil du legge inn i studieplanen din?: ")) - 1
            if hvilket_emne > len(emnekode_liste) :
                print("feil")
                continue
            break
        except ValueError:
            print("FEIL")
            
    emne = emne_dict.get(emnekode_liste[hvilket_emne])
    
    semester = int(input("Hvilket semester: "))

    hvilken_studieplan.legg_til_emne(emne, semester)
    
   # emne_navn = emne_dict.get(emne)
    
    
    #student_id.emne[semester] =  emne // eller denne, uiskker

    
