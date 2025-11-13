def skrive_ut_studieplan(studieplan_liste):
    
    for (i, studieplan) in enumerate(studieplan_liste):
        print(i, ":", studieplan.ID, ":", studieplan.navn)
            
        tall = int(input("\nHvilken studieplan vil du legge emne til i?"))
        
        hvilken_studieplan = studieplan_liste[tall]
        
        print(i, ":", studieplan)