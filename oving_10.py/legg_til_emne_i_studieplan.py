
from legg_til_emne import*

from klasse import*

def legg_til_emne_i_studieplan(emnekode_liste, student_id_liste, studieplan_dict, emne_dict, studieplan_liste):
    

    
    #if student_id not in studieplan_dict:
        #studieplan_dict[student_id] = [],[],[],[],[],[]
    
    
    # student_id.ID = student_id // trur ikkje me trrenge dette

    
    # student_id.navn = studieplan_navn // eller dette
    
    
    for studieplan in enumerate(i, studieplan_liste):
        print(f"{i}: {studieplan.navn}")
        
    tall = input("Hvilken studieplan vil du legge emne inn i?") - 1
    
    hvilken_studieplan = studieplan_liste[tall]
    
    
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
    
    hvilken_studieplan.append(emne)
    
    print(Studieplan)
    
    

