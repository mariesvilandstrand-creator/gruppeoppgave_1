
from legg_til_emne import*

from legg_til_emne_i_studieplan import*

from klasse import*

from fjerne_emne import*

emnekode_liste = []

student_id_liste = []

emne_dict = {
    
}

while True:
    with open("oving_10.py/menyvalg_tekst", "r", encoding="UTF-8") as fila:
        print(fila.read())
    ip = input(f"Hva vil du gjøre?").lower().strip()
    match ip:
        case "1" :
            legg_til_nytt_emne(emnekode_liste, emne_dict)
        case "2" :
            legg_til_emne_i_studieplan(emnekode_liste, student_id_liste)
        #case "3" :
            #skriv_ut_liste(emnekode_liste, semester_liste, studiepoeng_liste)
        #case "4" :
         #   skriv_ut_studieplan(studieplan_liste)
        #case "5" :
         #   sjekk_studieplan(studiepoeng_sum)
        #case "6" :
         #   lagre_emne_studieplan_fil(studieplan_liste, studiepoeng_sum)
        #case "7" :
         #   les_inn()
        #case "8" :
         #   break
        #case _:
           # print("ugyldig commando:", ip)