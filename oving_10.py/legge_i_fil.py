

def lagre_emne_studieplan_fil(studieplan_liste):
    
    for (i, studieplan) in enumerate(studieplan_liste):
       print(i, ":", studieplan.ID, ":", studieplan.navn)
        
    tall = int(input("\nHvilken studieplan vil du legge i en fil?"))
    
    hvilken_studieplan = studieplan_liste[tall]
  
    with open ("studieplan_fil.txt", "a", newline="", encoding="UTF-8") as fila:
        i = 1
        fila.write("ID:" + str(hvilken_studieplan.ID) + "\nstudie:" + hvilken_studieplan.navn)
        for semester in hvilken_studieplan.emner:
            fila.write(f"\nSemester {i}:\n")
            for emne in semester:
                fila.write(emne.emnekode+"\n")
            i = i + 1
                
