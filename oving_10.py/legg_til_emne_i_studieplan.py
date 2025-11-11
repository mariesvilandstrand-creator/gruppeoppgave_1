
from legg_til_emne import*

from klasse import*

def legg_til_emne_i_studieplan(emnekode_liste, student_id_liste):
    
    student_id = input("Hva er student-id'en din?")
    student_id.ID = student_id
    student_id_liste.append(student_id)
    
    studieplan_navn = input("Hvilket studie går du?")
    student_id.navn = studieplan_navn
    
    
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
    
    
    semester = emne.semester - 1
    
    student_id.emne[semester] =  emne

    
    for i in (6):
        if emne in emne.emne[i]: #prøve å finna ud om emne ligge i listå emne.emne
            print("Du har allerede dette emnet i studieplanen din!")
            return
        else:
            continue
    
    studiepoeng = emne.studiepoeng
    
    student_id.studiepoeng[semester].append(studiepoeng)
    
    if sum(emne.studiepoeng[semester]) > 60:
        print("Du har lagt til for mange emner")
        student_id.studiepoeng[semester].remove(studiepoeng)
    if sum(emne.studiepoeng[semester]) <= 60:
        print("\n emnet ditt er nå lagt til i studieplanen din")
    
    student_id = Studieplan(student_id, studieplan_navn, studiepoeng, emne)
        
    print(student_id)

