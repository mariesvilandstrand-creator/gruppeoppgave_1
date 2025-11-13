from klasse import*

def sjekk_emne_i_studieplan(emnekode_liste, emne_dict, studieplan_liste):
    
    x = 1
    print("\nRegistrerte emner:\n")
    for i in emnekode_liste:
        print(x,":", i)
        x = x + 1
    
    hvilket_emne = int(input("Hvilket emne vil du sjekke?")) - 1
    
    emne = emne_dict.get(emnekode_liste[hvilket_emne])
    
    for studieplan in studieplan_liste:
        if studieplan.sjekk_om_emne_i_studieplan(emne):
            print(f"Denne studieplanen: {studieplan.navn} har emnet: {emne.emnekode}")
        
    