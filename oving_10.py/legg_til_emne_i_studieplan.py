
from legg_til_emne import*

from klasse import*

def legg_til_emne_i_studieplan(emnekode_liste, student_id_liste, studieplan_dict, emne_dict):
    
    student_id = input("Hva er student-id'en din?")
    
    # student_id.ID = student_id // trur ikkje me trrenge dette
    
    student_id_liste.append(student_id)
    
    studieplan_navn = input("Hvilket studie går du?")
    
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
            
    emne = emnekode_liste[hvilket_emne]
    
    emne_navn = emne_dict[emne]
    
    hvilket_semester = emne_navn.semester_til_emnet
    
    
    #student_id.emne[semester] =  emne // eller denne, uiskker

    
    for i in (6):
        if emne in emne.emne[i]: #prøve å finna ud om emne ligge i listå emne.emne
            print("Du har allerede dette emnet i studieplanen din!")
            return
        else:
            continue
    
    studiepoeng = emne.studiepoeng
    
    student_id.studiepoeng[hvilket_semester].append(studiepoeng)
    
    if sum(emne.studiepoeng[hvilket_semester]) > 60:
        print("Du har lagt til for mange emner")
        student_id.studiepoeng[hvilket_semester].remove(studiepoeng)
    if sum(emne.studiepoeng[hvilket_semester]) <= 60:
        print("\n emnet ditt er nå lagt til i studieplanen din")
    
    Full_studieplan = Studieplan(student_id, studieplan_navn, studiepoeng, emne)
        
    studieplan_dict[student_id] = Full_studieplan
    
    print(studieplan_dict[student_id])

