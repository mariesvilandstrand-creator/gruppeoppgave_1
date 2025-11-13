from klasse import*

def gyldig_studieplan(studieplan_liste, emne_dict):
    
    for (i, studieplan) in enumerate(studieplan_liste):
       print(i, ":", studieplan)
        
    tall = int(input("Hvilken studieplan vil du sjekke"))
    
    hvilken_studieplan = studieplan_liste[tall]
    
    hvilken_studieplan.sjekk_studieplan_gyldig(emne_dict)