
def fjerne_emne(student_id_liste):
    

    if len(student_id_liste) == 1 :
        print(student_id_liste[0].emne)
        hvilket_emne = input(print("Hvilke av disse emnene vil du fjerne? (skriv navnet på faget) :")).lower().strip()
        
        del student_id_liste[0].hvilket_emne
        
        print("dette emne har blitt fjernet : \n", student_id_liste[0].emne)
        
    
        del student_id_liste[0].emne
        
    if len(student_id_liste) == 0 :
        print("Du har ikke lagt en studieplan enda!")
        
    if len(student_id_liste) > 1 :
        for x in len(student_id_liste):
            print(x + 1, student_id_liste[x])
        hvilken_studieplan = int(input(print("hvilket av disse studieplanene vil du fjerne et emne fra?"))) - 1
        del student_id_liste[hvilken_studieplan].emne
        
        
        