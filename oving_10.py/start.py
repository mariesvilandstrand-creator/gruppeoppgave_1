
from legg_til_emne import*

from legg_til_emne_i_studieplan import*

from klasse import*

from fjerne_emne import*

from lage_tom_studieplan import*

from fjerne_emne import*

from liste_over_emne import*

from skrive_ut_studieplan import*

from gyldig_studieplan import*

from sjekk_hvilke_studieplan_emne import*

from legge_i_fil import*

emnekode_liste = []

student_id_liste = []

emne_dict = {
    
}

studieplan_dict = {
    
}

studieplan_liste = []


while True:
    with open("oving_10.py/menyvalg_tekst", "r", encoding="UTF-8") as fila:
        print(fila.read())
    ip = input(f"Hva vil du gjøre?").lower().strip()
    match ip:
        case "1" :
            legg_til_nytt_emne(emnekode_liste, emne_dict)
        case "2" :
            lage_tom_studieplan(studieplan_liste)
        case "3" :
            legg_til_emne_i_studieplan(emnekode_liste, studieplan_liste, emne_dict)
        case "4" :
            fjerne_emne_fra_studieplan(emnekode_liste, studieplan_liste, emne_dict)
        case "5" :
            liste_over_emne(emnekode_liste)
        case "6" :
           skrive_ut_studieplan(studieplan_liste,)
        case "7" :
            gyldig_studieplan(studieplan_liste, emne_dict)
        case "8" :
            sjekk_emne_i_studieplan(emnekode_liste, emne_dict, studieplan_liste)
        case "9":
           lagre_emne_studieplan_fil(studieplan_liste)