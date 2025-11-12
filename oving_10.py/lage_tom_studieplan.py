
from klasse import*

def lage_tom_studieplan(studieplan_liste):
    
    student_id = int(input("Hva er student ID'en din?"))
    
    linje_navn = input("Hvilken linje går du på?")
    
    studieplan_liste.append(Studieplan(student_id, linje_navn))
    
    